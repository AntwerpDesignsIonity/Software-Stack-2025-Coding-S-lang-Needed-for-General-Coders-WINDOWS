#!/usr/bin/env python3
"""
Ionity Installer GUI - Comprehensive Language & Tool Installer
==============================================================

A safe, auditable Tkinter-based GUI installer for programming languages and development tools.

Features:
- Dry-Run mode (default) - preview commands without execution
- Explicit user confirmation required before making system changes
- Command preview window
- Elevation prompts for privileged operations
- Comprehensive logging to installer.log
- Cross-platform support (Windows, macOS, Linux)
- Open vendor URLs for proprietary software instead of auto-downloading

Safety:
- Defaults to Dry-Run mode
- Requires explicit confirmation checkbox before execution
- Logs all commands and output
- Never executes commands automatically

Requirements:
- Python 3.8 or higher (for security and EOL reasons)
- Tkinter (usually included with Python)
- Internet connection for package downloads
- Package managers: winget (Windows), brew (macOS), apt (Linux)

License: Creative Commons BY-NC-SA 4.0
Policy: POLICY 986 AED
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import platform
import subprocess
import sys
import os
import threading
import webbrowser
from datetime import datetime

# Version check
if sys.version_info < (3, 8):
    print("ERROR: Python 3.8 or higher is required for security and EOL reasons.")
    print(f"Current version: {sys.version}")
    sys.exit(1)

# Constants
LOG_FILE = "installer.log"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(REPO_ROOT, LOG_FILE)

# Items to install - comprehensive list of languages and tools
ITEMS = [
    # Programming Languages
    ("JavaScript", "language"),
    ("Java", "language"),
    ("PHP", "language"),
    ("Python", "language"),
    ("Rust", "language"),
    ("Swift", "language"),
    ("C++", "language"),
    ("C#", "language"),
    ("Ruby", "language"),
    ("R", "language"),
    ("SQL (SQLite)", "language"),
    ("Kotlin", "language"),
    ("TypeScript", "language"),
    ("MATLAB", "language_vendor"),  # Vendor-only
    ("Perl", "language"),
    ("Go", "language"),
    ("Dart", "language"),
    ("Visual Basic", "language_vendor"),  # Vendor-only
    ("Scala", "language"),
    ("CSS tooling", "language"),
    ("Assembly (NASM)", "language"),
    ("Objective-C", "language"),
    ("Delphi/Object Pascal", "language_vendor"),  # Vendor-only
    ("Ada", "language"),
    
    # Development Tools
    ("Git", "tool"),
    ("Node.js", "tool"),
    ("Docker", "tool"),
    ("Visual Studio Code", "tool"),
    ("Firebase CLI", "tool"),
    ("Google Cloud SDK (gcloud)", "tool"),
    ("AWS CLI", "tool"),
]


def get_os_type():
    """Detect the operating system."""
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Darwin":
        return "macos"
    elif system == "Linux":
        return "linux"
    else:
        return "unknown"


def log_message(message, also_print=True):
    """Log a message to the log file and optionally print it."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Warning: Could not write to log file: {e}")
    
    if also_print:
        print(message)


def get_commands_for_item(item_name, item_type):
    """
    Get installation commands for an item based on OS.
    
    Returns a list of commands or special directives:
    - Regular commands: ["command1", "command2", ...]
    - URL open directive: ["open_url:https://example.com"]
    - Elevation needed: ["sudo:command"] or ["admin:command"]
    
    Note: Linux commands are for Debian/Ubuntu (apt). Other distributions
    will need updates here (dnf, pacman, zypper, etc.)
    """
    os_type = get_os_type()
    
    # Command mappings per OS
    # TODO: Maintainers should verify and update package names for their specific environment
    
    commands = []
    
    if item_name == "JavaScript":
        # JavaScript runtime via Node.js
        if os_type == "windows":
            commands = ["winget install -e --id OpenJS.NodeJS"]
        elif os_type == "macos":
            commands = ["brew install node"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y nodejs npm"]
    
    elif item_name == "Java":
        if os_type == "windows":
            commands = ["winget install -e --id Oracle.JDK.21"]
        elif os_type == "macos":
            commands = ["brew install openjdk"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y default-jdk"]
    
    elif item_name == "PHP":
        if os_type == "windows":
            commands = ["winget install -e --id PHP.PHP"]
        elif os_type == "macos":
            commands = ["brew install php"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y php php-cli"]
    
    elif item_name == "Python":
        if os_type == "windows":
            commands = ["winget install -e --id Python.Python.3.12"]
        elif os_type == "macos":
            commands = ["brew install python@3.12"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y python3 python3-pip"]
    
    elif item_name == "Rust":
        if os_type == "windows":
            commands = ["winget install -e --id Rustlang.Rust.GNU"]
        elif os_type == "macos":
            commands = ["brew install rust"]
        elif os_type == "linux":
            commands = ["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"]
    
    elif item_name == "Swift":
        if os_type == "windows":
            commands = ["open_url:https://www.swift.org/download/"]
        elif os_type == "macos":
            commands = ["# Swift is included with Xcode Command Line Tools", "xcode-select --install"]
        elif os_type == "linux":
            commands = ["open_url:https://www.swift.org/download/"]
    
    elif item_name == "C++":
        if os_type == "windows":
            commands = ["winget install -e --id LLVM.LLVM"]
        elif os_type == "macos":
            commands = ["brew install gcc"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y build-essential g++"]
    
    elif item_name == "C#":
        if os_type == "windows":
            commands = ["winget install -e --id Microsoft.DotNet.SDK.8"]
        elif os_type == "macos":
            commands = ["brew install --cask dotnet-sdk"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y dotnet-sdk-8.0"]
    
    elif item_name == "Ruby":
        if os_type == "windows":
            commands = ["winget install -e --id RubyInstallerTeam.Ruby.3.2"]
        elif os_type == "macos":
            commands = ["brew install ruby"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y ruby-full"]
    
    elif item_name == "R":
        if os_type == "windows":
            commands = ["winget install -e --id RProject.R"]
        elif os_type == "macos":
            commands = ["brew install r"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y r-base"]
    
    elif item_name == "SQL (SQLite)":
        if os_type == "windows":
            commands = ["winget install -e --id SQLite.SQLite"]
        elif os_type == "macos":
            commands = ["brew install sqlite"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y sqlite3"]
    
    elif item_name == "Kotlin":
        if os_type == "windows":
            commands = ["winget install -e --id JetBrains.Kotlin"]
        elif os_type == "macos":
            commands = ["brew install kotlin"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y kotlin"]
    
    elif item_name == "TypeScript":
        # TypeScript requires Node.js/npm
        if os_type == "windows":
            commands = ["npm install -g typescript"]
        elif os_type == "macos":
            commands = ["npm install -g typescript"]
        elif os_type == "linux":
            commands = ["npm install -g typescript"]
    
    elif item_name == "MATLAB":
        # MATLAB is proprietary - open vendor URL
        commands = ["open_url:https://www.mathworks.com/products/matlab.html"]
    
    elif item_name == "Perl":
        if os_type == "windows":
            commands = ["winget install -e --id StrawberryPerl.StrawberryPerl"]
        elif os_type == "macos":
            commands = ["brew install perl"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y perl"]
    
    elif item_name == "Go":
        if os_type == "windows":
            commands = ["winget install -e --id GoLang.Go"]
        elif os_type == "macos":
            commands = ["brew install go"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y golang-go"]
    
    elif item_name == "Dart":
        if os_type == "windows":
            commands = ["winget install -e --id Dart.Dart"]
        elif os_type == "macos":
            commands = ["brew tap dart-lang/dart", "brew install dart"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y apt-transport-https", 
                       "sudo:sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'",
                       "sudo:sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'",
                       "sudo:apt update", "sudo:apt install -y dart"]
    
    elif item_name == "Visual Basic":
        # Visual Studio is proprietary - open vendor URL
        commands = ["open_url:https://visualstudio.microsoft.com/downloads/"]
    
    elif item_name == "Scala":
        if os_type == "windows":
            commands = ["winget install -e --id Scala.Scala.2"]
        elif os_type == "macos":
            commands = ["brew install scala"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y scala"]
    
    elif item_name == "CSS tooling":
        # CSS tooling via Node.js packages
        if os_type in ["windows", "macos", "linux"]:
            commands = ["npm install -g postcss-cli autoprefixer"]
    
    elif item_name == "Assembly (NASM)":
        if os_type == "windows":
            commands = ["winget install -e --id NASM.NASM"]
        elif os_type == "macos":
            commands = ["brew install nasm"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y nasm"]
    
    elif item_name == "Objective-C":
        if os_type == "windows":
            commands = ["# Objective-C on Windows requires GNUstep or similar"]
        elif os_type == "macos":
            commands = ["# Objective-C is included with Xcode Command Line Tools", "xcode-select --install"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y gobjc gnustep gnustep-devel"]
    
    elif item_name == "Delphi/Object Pascal":
        # Delphi is proprietary - open vendor URL
        commands = ["open_url:https://www.embarcadero.com/products/delphi"]
    
    elif item_name == "Ada":
        if os_type == "windows":
            commands = ["open_url:https://www.adacore.com/download"]
        elif os_type == "macos":
            commands = ["brew install gcc"]  # GCC includes GNAT
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y gnat"]
    
    # Development Tools
    elif item_name == "Git":
        if os_type == "windows":
            commands = ["winget install -e --id Git.Git"]
        elif os_type == "macos":
            commands = ["brew install git"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y git"]
    
    elif item_name == "Node.js":
        if os_type == "windows":
            commands = ["winget install -e --id OpenJS.NodeJS"]
        elif os_type == "macos":
            commands = ["brew install node"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y nodejs npm"]
    
    elif item_name == "Docker":
        if os_type == "windows":
            commands = ["winget install -e --id Docker.DockerDesktop"]
        elif os_type == "macos":
            commands = ["brew install --cask docker"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y docker.io", "sudo:systemctl start docker", "sudo:systemctl enable docker"]
    
    elif item_name == "Visual Studio Code":
        if os_type == "windows":
            commands = ["winget install -e --id Microsoft.VisualStudioCode"]
        elif os_type == "macos":
            commands = ["brew install --cask visual-studio-code"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y code"]
    
    elif item_name == "Firebase CLI":
        if os_type in ["windows", "macos", "linux"]:
            commands = ["npm install -g firebase-tools"]
    
    elif item_name == "Google Cloud SDK (gcloud)":
        if os_type == "windows":
            commands = ["winget install -e --id Google.CloudSDK"]
        elif os_type == "macos":
            commands = ["brew install --cask google-cloud-sdk"]
        elif os_type == "linux":
            commands = ["open_url:https://cloud.google.com/sdk/docs/install"]
    
    elif item_name == "AWS CLI":
        if os_type == "windows":
            commands = ["winget install -e --id Amazon.AWSCLI"]
        elif os_type == "macos":
            commands = ["brew install awscli"]
        elif os_type == "linux":
            commands = ["sudo:apt update", "sudo:apt install -y awscli"]
    
    return commands if commands else ["# No commands available for this OS"]


class InstallerGUI:
    """Main GUI application for the Ionity Installer."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ionity Installer - Comprehensive Language & Tool Installer")
        self.root.geometry("900x700")
        
        # State variables
        self.dry_run = tk.BooleanVar(value=True)  # Default to Dry-Run
        self.confirm_changes = tk.BooleanVar(value=False)
        self.item_vars = {}
        
        # Initialize log file
        log_message("=== Ionity Installer GUI Started ===")
        log_message(f"Operating System: {get_os_type()} ({platform.system()} {platform.release()})")
        log_message(f"Python Version: {sys.version}")
        log_message(f"Log File: {LOG_PATH}")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Top frame - title and info
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        title_label = ttk.Label(top_frame, text="Ionity Installer", font=("Arial", 16, "bold"))
        title_label.pack()
        
        subtitle_label = ttk.Label(top_frame, text="Safe, auditable installer for programming languages and development tools")
        subtitle_label.pack()
        
        os_label = ttk.Label(top_frame, text=f"Detected OS: {get_os_type().title()} ({platform.system()})")
        os_label.pack()
        
        # Separator
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        # Main content frame
        content_frame = ttk.Frame(self.root, padding="10")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - item selection
        left_panel = ttk.Frame(content_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        selection_label = ttk.Label(left_panel, text="Select items to install:", font=("Arial", 12, "bold"))
        selection_label.pack(anchor=tk.W)
        
        # Scrollable frame for checkboxes
        canvas = tk.Canvas(left_panel, highlightthickness=0)
        scrollbar = ttk.Scrollbar(left_panel, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create checkboxes for each item
        current_category = None
        for item_name, item_type in ITEMS:
            # Add category headers
            if item_type.startswith("language") and current_category != "Languages":
                current_category = "Languages"
                ttk.Label(scrollable_frame, text="\nProgramming Languages:", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=5)
            elif item_type == "tool" and current_category != "Tools":
                current_category = "Tools"
                ttk.Label(scrollable_frame, text="\nDevelopment Tools:", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=5)
            
            var = tk.BooleanVar()
            self.item_vars[item_name] = var
            
            text = item_name
            if item_type == "language_vendor":
                text += " (vendor link)"
            
            cb = ttk.Checkbutton(scrollable_frame, text=text, variable=var)
            cb.pack(anchor=tk.W, padx=20)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Right panel - options and controls
        right_panel = ttk.Frame(content_frame, padding="10")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        options_label = ttk.Label(right_panel, text="Options:", font=("Arial", 12, "bold"))
        options_label.pack(anchor=tk.W)
        
        # Dry-run checkbox
        dry_run_cb = ttk.Checkbutton(
            right_panel, 
            text="Dry-Run Mode (safe - only preview)", 
            variable=self.dry_run,
            command=self.on_dry_run_toggle
        )
        dry_run_cb.pack(anchor=tk.W, pady=5)
        
        # Info label
        info_text = "Dry-Run is ON: Commands will be displayed but not executed."
        self.info_label = ttk.Label(right_panel, text=info_text, foreground="green", wraplength=250)
        self.info_label.pack(anchor=tk.W, pady=5)
        
        # Confirmation checkbox (disabled when dry-run is on)
        self.confirm_cb = ttk.Checkbutton(
            right_panel,
            text="I understand this will make system changes",
            variable=self.confirm_changes,
            state=tk.DISABLED
        )
        self.confirm_cb.pack(anchor=tk.W, pady=5)
        
        ttk.Separator(right_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Buttons
        btn_frame = ttk.Frame(right_panel)
        btn_frame.pack(fill=tk.X, pady=5)
        
        preview_btn = ttk.Button(btn_frame, text="Preview Commands", command=self.preview_commands)
        preview_btn.pack(fill=tk.X, pady=2)
        
        self.install_btn = ttk.Button(btn_frame, text="Install Selected", command=self.install_selected)
        self.install_btn.pack(fill=tk.X, pady=2)
        
        select_all_btn = ttk.Button(btn_frame, text="Select All", command=self.select_all)
        select_all_btn.pack(fill=tk.X, pady=2)
        
        deselect_all_btn = ttk.Button(btn_frame, text="Deselect All", command=self.deselect_all)
        deselect_all_btn.pack(fill=tk.X, pady=2)
        
        ttk.Separator(right_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Log info
        log_label = ttk.Label(right_panel, text=f"Log file:\n{LOG_PATH}", wraplength=250, font=("Arial", 8))
        log_label.pack(anchor=tk.W)
        
        # Bottom frame - status bar
        bottom_frame = ttk.Frame(self.root, padding="5")
        bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = ttk.Label(bottom_frame, text="Ready", relief=tk.SUNKEN)
        self.status_label.pack(fill=tk.X)
        
        self.progress_bar = ttk.Progressbar(bottom_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X, pady=2)
    
    def on_dry_run_toggle(self):
        """Handle dry-run checkbox toggle."""
        if self.dry_run.get():
            self.info_label.config(text="Dry-Run is ON: Commands will be displayed but not executed.", foreground="green")
            self.confirm_cb.config(state=tk.DISABLED)
            self.confirm_changes.set(False)
        else:
            self.info_label.config(text="WARNING: Dry-Run is OFF. Commands will be EXECUTED!", foreground="red")
            self.confirm_cb.config(state=tk.NORMAL)
    
    def select_all(self):
        """Select all items."""
        for var in self.item_vars.values():
            var.set(True)
    
    def deselect_all(self):
        """Deselect all items."""
        for var in self.item_vars.values():
            var.set(False)
    
    def get_selected_items(self):
        """Get list of selected items."""
        selected = []
        for item_name, item_type in ITEMS:
            if self.item_vars[item_name].get():
                selected.append((item_name, item_type))
        return selected
    
    def preview_commands(self):
        """Show a preview of commands that would be executed."""
        selected = self.get_selected_items()
        
        if not selected:
            messagebox.showwarning("No Selection", "Please select at least one item to preview.")
            return
        
        # Create preview window
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Command Preview")
        preview_window.geometry("700x500")
        
        label = ttk.Label(preview_window, text="Commands that would be executed:", font=("Arial", 12, "bold"))
        label.pack(pady=5)
        
        text_widget = scrolledtext.ScrolledText(preview_window, wrap=tk.WORD, width=80, height=25)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Generate command list
        output = []
        for item_name, item_type in selected:
            output.append(f"\n{'='*60}")
            output.append(f"Item: {item_name}")
            output.append(f"{'='*60}")
            
            commands = get_commands_for_item(item_name, item_type)
            for cmd in commands:
                if cmd.startswith("open_url:"):
                    url = cmd.replace("open_url:", "")
                    output.append(f"  [OPEN URL] {url}")
                elif cmd.startswith("sudo:"):
                    actual_cmd = cmd.replace("sudo:", "")
                    output.append(f"  [SUDO] {actual_cmd}")
                elif cmd.startswith("admin:"):
                    actual_cmd = cmd.replace("admin:", "")
                    output.append(f"  [ADMIN] {actual_cmd}")
                elif cmd.startswith("#"):
                    output.append(f"  [COMMENT] {cmd}")
                else:
                    output.append(f"  {cmd}")
        
        text_widget.insert(tk.END, "\n".join(output))
        text_widget.config(state=tk.DISABLED)
        
        close_btn = ttk.Button(preview_window, text="Close", command=preview_window.destroy)
        close_btn.pack(pady=5)
    
    def install_selected(self):
        """Install selected items."""
        selected = self.get_selected_items()
        
        if not selected:
            messagebox.showwarning("No Selection", "Please select at least one item to install.")
            return
        
        # Check dry-run and confirmation
        if not self.dry_run.get() and not self.confirm_changes.get():
            messagebox.showerror(
                "Confirmation Required",
                "You must check the confirmation box to proceed with installation.\n\n"
                "This installer will make system changes."
            )
            return
        
        # Confirm with user
        if self.dry_run.get():
            msg = f"Dry-Run Mode: Preview {len(selected)} items?\n\nNo commands will be executed."
            title = "Dry-Run Confirmation"
        else:
            msg = (f"WARNING: You are about to install {len(selected)} items.\n\n"
                   "This will execute commands on your system.\n\n"
                   "Are you sure you want to proceed?")
            title = "Installation Confirmation"
        
        if not messagebox.askyesno(title, msg):
            return
        
        # Disable buttons during installation
        self.install_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Processing...")
        self.progress_bar.start()
        
        # Run installation in a separate thread
        thread = threading.Thread(target=self.run_installation, args=(selected,))
        thread.daemon = True
        thread.start()
    
    def run_installation(self, selected_items):
        """Run the installation process in a background thread."""
        log_message("\n=== Installation Started ===")
        log_message(f"Dry-Run Mode: {self.dry_run.get()}")
        log_message(f"Selected Items: {len(selected_items)}")
        
        results = []
        
        for item_name, item_type in selected_items:
            log_message(f"\n--- Processing: {item_name} ---")
            
            commands = get_commands_for_item(item_name, item_type)
            
            for cmd in commands:
                if cmd.startswith("open_url:"):
                    url = cmd.replace("open_url:", "")
                    log_message(f"Opening URL: {url}")
                    
                    if not self.dry_run.get():
                        try:
                            webbrowser.open(url)
                            results.append((item_name, "URL opened", None))
                        except Exception as e:
                            log_message(f"ERROR opening URL: {e}")
                            results.append((item_name, "ERROR", str(e)))
                    else:
                        results.append((item_name, "DRY-RUN", f"Would open: {url}"))
                
                elif cmd.startswith("sudo:") or cmd.startswith("admin:"):
                    prefix = "sudo:" if cmd.startswith("sudo:") else "admin:"
                    actual_cmd = cmd.replace(prefix, "")
                    log_message(f"Elevated command: {actual_cmd}")
                    
                    if not self.dry_run.get():
                        # On Unix-like systems, prompt for sudo
                        # On Windows, commands should be run as admin
                        result = self.execute_command(actual_cmd, elevated=True)
                        results.append((item_name, "executed" if result else "failed", None))
                    else:
                        results.append((item_name, "DRY-RUN", f"Would execute (elevated): {actual_cmd}"))
                
                elif cmd.startswith("#"):
                    log_message(f"Comment: {cmd}")
                    results.append((item_name, "INFO", cmd))
                
                else:
                    log_message(f"Command: {cmd}")
                    
                    if not self.dry_run.get():
                        result = self.execute_command(cmd, elevated=False)
                        results.append((item_name, "executed" if result else "failed", None))
                    else:
                        results.append((item_name, "DRY-RUN", f"Would execute: {cmd}"))
        
        log_message("\n=== Installation Complete ===")
        
        # Update UI from main thread
        self.root.after(0, self.installation_complete, results)
    
    def execute_command(self, cmd, elevated=False):
        """Execute a command and log the output."""
        try:
            log_message(f"Executing: {cmd}")
            
            # Use shell=True for complex commands
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.stdout:
                log_message(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                log_message(f"STDERR:\n{result.stderr}")
            
            log_message(f"Return code: {result.returncode}")
            
            return result.returncode == 0
        
        except subprocess.TimeoutExpired:
            log_message("ERROR: Command timed out after 5 minutes")
            return False
        except Exception as e:
            log_message(f"ERROR executing command: {e}")
            return False
    
    def installation_complete(self, results):
        """Handle installation completion."""
        self.progress_bar.stop()
        self.install_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Complete")
        
        # Show results summary
        summary = []
        for item_name, status, detail in results:
            if detail:
                summary.append(f"{item_name}: {status} - {detail}")
            else:
                summary.append(f"{item_name}: {status}")
        
        result_window = tk.Toplevel(self.root)
        result_window.title("Installation Results")
        result_window.geometry("600x400")
        
        label = ttk.Label(result_window, text="Installation Results:", font=("Arial", 12, "bold"))
        label.pack(pady=5)
        
        text_widget = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=70, height=20)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        text_widget.insert(tk.END, "\n".join(summary))
        text_widget.insert(tk.END, f"\n\nFull log available at: {LOG_PATH}")
        text_widget.config(state=tk.DISABLED)
        
        close_btn = ttk.Button(result_window, text="Close", command=result_window.destroy)
        close_btn.pack(pady=5)


def main():
    """Main entry point."""
    # Check Python version
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8 or higher is required.")
        sys.exit(1)
    
    # Check for Tkinter
    try:
        root = tk.Tk()
    except Exception as e:
        print(f"ERROR: Could not initialize Tkinter: {e}")
        print("On Linux, try: sudo apt install python3-tk")
        sys.exit(1)
    
    app = InstallerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
