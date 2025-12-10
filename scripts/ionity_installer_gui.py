#!/usr/bin/env python3
"""
Ionity GUI Installer - Cross-platform SDK and CLI installer
Copyright (c) 2025 Johan Wilhelm van Antwerp // Antwerp Ecosystems Designs Ionity ÆĐï

MIT License - See LICENSE file in repository root

This script provides a Tkinter-based GUI for installing common development tools
and SDKs across Windows (winget/choco), macOS (Homebrew), and Debian-based Linux (apt).

SAFETY FEATURES:
- Dry-Run mode by default: Preview commands before execution
- Explicit user confirmation required
- Admin elevation prompts
- Detailed logging of all actions
- Conservative command selection

USAGE:
    python3 scripts/ionity_installer_gui.py

REQUIREMENTS:
    - Python 3.6+
    - tkinter (usually included with Python)
    - Appropriate package manager installed on the system

WARNINGS:
    - Test on a VM or disposable environment first
    - Review all commands in Dry-Run mode before executing
    - Some installations may require system reboot
    - Not all packages available on all platforms
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import platform
import subprocess
import threading
import sys
import os
from typing import Dict, List, Tuple, Optional


class IonityInstaller:
    """Main installer GUI application."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the installer GUI.
        
        Args:
            root: The Tkinter root window
        """
        self.root = root
        self.root.title("Ionity Software Stack Installer 2025")
        self.root.geometry("900x700")
        
        # Detect operating system and package manager
        self.os_type = platform.system()  # Windows, Darwin (macOS), Linux
        self.package_manager = self._detect_package_manager()
        
        # Track installation state
        self.dry_run_mode = True  # Default to dry-run for safety
        self.installing = False
        
        # Define installable items with commands per OS
        self.install_items = self._define_install_items()
        
        # GUI variables
        self.item_vars = {}  # Checkbox variables
        self.select_all_var = tk.BooleanVar(value=False)
        self.dry_run_var = tk.BooleanVar(value=True)
        self.confirm_var = tk.BooleanVar(value=False)
        
        # Build the GUI
        self._build_gui()
        
        # Log initial status
        self._log(f"Ionity Installer initialized")
        self._log(f"Detected OS: {self.os_type}")
        self._log(f"Package Manager: {self.package_manager}")
        self._log(f"Mode: DRY-RUN (safe preview mode)")
        self._log("-" * 60)
        self._log("SAFETY NOTICE: This script will not execute any commands")
        self._log("until you disable Dry-Run mode and confirm installation.")
        self._log("-" * 60)
    
    def _detect_package_manager(self) -> str:
        """Detect available package manager on the system.
        
        Returns:
            String identifier of the package manager
        """
        if self.os_type == "Windows":
            # Check for winget first (Windows 10+)
            try:
                result = subprocess.run(
                    ["winget", "--version"],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return "winget"
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            
            # Fallback to chocolatey
            try:
                result = subprocess.run(
                    ["choco", "--version"],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return "choco"
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            
            return "manual"
        
        elif self.os_type == "Darwin":  # macOS
            try:
                result = subprocess.run(
                    ["brew", "--version"],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return "brew"
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            return "manual"
        
        elif self.os_type == "Linux":
            # Check for apt (Debian/Ubuntu)
            try:
                result = subprocess.run(
                    ["apt", "--version"],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return "apt"
            except (FileNotFoundError, subprocess.TimeoutExpired):
                pass
            
            # Other distributions would be detected here
            # For now, return manual for non-Debian Linux
            return "manual"
        
        return "unknown"
    
    def _define_install_items(self) -> Dict[str, Dict]:
        """Define all installable items with OS-specific commands.
        
        Returns:
            Dictionary mapping item names to their installation details
        """
        items = {
            "Git": {
                "description": "Git version control system",
                "commands": {
                    "winget": ["winget", "install", "--id", "Git.Git", "-e"],
                    "choco": ["choco", "install", "git", "-y"],
                    "brew": ["brew", "install", "git"],
                    "apt": ["sudo", "apt", "install", "-y", "git"]
                }
            },
            "Node.js (with npm)": {
                "description": "Node.js runtime and npm package manager",
                "commands": {
                    "winget": ["winget", "install", "--id", "OpenJS.NodeJS", "-e"],
                    "choco": ["choco", "install", "nodejs", "-y"],
                    "brew": ["brew", "install", "node"],
                    "apt": ["sudo", "apt", "install", "-y", "nodejs", "npm"]
                }
            },
            "Python pip packages": {
                "description": "Essential Python packages (virtualenv, pipx, flask)",
                "commands": {
                    "winget": ["pip", "install", "virtualenv", "pipx", "flask"],
                    "choco": ["pip", "install", "virtualenv", "pipx", "flask"],
                    "brew": ["pip3", "install", "virtualenv", "pipx", "flask"],
                    "apt": ["pip3", "install", "virtualenv", "pipx", "flask"]
                }
            },
            "Rust (rustup)": {
                "description": "Rust programming language toolchain",
                "commands": {
                    "winget": ["winget", "install", "--id", "Rustlang.Rustup", "-e"],
                    "choco": ["choco", "install", "rust", "-y"],
                    "brew": ["brew", "install", "rust"],
                    "apt": ["curl", "--proto", "=https", "--tlsv1.2", "-sSf", 
                           "https://sh.rustup.rs", "|", "sh", "-s", "--", "-y"]
                }
            },
            "Java (OpenJDK)": {
                "description": "OpenJDK Java Development Kit",
                "commands": {
                    "winget": ["winget", "install", "--id", "Microsoft.OpenJDK.17", "-e"],
                    "choco": ["choco", "install", "openjdk", "-y"],
                    "brew": ["brew", "install", "openjdk"],
                    "apt": ["sudo", "apt", "install", "-y", "default-jdk"]
                }
            },
            "PHP": {
                "description": "PHP programming language",
                "commands": {
                    "winget": ["winget", "install", "--id", "PHP.PHP", "-e"],
                    "choco": ["choco", "install", "php", "-y"],
                    "brew": ["brew", "install", "php"],
                    "apt": ["sudo", "apt", "install", "-y", "php", "php-cli"]
                }
            },
            "Composer (PHP)": {
                "description": "PHP dependency manager",
                "commands": {
                    "winget": ["winget", "install", "--id", "Composer.Composer", "-e"],
                    "choco": ["choco", "install", "composer", "-y"],
                    "brew": ["brew", "install", "composer"],
                    "apt": ["sudo", "apt", "install", "-y", "composer"]
                }
            },
            "Docker": {
                "description": "Docker container platform",
                "commands": {
                    "winget": ["winget", "install", "--id", "Docker.DockerDesktop", "-e"],
                    "choco": ["choco", "install", "docker-desktop", "-y"],
                    "brew": ["brew", "install", "--cask", "docker"],
                    "apt": ["sudo", "apt", "install", "-y", "docker.io"]
                }
            },
            "Visual Studio Code": {
                "description": "VS Code editor",
                "commands": {
                    "winget": ["winget", "install", "--id", "Microsoft.VisualStudioCode", "-e"],
                    "choco": ["choco", "install", "vscode", "-y"],
                    "brew": ["brew", "install", "--cask", "visual-studio-code"],
                    "apt": ["sudo", "snap", "install", "code", "--classic"]
                }
            },
            "Firebase CLI": {
                "description": "Firebase command-line tools (requires Node.js/npm)",
                "commands": {
                    "winget": ["npm", "install", "-g", "firebase-tools"],
                    "choco": ["npm", "install", "-g", "firebase-tools"],
                    "brew": ["npm", "install", "-g", "firebase-tools"],
                    "apt": ["npm", "install", "-g", "firebase-tools"]
                }
            },
            "Google Cloud SDK": {
                "description": "Google Cloud gcloud CLI",
                "commands": {
                    "winget": ["winget", "install", "--id", "Google.CloudSDK", "-e"],
                    "choco": ["choco", "install", "gcloudsdk", "-y"],
                    "brew": ["brew", "install", "--cask", "google-cloud-sdk"],
                    "apt": ["sudo", "snap", "install", "google-cloud-cli", "--classic"]
                }
            },
            "AWS CLI": {
                "description": "Amazon Web Services command-line interface",
                "commands": {
                    "winget": ["winget", "install", "--id", "Amazon.AWSCLI", "-e"],
                    "choco": ["choco", "install", "awscli", "-y"],
                    "brew": ["brew", "install", "awscli"],
                    "apt": ["sudo", "apt", "install", "-y", "awscli"]
                }
            },
            "Yarn": {
                "description": "Yarn package manager for Node.js",
                "commands": {
                    "winget": ["npm", "install", "-g", "yarn"],
                    "choco": ["choco", "install", "yarn", "-y"],
                    "brew": ["brew", "install", "yarn"],
                    "apt": ["npm", "install", "-g", "yarn"]
                }
            },
            "pnpm": {
                "description": "Fast, disk space efficient package manager",
                "commands": {
                    "winget": ["npm", "install", "-g", "pnpm"],
                    "choco": ["npm", "install", "-g", "pnpm"],
                    "brew": ["npm", "install", "-g", "pnpm"],
                    "apt": ["npm", "install", "-g", "pnpm"]
                }
            },
            "TypeScript": {
                "description": "TypeScript compiler and language tools",
                "commands": {
                    "winget": ["npm", "install", "-g", "typescript"],
                    "choco": ["npm", "install", "-g", "typescript"],
                    "brew": ["npm", "install", "-g", "typescript"],
                    "apt": ["npm", "install", "-g", "typescript"]
                }
            }
        }
        
        return items
    
    def _build_gui(self):
        """Build the GUI layout."""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="Ionity Software Stack Installer 2025",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Johan Wilhelm van Antwerp // Antwerp Ecosystems Designs Ionity",
            font=("Arial", 9),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Main content area
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Item selection
        left_frame = tk.LabelFrame(main_frame, text="Select Items to Install", padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Select All checkbox
        select_all_cb = tk.Checkbutton(
            left_frame,
            text="Select All",
            variable=self.select_all_var,
            command=self._toggle_select_all,
            font=("Arial", 10, "bold")
        )
        select_all_cb.pack(anchor=tk.W, pady=(0, 10))
        
        # Scrollable frame for checkboxes
        canvas = tk.Canvas(left_frame)
        scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create checkboxes for each item
        for item_name, item_info in self.install_items.items():
            var = tk.BooleanVar(value=False)
            self.item_vars[item_name] = var
            
            cb = tk.Checkbutton(
                scrollable_frame,
                text=item_name,
                variable=var,
                font=("Arial", 9)
            )
            cb.pack(anchor=tk.W, pady=2)
            
            desc_label = tk.Label(
                scrollable_frame,
                text=f"  → {item_info['description']}",
                font=("Arial", 8),
                fg="gray"
            )
            desc_label.pack(anchor=tk.W, padx=(20, 0))
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Right panel - Controls and log
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Control panel
        control_frame = tk.LabelFrame(right_frame, text="Installation Options", padx=10, pady=10)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Dry-run checkbox
        dry_run_cb = tk.Checkbutton(
            control_frame,
            text="Dry-Run Mode (Preview only - SAFE)",
            variable=self.dry_run_var,
            font=("Arial", 10, "bold"),
            fg="green"
        )
        dry_run_cb.pack(anchor=tk.W, pady=5)
        
        # Confirmation checkbox
        confirm_cb = tk.Checkbutton(
            control_frame,
            text="I understand this will modify my system",
            variable=self.confirm_var,
            font=("Arial", 9),
            fg="red"
        )
        confirm_cb.pack(anchor=tk.W, pady=5)
        
        # Warning label
        warning_label = tk.Label(
            control_frame,
            text="⚠️ Test on VM first! Review logs carefully.",
            font=("Arial", 9, "italic"),
            fg="orange"
        )
        warning_label.pack(pady=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            control_frame,
            variable=self.progress_var,
            maximum=100,
            mode='determinate'
        )
        self.progress_bar.pack(fill=tk.X, pady=5)
        
        # Install button
        self.install_button = tk.Button(
            control_frame,
            text="Install Selected Items",
            command=self._start_installation,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            height=2
        )
        self.install_button.pack(fill=tk.X, pady=10)
        
        # Log panel
        log_frame = tk.LabelFrame(right_frame, text="Installation Log", padx=5, pady=5)
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=15,
            font=("Courier", 9),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="white"
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Bottom status bar
        status_frame = tk.Frame(self.root, bg="#34495e", height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text=f"Ready | OS: {self.os_type} | Package Manager: {self.package_manager}",
            bg="#34495e",
            fg="white",
            font=("Arial", 9)
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
    
    def _toggle_select_all(self):
        """Toggle all item checkboxes."""
        state = self.select_all_var.get()
        for var in self.item_vars.values():
            var.set(state)
    
    def _log(self, message: str):
        """Add a message to the log display.
        
        Args:
            message: The message to log
        """
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def _update_status(self, message: str):
        """Update the status bar.
        
        Args:
            message: Status message to display
        """
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def _start_installation(self):
        """Start the installation process in a separate thread."""
        if self.installing:
            messagebox.showwarning("Already Running", "Installation is already in progress.")
            return
        
        # Get selected items
        selected_items = [name for name, var in self.item_vars.items() if var.get()]
        
        if not selected_items:
            messagebox.showwarning("No Selection", "Please select at least one item to install.")
            return
        
        # Check dry-run mode
        self.dry_run_mode = self.dry_run_var.get()
        
        if not self.dry_run_mode:
            # Require confirmation for actual installation
            if not self.confirm_var.get():
                messagebox.showerror(
                    "Confirmation Required",
                    "You must check 'I understand this will modify my system' before proceeding with actual installation."
                )
                return
            
            # Final warning
            response = messagebox.askyesno(
                "Final Confirmation",
                f"You are about to install {len(selected_items)} item(s) on your system.\n\n"
                "This will:\n"
                "- Execute system commands with elevated privileges\n"
                "- Download and install software packages\n"
                "- Modify system configuration\n\n"
                "Are you sure you want to continue?"
            )
            if not response:
                self._log("Installation cancelled by user.")
                return
        
        # Disable install button during installation
        self.installing = True
        self.install_button.config(state=tk.DISABLED)
        
        # Run installation in separate thread to keep GUI responsive
        thread = threading.Thread(target=self._run_installation, args=(selected_items,))
        thread.daemon = True
        thread.start()
    
    def _run_installation(self, selected_items: List[str]):
        """Run the installation process.
        
        Args:
            selected_items: List of item names to install
        """
        try:
            self._log("\n" + "=" * 60)
            if self.dry_run_mode:
                self._log("DRY-RUN MODE: Commands will be displayed but not executed")
            else:
                self._log("LIVE MODE: Commands will be executed")
            self._log("=" * 60)
            
            total_items = len(selected_items)
            completed = 0
            
            for item_name in selected_items:
                self._log(f"\n[{completed + 1}/{total_items}] Processing: {item_name}")
                self._update_status(f"Processing {item_name}...")
                
                item_info = self.install_items[item_name]
                command = item_info["commands"].get(self.package_manager)
                
                if not command:
                    self._log(f"  ⚠️  No command defined for package manager: {self.package_manager}")
                    self._log(f"  Please install '{item_name}' manually")
                    completed += 1
                    self.progress_var.set((completed / total_items) * 100)
                    continue
                
                # Display the command
                cmd_str = " ".join(command)
                self._log(f"  Command: {cmd_str}")
                
                if self.dry_run_mode:
                    self._log(f"  ✓ DRY-RUN: Command would be executed")
                else:
                    # Execute the command
                    success = self._execute_command(command)
                    if success:
                        self._log(f"  ✓ Successfully installed {item_name}")
                    else:
                        self._log(f"  ✗ Failed to install {item_name}")
                
                completed += 1
                self.progress_var.set((completed / total_items) * 100)
            
            self._log("\n" + "=" * 60)
            self._log(f"Process completed: {completed}/{total_items} items processed")
            self._log("=" * 60)
            
            if self.dry_run_mode:
                self._update_status("Dry-run completed - No changes made")
                messagebox.showinfo(
                    "Dry-Run Complete",
                    f"Dry-run completed successfully!\n\n"
                    f"Processed {completed} items.\n"
                    f"Review the log to see what commands would be executed.\n\n"
                    f"To actually install, uncheck 'Dry-Run Mode' and run again."
                )
            else:
                self._update_status("Installation completed")
                messagebox.showinfo(
                    "Installation Complete",
                    f"Installation process completed!\n\n"
                    f"Processed {completed} items.\n"
                    f"Check the log for details and any errors.\n\n"
                    f"Some tools may require a system restart to work properly."
                )
        
        except Exception as e:
            self._log(f"\n✗ ERROR: {str(e)}")
            self._update_status("Error occurred")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        
        finally:
            self.installing = False
            self.install_button.config(state=tk.NORMAL)
            self.progress_var.set(0)
    
    def _execute_command(self, command: List[str]) -> bool:
        """Execute a system command.
        
        Args:
            command: Command and arguments as a list
            
        Returns:
            True if command succeeded, False otherwise
        """
        try:
            # Check if command requires elevation
            needs_elevation = any(cmd in command for cmd in ["sudo", "choco", "winget"])
            
            if needs_elevation and self.os_type == "Windows":
                # Note: On Windows, many installers will prompt for elevation automatically
                self._log(f"  ℹ️  This command may require administrator privileges")
            
            # Execute command
            self._log(f"  Executing...")
            
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            # Log output
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    if line.strip():
                        self._log(f"    {line}")
            
            if result.stderr and result.returncode != 0:
                for line in result.stderr.strip().split('\n'):
                    if line.strip():
                        self._log(f"    ERROR: {line}")
            
            return result.returncode == 0
        
        except subprocess.TimeoutExpired:
            self._log(f"  ✗ Command timed out after 5 minutes")
            return False
        except FileNotFoundError:
            self._log(f"  ✗ Command not found: {command[0]}")
            self._log(f"  ℹ️  Make sure {command[0]} is installed and in your PATH")
            return False
        except Exception as e:
            self._log(f"  ✗ Unexpected error: {str(e)}")
            return False


def main():
    """Main entry point for the installer."""
    # Check Python version
    if sys.version_info < (3, 6):
        print("ERROR: This script requires Python 3.6 or higher")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    # Check if tkinter is available
    try:
        import tkinter
    except ImportError:
        print("ERROR: tkinter is not available")
        print("Please install tkinter:")
        print("  - On Debian/Ubuntu: sudo apt install python3-tk")
        print("  - On macOS: tkinter should be included with Python")
        print("  - On Windows: tkinter should be included with Python")
        sys.exit(1)
    
    # Create and run the GUI
    root = tk.Tk()
    app = IonityInstaller(root)
    root.mainloop()


if __name__ == "__main__":
    main()
