#!/usr/bin/env python3
"""
Ionity Comprehensive Language Installer GUI

A conservative, auditable Tkinter-based installer for programming languages,
runtimes, SDKs, and CLI tools across Windows, macOS, and Linux.

Author: Johan Wilhelm van Antwerp
Organization: Antwerp Designs / Ionity
License: Creative Commons BY-NC-SA 4.0
Policy: POLICY 986 AED

SAFETY FIRST:
- Default mode: DRY-RUN (shows commands without executing)
- User must explicitly check "I understand and accept" to execute
- All commands are logged with timestamps
- Test in a VM before production use
- Audit all commands before executing

Requirements:
- Python 3.8 or higher (for security and EOL reasons)
- tkinter (usually included with Python)
- Internet connection for downloads and URL opening
"""

import sys
import os
import platform
import subprocess
import webbrowser
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import threading
import queue

# Version check
if sys.version_info < (3, 8):
    print("ERROR: Python 3.8 or higher is required for security reasons.")
    sys.exit(1)


class InstallerGUI:
    """Main installer GUI application."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ionity Comprehensive Language Installer")
        self.root.geometry("900x700")
        
        # Detect OS
        self.os_type = self.detect_os()
        
        # Language/tool items - comprehensive list
        self.items = [
            ("JavaScript", "javascript"),
            ("Java", "java"),
            ("PHP", "php"),
            ("Python", "python"),
            ("Rust", "rust"),
            ("Swift", "swift"),
            ("C++", "cpp"),
            ("C#", "csharp"),
            ("Ruby", "ruby"),
            ("R", "r"),
            ("SQL (clients & tools)", "sql"),
            ("Kotlin", "kotlin"),
            ("TypeScript", "typescript"),
            ("MATLAB", "matlab"),
            ("Perl", "perl"),
            ("Go", "go"),
            ("Dart", "dart"),
            ("Visual Basic", "vb"),
            ("Scala", "scala"),
            ("CSS (tooling)", "css"),
            ("Assembly (tools)", "assembly"),
            ("Objective-C", "objc"),
            ("Delphi/Object Pascal", "delphi"),
            ("Ada", "ada"),
        ]
        
        # State
        self.item_vars = {}
        self.dry_run = True
        self.confirm_var = tk.BooleanVar(value=False)
        self.log_queue = queue.Queue()
        
        # Build UI
        self.setup_ui()
        
        # Start log processor
        self.process_log_queue()
    
    def detect_os(self):
        """Detect the operating system."""
        system = platform.system().lower()
        if system == "windows":
            return "windows"
        elif system == "darwin":
            return "macos"
        elif system == "linux":
            return "linux"
        else:
            return "unknown"
    
    def setup_ui(self):
        """Set up the user interface."""
        # Title and OS info
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill=tk.X)
        
        ttk.Label(
            title_frame,
            text="Ionity Comprehensive Language Installer",
            font=("Arial", 16, "bold")
        ).pack()
        
        os_name = {
            "windows": "Windows (winget)",
            "macos": "macOS (brew)",
            "linux": "Linux (apt/dnf)",
            "unknown": "Unknown OS"
        }.get(self.os_type, "Unknown")
        
        ttk.Label(
            title_frame,
            text=f"Detected OS: {os_name}",
            font=("Arial", 10)
        ).pack()
        
        # Warning label
        warning_frame = ttk.Frame(self.root, padding="10")
        warning_frame.pack(fill=tk.X)
        ttk.Label(
            warning_frame,
            text="⚠ WARNING: Test in a VM first! Audit commands before executing!",
            foreground="red",
            font=("Arial", 10, "bold")
        ).pack()
        
        # Main content area with scrollbar
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side: item selection
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        ttk.Label(
            left_frame,
            text="Select Languages/Tools to Install:",
            font=("Arial", 11, "bold")
        ).pack(anchor=tk.W)
        
        # Canvas and scrollbar for checkboxes
        canvas_frame = ttk.Frame(left_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(canvas_frame, height=300)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create checkboxes for each item
        for display_name, key in self.items:
            var = tk.BooleanVar()
            self.item_vars[key] = var
            cb = ttk.Checkbutton(scrollable_frame, text=display_name, variable=var)
            cb.pack(anchor=tk.W, padx=5, pady=2)
        
        # Control buttons
        button_frame = ttk.Frame(left_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            button_frame,
            text="Select All",
            command=self.select_all
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Deselect All",
            command=self.deselect_all
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Preview Commands",
            command=self.preview_commands
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Open Vendor Pages",
            command=self.open_vendor_pages
        ).pack(side=tk.LEFT, padx=5)
        
        # Confirmation checkbox
        confirm_frame = ttk.Frame(left_frame)
        confirm_frame.pack(fill=tk.X, pady=5)
        
        ttk.Checkbutton(
            confirm_frame,
            text="I understand and accept the risks (required to execute)",
            variable=self.confirm_var
        ).pack(anchor=tk.W)
        
        # Install button
        install_frame = ttk.Frame(left_frame)
        install_frame.pack(fill=tk.X, pady=10)
        
        self.install_button = ttk.Button(
            install_frame,
            text="Install Selected (Dry-Run)",
            command=self.install_selected,
            style="Accent.TButton"
        )
        self.install_button.pack(fill=tk.X)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            left_frame,
            mode='determinate'
        )
        self.progress.pack(fill=tk.X, pady=5)
        
        # Right side: log output
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        ttk.Label(
            right_frame,
            text="Installation Log:",
            font=("Arial", 11, "bold")
        ).pack(anchor=tk.W)
        
        self.log_text = scrolledtext.ScrolledText(
            right_frame,
            wrap=tk.WORD,
            width=50,
            height=30,
            font=("Courier", 9)
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Clear log button
        ttk.Button(
            right_frame,
            text="Clear Log",
            command=self.clear_log
        ).pack(fill=tk.X, pady=5)
        
        # Initial log message
        self.log("Ionity Comprehensive Language Installer")
        self.log(f"Detected OS: {os_name}")
        self.log("=" * 60)
        self.log("DEFAULT MODE: DRY-RUN (commands will NOT be executed)")
        self.log("Check 'I understand and accept' to enable execution")
        self.log("=" * 60)
    
    def log(self, message):
        """Add a message to the log."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        self.log_queue.put(log_message)
    
    def process_log_queue(self):
        """Process log messages from the queue."""
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, message)
                self.log_text.see(tk.END)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.process_log_queue)
    
    def clear_log(self):
        """Clear the log text area."""
        self.log_text.delete(1.0, tk.END)
    
    def select_all(self):
        """Select all items."""
        for var in self.item_vars.values():
            var.set(True)
        self.log("Selected all items")
    
    def deselect_all(self):
        """Deselect all items."""
        for var in self.item_vars.values():
            var.set(False)
        self.log("Deselected all items")
    
    def get_selected_items(self):
        """Get list of selected item keys."""
        return [key for key, var in self.item_vars.items() if var.get()]
    
    def preview_commands(self):
        """Preview commands that would be executed."""
        selected = self.get_selected_items()
        if not selected:
            messagebox.showinfo("No Selection", "Please select at least one item.")
            return
        
        self.log("\n" + "=" * 60)
        self.log("COMMAND PREVIEW (DRY-RUN)")
        self.log("=" * 60)
        
        for item_key in selected:
            display_name = next(name for name, key in self.items if key == item_key)
            self.log(f"\n--- {display_name} ---")
            
            commands = self.get_commands_for_item(item_key)
            if not commands:
                self.log("  No commands available for this OS")
            else:
                for cmd in commands:
                    if cmd.startswith("open_url:"):
                        url = cmd.replace("open_url:", "").strip()
                        self.log(f"  [OPEN URL] {url}")
                    else:
                        self.log(f"  [COMMAND] {cmd}")
        
        self.log("\n" + "=" * 60)
    
    def open_vendor_pages(self):
        """Open vendor download pages for selected items."""
        selected = self.get_selected_items()
        if not selected:
            messagebox.showinfo("No Selection", "Please select at least one item.")
            return
        
        self.log("\n" + "=" * 60)
        self.log("Opening vendor pages...")
        self.log("=" * 60)
        
        opened_count = 0
        for item_key in selected:
            display_name = next(name for name, key in self.items if key == item_key)
            commands = self.get_commands_for_item(item_key)
            
            for cmd in commands:
                if cmd.startswith("open_url:"):
                    url = cmd.replace("open_url:", "").strip()
                    self.log(f"{display_name}: Opening {url}")
                    try:
                        webbrowser.open(url)
                        opened_count += 1
                    except Exception as e:
                        self.log(f"  ERROR: Could not open URL: {e}")
        
        if opened_count == 0:
            self.log("No vendor pages found for selected items.")
            messagebox.showinfo("No Vendor Pages", "Selected items use package managers or have no vendor pages defined.")
        else:
            self.log(f"Opened {opened_count} vendor page(s)")
    
    def install_selected(self):
        """Install selected items."""
        selected = self.get_selected_items()
        if not selected:
            messagebox.showinfo("No Selection", "Please select at least one item.")
            return
        
        # Check if user confirmed (for actual execution)
        is_dry_run = not self.confirm_var.get()
        
        if is_dry_run:
            mode_text = "DRY-RUN MODE"
        else:
            mode_text = "EXECUTION MODE"
            # Final confirmation
            result = messagebox.askyesno(
                "Execute Commands?",
                f"You are about to execute installation commands for {len(selected)} item(s).\n\n"
                "Commands will be executed with elevated privileges where needed.\n\n"
                "Continue?"
            )
            if not result:
                self.log("Installation cancelled by user")
                return
        
        self.log("\n" + "=" * 60)
        self.log(f"INSTALLATION STARTED - {mode_text}")
        self.log("=" * 60)
        
        # Disable install button during installation
        self.install_button.config(state="disabled")
        
        # Run installation in a separate thread
        thread = threading.Thread(
            target=self.run_installation,
            args=(selected, is_dry_run)
        )
        thread.daemon = True
        thread.start()
    
    def run_installation(self, selected_items, is_dry_run):
        """Run installation commands (in separate thread)."""
        total = len(selected_items)
        self.progress['maximum'] = total
        self.progress['value'] = 0
        
        for i, item_key in enumerate(selected_items):
            display_name = next(name for name, key in self.items if key == item_key)
            self.log(f"\n[{i+1}/{total}] Processing: {display_name}")
            
            commands = self.get_commands_for_item(item_key)
            if not commands:
                self.log(f"  No commands available for {self.os_type}")
                continue
            
            for cmd in commands:
                if cmd.startswith("open_url:"):
                    url = cmd.replace("open_url:", "").strip()
                    if is_dry_run:
                        self.log(f"  [DRY-RUN] Would open URL: {url}")
                    else:
                        self.log(f"  Opening URL: {url}")
                        try:
                            webbrowser.open(url)
                        except Exception as e:
                            self.log(f"  ERROR: {e}")
                elif cmd.startswith("#"):
                    # Comment/recommendation
                    self.log(f"  [INFO] {cmd}")
                else:
                    if is_dry_run:
                        self.log(f"  [DRY-RUN] Would execute: {cmd}")
                    else:
                        self.execute_command(cmd)
            
            self.progress['value'] = i + 1
            self.root.update_idletasks()
        
        self.log("\n" + "=" * 60)
        self.log("INSTALLATION COMPLETED")
        self.log("=" * 60)
        
        # Re-enable install button
        self.root.after(0, lambda: self.install_button.config(state="normal"))
    
    def execute_command(self, command):
        """Execute a single command with elevated privileges."""
        self.log(f"  Executing: {command}")
        
        try:
            # Attempt to elevate privileges
            if self.os_type == "windows":
                # On Windows, use shell=True for winget and other commands
                # Note: elevation prompts are handled by the OS
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            else:
                # On Unix-like systems, try with sudo if needed
                if command.startswith("sudo "):
                    # Already has sudo
                    cmd_list = command.split()
                else:
                    # Add sudo for package manager commands
                    if any(pm in command for pm in ["apt-get", "apt", "dnf", "yum", "brew"]):
                        if "brew" not in command:  # brew doesn't need sudo
                            cmd_list = ["sudo"] + command.split()
                        else:
                            cmd_list = command.split()
                    else:
                        cmd_list = command.split()
                
                result = subprocess.run(
                    cmd_list,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            
            if result.returncode == 0:
                self.log(f"  ✓ Success")
                if result.stdout.strip():
                    self.log(f"  Output: {result.stdout.strip()[:200]}")
            else:
                self.log(f"  ✗ Failed (exit code: {result.returncode})")
                if result.stderr.strip():
                    self.log(f"  Error: {result.stderr.strip()[:200]}")
        
        except subprocess.TimeoutExpired:
            self.log(f"  ✗ Timeout (command took longer than 5 minutes)")
        except FileNotFoundError:
            self.log(f"  ✗ Command not found (may need to install package manager first)")
        except Exception as e:
            self.log(f"  ✗ Error: {e}")
    
    def get_commands_for_item(self, item_key):
        """
        Get installation commands for a specific item based on OS.
        
        Returns a list of commands or open_url: directives.
        
        MAINTAINERS: Update package names and versions here as needed.
        For distro-specific logic, add checks for specific Linux distributions.
        """
        commands = {
            "javascript": {
                "windows": ["winget install OpenJS.NodeJS"],
                "macos": ["brew install node"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y nodejs npm"],
            },
            "java": {
                "windows": ["winget install Oracle.JDK.21"],
                "macos": ["brew install openjdk"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y default-jdk"],
            },
            "php": {
                "windows": ["winget install PHP.PHP"],
                "macos": ["brew install php"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y php php-cli"],
            },
            "python": {
                "windows": ["winget install Python.Python.3.12"],
                "macos": ["brew install python3"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y python3 python3-pip"],
            },
            "rust": {
                "windows": ["winget install Rustlang.Rust.MSVC"],
                "macos": ["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"],
                "linux": ["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"],
            },
            "swift": {
                "windows": ["open_url:https://www.swift.org/download/"],
                "macos": ["# Swift is included with Xcode. Install via: xcode-select --install"],
                "linux": ["open_url:https://www.swift.org/download/"],
            },
            "cpp": {
                "windows": ["winget install Microsoft.VisualStudio.2022.BuildTools"],
                "macos": ["# Install Xcode Command Line Tools: xcode-select --install"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y build-essential g++ clang"],
            },
            "csharp": {
                "windows": ["winget install Microsoft.DotNet.SDK.8"],
                "macos": ["brew install --cask dotnet-sdk"],
                "linux": ["open_url:https://dotnet.microsoft.com/download"],
            },
            "ruby": {
                "windows": ["winget install RubyInstallerTeam.Ruby.3.2"],
                "macos": ["brew install ruby"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y ruby-full"],
            },
            "r": {
                "windows": ["winget install RProject.R"],
                "macos": ["brew install r"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y r-base"],
            },
            "sql": {
                "windows": [
                    "winget install SQLite.SQLite",
                    "winget install PostgreSQL.PostgreSQL"
                ],
                "macos": [
                    "brew install sqlite",
                    "brew install postgresql@15"
                ],
                "linux": [
                    "sudo apt-get update",
                    "sudo apt-get install -y sqlite3",
                    "sudo apt-get install -y postgresql postgresql-client"
                ],
            },
            "kotlin": {
                "windows": ["winget install JetBrains.Kotlin.EAP"],
                "macos": ["brew install kotlin"],
                "linux": ["open_url:https://kotlinlang.org/docs/command-line.html"],
            },
            "typescript": {
                "windows": ["# Install via npm: npm install -g typescript"],
                "macos": ["# Install via npm: npm install -g typescript"],
                "linux": ["# Install via npm: npm install -g typescript"],
            },
            "matlab": {
                "windows": ["open_url:https://www.mathworks.com/products/matlab.html"],
                "macos": ["open_url:https://www.mathworks.com/products/matlab.html"],
                "linux": ["open_url:https://www.mathworks.com/products/matlab.html"],
            },
            "perl": {
                "windows": ["winget install StrawberryPerl.StrawberryPerl"],
                "macos": ["# Perl is pre-installed on macOS"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y perl"],
            },
            "go": {
                "windows": ["winget install GoLang.Go"],
                "macos": ["brew install go"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y golang"],
            },
            "dart": {
                "windows": ["winget install Dart.Dart"],
                "macos": ["brew tap dart-lang/dart", "brew install dart"],
                "linux": ["open_url:https://dart.dev/get-dart"],
            },
            "vb": {
                "windows": ["open_url:https://visualstudio.microsoft.com/"],
                "macos": ["# Visual Basic is Windows-only"],
                "linux": ["# Visual Basic is Windows-only"],
            },
            "scala": {
                "windows": ["winget install Scala.Scala.3"],
                "macos": ["brew install scala"],
                "linux": ["open_url:https://www.scala-lang.org/download/"],
            },
            "css": {
                "windows": ["# Install via npm: npm install -g postcss-cli autoprefixer"],
                "macos": ["# Install via npm: npm install -g postcss-cli autoprefixer"],
                "linux": ["# Install via npm: npm install -g postcss-cli autoprefixer"],
            },
            "assembly": {
                "windows": ["winget install NASM.NASM"],
                "macos": ["brew install nasm"],
                "linux": ["sudo apt-get update", "sudo apt-get install -y nasm"],
            },
            "objc": {
                "windows": ["# Objective-C is primarily for macOS/iOS development"],
                "macos": ["# Install Xcode from App Store or: xcode-select --install"],
                "linux": ["# Objective-C is primarily for macOS/iOS development"],
            },
            "delphi": {
                "windows": ["open_url:https://www.embarcadero.com/products/delphi"],
                "macos": ["# Delphi is primarily Windows-based"],
                "linux": ["# Delphi is primarily Windows-based, but see Free Pascal: https://www.freepascal.org/"],
            },
            "ada": {
                "windows": ["open_url:https://www.adacore.com/download"],
                "macos": ["brew install gcc"],  # GCC includes GNAT
                "linux": ["sudo apt-get update", "sudo apt-get install -y gnat gprbuild"],
            },
        }
        
        item_commands = commands.get(item_key, {})
        os_commands = item_commands.get(self.os_type, [])
        
        return os_commands


def main():
    """Main entry point."""
    # Check Python version
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8 or higher is required.")
        print("Please upgrade Python and try again.")
        sys.exit(1)
    
    # Check if tkinter is available
    try:
        import tkinter
    except ImportError:
        print("ERROR: tkinter is not available.")
        print("Please install tkinter:")
        print("  - Ubuntu/Debian: sudo apt-get install python3-tk")
        print("  - Fedora: sudo dnf install python3-tkinter")
        print("  - macOS: tkinter is included with Python from python.org")
        print("  - Windows: tkinter is included with Python from python.org")
        sys.exit(1)
    
    root = tk.Tk()
    app = InstallerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
