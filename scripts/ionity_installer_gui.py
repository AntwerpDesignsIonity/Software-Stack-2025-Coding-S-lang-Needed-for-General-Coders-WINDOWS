#!/usr/bin/env python3
"""
Ionity Installer GUI - Conservative, Auditable Software Stack Installer

Author: Johan Wilhelm van Antwerp / Ionity
License: Creative Commons BY-NC-SA 4.0
Purpose: A Tkinter-based GUI to help users install common developer SDKs, 
         CLIs and runtimes across Windows, macOS and Debian-based Linux.

Safety Features:
- Default Dry-Run mode (lists commands without executing)
- Explicit confirmation required before execution
- OS detection with appropriate package manager commands
- Command preview functionality
- Comprehensive logging

Usage:
    python3 scripts/ionity_installer_gui.py
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import platform
import subprocess
import sys
import os
import webbrowser
from datetime import datetime
import ctypes

# Version
VERSION = "1.0.0"

class InstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Ionity Software Stack Installer v{VERSION}")
        self.root.geometry("900x700")
        
        # Detect OS
        self.os_type = self.detect_os()
        
        # Variables
        self.dry_run = tk.BooleanVar(value=True)
        self.accept_terms = tk.BooleanVar(value=False)
        self.item_vars = {}
        
        # Log file setup
        self.log_file = os.path.join(os.path.dirname(__file__), "..", "installer_log.txt")
        
        # Create UI
        self.create_ui()
        
        # Initial log message
        self.log_message(f"Ionity Installer v{VERSION} started")
        self.log_message(f"Detected OS: {self.os_type}")
        
    def detect_os(self):
        """Detect the operating system"""
        system = platform.system().lower()
        if system == "windows":
            return "windows"
        elif system == "darwin":
            return "macos"
        elif system == "linux":
            # Check for Debian/Ubuntu
            if os.path.exists("/etc/debian_version"):
                return "linux_debian"
            return "linux_other"
        return "unknown"
    
    def create_ui(self):
        """Create the main UI"""
        # Top frame - OS info and options
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        ttk.Label(top_frame, text=f"Detected OS: {self.os_type}", 
                 font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        ttk.Checkbutton(top_frame, text="Dry-Run Mode (Preview only, don't execute)", 
                       variable=self.dry_run).pack(anchor=tk.W, pady=5)
        
        ttk.Checkbutton(top_frame, text="I understand and accept (Required to install)", 
                       variable=self.accept_terms).pack(anchor=tk.W)
        
        # Middle frame - Selection
        middle_frame = ttk.Frame(self.root, padding="10")
        middle_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(middle_frame, text="Select Software to Install:", 
                 font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        # Create notebook for categories
        notebook = ttk.Notebook(middle_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Define categories and items
        categories = self.get_categories()
        
        for category_name, items in categories.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=category_name)
            
            # Create scrollable frame
            canvas = tk.Canvas(frame)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e, c=canvas: c.configure(scrollregion=c.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Add items
            for item_id, item_name in items:
                var = tk.BooleanVar(value=False)
                self.item_vars[item_id] = var
                ttk.Checkbutton(scrollable_frame, text=item_name, 
                              variable=var).pack(anchor=tk.W, padx=10, pady=2)
            
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Select All button
        btn_frame = ttk.Frame(middle_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="Select All", 
                  command=self.select_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Deselect All", 
                  command=self.deselect_all).pack(side=tk.LEFT, padx=5)
        
        # Bottom frame - Actions and log
        bottom_frame = ttk.Frame(self.root, padding="10")
        bottom_frame.pack(fill=tk.BOTH, expand=True)
        
        # Action buttons
        action_frame = ttk.Frame(bottom_frame)
        action_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(action_frame, text="Preview Commands", 
                  command=self.preview_commands).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Install Selected", 
                  command=self.install_selected).pack(side=tk.LEFT, padx=5)
        
        # Log area
        ttk.Label(bottom_frame, text="Log:", font=("Arial", 9, "bold")).pack(anchor=tk.W)
        self.log_text = scrolledtext.ScrolledText(bottom_frame, height=10, 
                                                   wrap=tk.WORD, font=("Courier", 8))
        self.log_text.pack(fill=tk.BOTH, expand=True)
    
    def get_categories(self):
        """Define categories and items"""
        return {
            "Languages - Core": [
                ("python", "Python (pip, virtualenv, pipx)"),
                ("javascript", "JavaScript (Node.js, npm)"),
                ("typescript", "TypeScript"),
                ("java", "Java (OpenJDK)"),
                ("csharp", "C# (.NET SDK)"),
                ("cpp", "C++"),
                ("rust", "Rust (rustup, cargo)"),
                ("go", "Go"),
                ("php", "PHP & Composer"),
                ("ruby", "Ruby"),
            ],
            "Languages - Extended": [
                ("swift", "Swift"),
                ("kotlin", "Kotlin"),
                ("scala", "Scala"),
                ("perl", "Perl"),
                ("r", "R"),
                ("dart", "Dart"),
                ("ada", "Ada (GNAT)"),
                ("objectivec", "Objective-C (Xcode tools)"),
                ("delphi", "Delphi / Object Pascal (Free Pascal)"),
                ("assembly", "Assembly (NASM)"),
            ],
            "Specialized Tools": [
                ("matlab", "MATLAB (Vendor page)"),
                ("visualbasic", "Visual Basic (Visual Studio link)"),
                ("sql", "SQL Tools (sqlite3, postgresql-client)"),
            ],
            "Web & CSS": [
                ("css_tools", "CSS Tools (PostCSS, Autoprefixer)"),
            ],
            "Development Tools": [
                ("git", "Git"),
                ("docker", "Docker"),
                ("vscode", "Visual Studio Code"),
                ("firebase", "Firebase CLI"),
                ("gcloud", "Google Cloud SDK"),
                ("awscli", "AWS CLI"),
                ("yarn", "Yarn"),
                ("pnpm", "pnpm"),
            ],
        }
    
    def select_all(self):
        """Select all items"""
        for var in self.item_vars.values():
            var.set(True)
        self.log_message("Selected all items")
    
    def deselect_all(self):
        """Deselect all items"""
        for var in self.item_vars.values():
            var.set(False)
        self.log_message("Deselected all items")
    
    def get_commands_for_item(self, item_id):
        """Get installation commands for an item based on OS"""
        commands_map = {
            "windows": {
                "python": ["winget install -e --id Python.Python.3.12"],
                "javascript": ["winget install -e --id OpenJS.NodeJS"],
                "typescript": ["npm install -g typescript"],
                "java": ["winget install -e --id Oracle.JDK.21"],
                "csharp": ["winget install -e --id Microsoft.DotNet.SDK.8"],
                "cpp": ["winget install -e --id LLVM.LLVM"],
                "rust": ["winget install -e --id Rustlang.Rust.GNU"],
                "go": ["winget install -e --id GoLang.Go"],
                "php": ["winget install -e --id shivammathur.php"],
                "ruby": ["winget install -e --id RubyInstallerTeam.Ruby.3.2"],
                "swift": ["open_url:https://www.swift.org/download/"],
                "kotlin": ["winget install -e --id JetBrains.Kotlin"],
                "scala": ["winget install -e --id Scala.Scala.3"],
                "perl": ["winget install -e --id StrawberryPerl.StrawberryPerl"],
                "r": ["winget install -e --id RProject.R"],
                "dart": ["winget install -e --id Dart.Dart"],
                "ada": ["open_url:https://www.adacore.com/download"],
                "objectivec": ["open_url:https://developer.apple.com/xcode/"],
                "delphi": ["open_url:https://www.freepascal.org/"],
                "assembly": ["winget install -e --id NASM.NASM"],
                "matlab": ["open_url:https://www.mathworks.com/downloads/"],
                "visualbasic": ["open_url:https://visualstudio.microsoft.com/downloads/"],
                "sql": ["winget install -e --id SQLite.SQLite", "winget install -e --id PostgreSQL.PostgreSQL"],
                "css_tools": ["npm install -g postcss-cli autoprefixer"],
                "git": ["winget install -e --id Git.Git"],
                "docker": ["winget install -e --id Docker.DockerDesktop"],
                "vscode": ["winget install -e --id Microsoft.VisualStudioCode"],
                "firebase": ["npm install -g firebase-tools"],
                "gcloud": ["open_url:https://cloud.google.com/sdk/docs/install"],
                "awscli": ["winget install -e --id Amazon.AWSCLI"],
                "yarn": ["npm install -g yarn"],
                "pnpm": ["npm install -g pnpm"],
            },
            "macos": {
                "python": ["brew install python@3.12"],
                "javascript": ["brew install node"],
                "typescript": ["npm install -g typescript"],
                "java": ["brew install openjdk@21"],
                "csharp": ["brew install --cask dotnet-sdk"],
                "cpp": ["xcode-select --install"],
                "rust": ["# Download Rust installer (official rustup)", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"],
                "go": ["brew install go"],
                "php": ["brew install php", "brew install composer"],
                "ruby": ["brew install ruby"],
                "swift": ["xcode-select --install"],
                "kotlin": ["brew install kotlin"],
                "scala": ["brew install scala"],
                "perl": ["brew install perl"],
                "r": ["brew install r"],
                "dart": ["brew install dart"],
                "ada": ["brew install gnat"],
                "objectivec": ["xcode-select --install"],
                "delphi": ["brew install fpc"],
                "assembly": ["brew install nasm"],
                "matlab": ["open_url:https://www.mathworks.com/downloads/"],
                "visualbasic": ["open_url:https://visualstudio.microsoft.com/vs/mac/"],
                "sql": ["brew install sqlite", "brew install postgresql"],
                "css_tools": ["npm install -g postcss-cli autoprefixer"],
                "git": ["brew install git"],
                "docker": ["brew install --cask docker"],
                "vscode": ["brew install --cask visual-studio-code"],
                "firebase": ["npm install -g firebase-tools"],
                "gcloud": ["brew install --cask google-cloud-sdk"],
                "awscli": ["brew install awscli"],
                "yarn": ["npm install -g yarn"],
                "pnpm": ["npm install -g pnpm"],
            },
            "linux_debian": {
                "python": ["sudo apt update", "sudo apt install -y python3 python3-pip python3-venv pipx"],
                "javascript": ["curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -", "sudo apt install -y nodejs"],
                "typescript": ["npm install -g typescript"],
                "java": ["sudo apt update", "sudo apt install -y openjdk-21-jdk"],
                "csharp": ["# NOTE: Update ubuntu version (22.04) if needed for your system",
                          "wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb", 
                          "sudo dpkg -i packages-microsoft-prod.deb", "sudo apt update", "sudo apt install -y dotnet-sdk-8.0"],
                "cpp": ["sudo apt update", "sudo apt install -y build-essential clang"],
                "rust": ["# Download Rust installer (official rustup)", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"],
                "go": ["sudo apt update", "sudo apt install -y golang"],
                "php": ["sudo apt update", "sudo apt install -y php php-cli composer"],
                "ruby": ["sudo apt update", "sudo apt install -y ruby-full"],
                "swift": ["open_url:https://www.swift.org/download/"],
                "kotlin": ["sudo snap install --classic kotlin"],
                "scala": ["sudo apt update", "sudo apt install -y scala"],
                "perl": ["sudo apt update", "sudo apt install -y perl"],
                "r": ["sudo apt update", "sudo apt install -y r-base"],
                "dart": ["sudo apt update", "sudo apt install -y apt-transport-https", 
                        "wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/dart.gpg",
                        "echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list",
                        "sudo apt update", "sudo apt install -y dart"],
                "ada": ["sudo apt update", "sudo apt install -y gnat"],
                "objectivec": ["open_url:https://developer.apple.com/xcode/"],
                "delphi": ["sudo apt update", "sudo apt install -y fpc"],
                "assembly": ["sudo apt update", "sudo apt install -y nasm"],
                "matlab": ["open_url:https://www.mathworks.com/downloads/"],
                "visualbasic": ["open_url:https://visualstudio.microsoft.com/downloads/"],
                "sql": ["sudo apt update", "sudo apt install -y sqlite3 postgresql-client"],
                "css_tools": ["npm install -g postcss-cli autoprefixer"],
                "git": ["sudo apt update", "sudo apt install -y git"],
                "docker": ["# Docker installation script from official source", 
                          "curl -fsSL https://get.docker.com -o get-docker.sh", 
                          "# Review get-docker.sh before running", "sudo sh get-docker.sh"],
                "vscode": ["sudo snap install --classic code"],
                "firebase": ["npm install -g firebase-tools"],
                "gcloud": ["open_url:https://cloud.google.com/sdk/docs/install"],
                "awscli": ["sudo apt update", "sudo apt install -y awscli"],
                "yarn": ["npm install -g yarn"],
                "pnpm": ["npm install -g pnpm"],
            },
        }
        
        return commands_map.get(self.os_type, {}).get(item_id, [f"# No commands defined for {item_id} on {self.os_type}"])
    
    def preview_commands(self):
        """Preview commands that would be executed"""
        selected_items = [item_id for item_id, var in self.item_vars.items() if var.get()]
        
        if not selected_items:
            messagebox.showinfo("Info", "No items selected")
            return
        
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Command Preview")
        preview_window.geometry("700x500")
        
        text_area = scrolledtext.ScrolledText(preview_window, wrap=tk.WORD, 
                                              font=("Courier", 9))
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_area.insert(tk.END, f"Commands for OS: {self.os_type}\n")
        text_area.insert(tk.END, "=" * 70 + "\n\n")
        
        for item_id in selected_items:
            commands = self.get_commands_for_item(item_id)
            text_area.insert(tk.END, f"# {item_id.upper()}\n")
            for cmd in commands:
                text_area.insert(tk.END, f"{cmd}\n")
            text_area.insert(tk.END, "\n")
        
        text_area.config(state=tk.DISABLED)
        
        self.log_message(f"Previewed commands for {len(selected_items)} items")
    
    def install_selected(self):
        """Install selected items"""
        if not self.accept_terms.get() and not self.dry_run.get():
            messagebox.showerror("Error", 
                               "You must check 'I understand and accept' before installing")
            return
        
        selected_items = [item_id for item_id, var in self.item_vars.items() if var.get()]
        
        if not selected_items:
            messagebox.showinfo("Info", "No items selected")
            return
        
        mode = "DRY-RUN" if self.dry_run.get() else "INSTALL"
        
        if not self.dry_run.get():
            result = messagebox.askyesno("Confirm", 
                f"This will install {len(selected_items)} items. Continue?")
            if not result:
                return
        
        self.log_message(f"\n{'='*70}")
        self.log_message(f"Starting {mode} for {len(selected_items)} items")
        self.log_message(f"{'='*70}\n")
        
        for item_id in selected_items:
            self.log_message(f"\n--- Processing: {item_id} ---")
            commands = self.get_commands_for_item(item_id)
            
            for cmd in commands:
                if cmd.startswith("open_url:"):
                    url = cmd.replace("open_url:", "")
                    self.log_message(f"Opening URL: {url}")
                    if not self.dry_run.get():
                        webbrowser.open(url)
                elif cmd.startswith("#"):
                    # Skip comment lines
                    self.log_message(f"Note: {cmd}")
                else:
                    self.log_message(f"Command: {cmd}")
                    
                    if not self.dry_run.get():
                        try:
                            # Execute command with shell=True
                            # NOTE: Commands are predefined and not user-controlled
                            # This is safe because all commands come from get_commands_for_item()
                            result = subprocess.run(cmd, shell=True, 
                                                  capture_output=True, text=True, 
                                                  timeout=300)
                            
                            if result.returncode == 0:
                                self.log_message(f"✓ Success")
                                if result.stdout:
                                    self.log_message(f"Output: {result.stdout[:200]}")
                            else:
                                self.log_message(f"✗ Failed (exit code {result.returncode})")
                                if result.stderr:
                                    self.log_message(f"Error: {result.stderr[:200]}")
                        except subprocess.TimeoutExpired:
                            self.log_message(f"✗ Timeout (> 5 minutes)")
                        except Exception as e:
                            self.log_message(f"✗ Exception: {str(e)}")
        
        self.log_message(f"\n{'='*70}")
        self.log_message(f"{mode} completed for {len(selected_items)} items")
        self.log_message(f"{'='*70}\n")
        
        if self.dry_run.get():
            messagebox.showinfo("Dry-Run Complete", 
                              "Dry-run completed. Check the log for details.\n"
                              "Uncheck 'Dry-Run Mode' to actually install.")
        else:
            messagebox.showinfo("Installation Complete", 
                              "Installation process completed. Check the log for details.")
    
    def log_message(self, message):
        """Log a message to the UI and file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # Update UI
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
        # Write to file
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Failed to write to log file: {e}")

def check_elevation():
    """Check if running with admin/root privileges on Windows"""
    if platform.system() == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.geteuid() == 0

def main():
    """Main entry point"""
    # Check for elevation (informational only, not enforced)
    if platform.system() == "Windows" and not check_elevation():
        print("Note: Not running as administrator. Some installations may require elevation.")
    elif platform.system() in ["Linux", "Darwin"] and os.geteuid() != 0:
        print("Note: Not running as root. Some installations may require sudo.")
    
    # Create and run GUI
    root = tk.Tk()
    app = InstallerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
