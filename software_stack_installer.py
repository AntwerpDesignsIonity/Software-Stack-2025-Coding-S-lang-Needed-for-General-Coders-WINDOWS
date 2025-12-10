#!/usr/bin/env python3
"""
Software Stack Installer for Windows
Ionity (Pty) Ltd by Johan Wilhelm van Antwerp
Centirion | +27 646 999 877 | Services@ionity.world

A comprehensive installer for development tools and programming languages.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import subprocess
import os
import urllib.request
import tempfile
import json
from pathlib import Path

class SoftwareStackInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Software Stack Installer 2025 - Ionity (Pty) Ltd")
        self.root.geometry("900x700")
        
        # Installation directory
        self.install_dir = tk.StringVar(value=str(Path.home() / "DevelopmentTools"))
        
        # Software components with download URLs
        self.software_components = {
            "Programming Languages": {
                "Python": {"url": "https://www.python.org/downloads/", "checked": True},
                "Java (JDK)": {"url": "https://adoptium.net/", "checked": False},
                "Rust": {"url": "https://www.rust-lang.org/tools/install", "checked": False},
                "C++ (MinGW)": {"url": "https://github.com/msys2/msys2-installer/releases", "checked": False},
                "C# (.NET SDK)": {"url": "https://dotnet.microsoft.com/download", "checked": False},
                "Go (Golang)": {"url": "https://golang.org/dl/", "checked": False},
                "Kotlin": {"url": "https://github.com/JetBrains/kotlin/releases", "checked": False},
                "Lua": {"url": "https://github.com/rjpcomputing/luaforwindows/releases", "checked": False},
                "Ruby": {"url": "https://rubyinstaller.org/", "checked": False},
                "Swift": {"url": "https://www.swift.org/download/", "checked": False},
                "Scala": {"url": "https://www.scala-lang.org/download/", "checked": False},
                "Dart": {"url": "https://dart.dev/get-dart", "checked": False},
                "Ada (GNAT)": {"url": "https://www.adacore.com/download", "checked": False},
                "Perl": {"url": "https://strawberryperl.com/", "checked": False},
                "Visual Basic": {"url": "https://dotnet.microsoft.com/download/visual-studio-sdks", "checked": False},
                "Objective-C": {"url": "https://github.com/msys2/msys2-installer/releases", "checked": False},
                "MATLAB": {"url": "https://www.mathworks.com/products/matlab.html", "checked": False},
            },
            "Web Technologies": {
                "Node.js & NPM": {"url": "https://nodejs.org/", "checked": False},
                "PHP": {"url": "https://windows.php.net/download/", "checked": False},
                "TypeScript": {"url": "npm", "checked": False},
            },
            "Python Frameworks & Tools": {
                "Flask": {"url": "pip", "checked": False},
                "Python venv": {"url": "builtin", "checked": False},
            },
            "Shell & Terminal": {
                "Git Bash": {"url": "https://git-scm.com/download/win", "checked": False},
                "PowerShell 7": {"url": "https://github.com/PowerShell/PowerShell/releases", "checked": False},
            },
            "Cloud & Firebase": {
                "Firebase CLI": {"url": "npm", "checked": False},
                "Firebase SDK": {"url": "npm", "checked": False},
                "Google Cloud SDK": {"url": "https://cloud.google.com/sdk/docs/install", "checked": False},
            },
            "Mobile Development": {
                "Android SDK": {"url": "https://developer.android.com/studio", "checked": False},
            },
            "Editors & IDEs": {
                "Visual Studio Code": {"url": "https://code.visualstudio.com/download", "checked": False},
            },
        }
        
        # Store checkbox variables
        self.check_vars = {}
        
        self.create_ui()
        
    def create_ui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Software Stack Installer 2025", 
                                font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 5))
        
        # Company info
        company_label = ttk.Label(main_frame, text="Ionity (Pty) Ltd | Services@ionity.world", 
                                  font=("Arial", 9))
        company_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        # Installation directory selection
        dir_frame = ttk.LabelFrame(main_frame, text="Installation Directory", padding="5")
        dir_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Entry(dir_frame, textvariable=self.install_dir, width=60).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(dir_frame, text="Browse...", command=self.browse_directory).grid(row=0, column=1)
        
        # Software selection area with scrollbar
        selection_frame = ttk.LabelFrame(main_frame, text="Select Software to Install", padding="5")
        selection_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Create canvas and scrollbar
        canvas = tk.Canvas(selection_frame, height=300)
        scrollbar = ttk.Scrollbar(selection_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add checkboxes for each category
        row = 0
        for category, items in self.software_components.items():
            # Category header
            category_label = ttk.Label(scrollable_frame, text=category, 
                                      font=("Arial", 11, "bold"))
            category_label.grid(row=row, column=0, sticky=tk.W, pady=(10, 5))
            row += 1
            
            # Items in category
            for item_name, item_data in items.items():
                var = tk.BooleanVar(value=item_data["checked"])
                self.check_vars[item_name] = var
                cb = ttk.Checkbutton(scrollable_frame, text=item_name, variable=var)
                cb.grid(row=row, column=0, sticky=tk.W, padx=(20, 0))
                row += 1
        
        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        ttk.Button(button_frame, text="Select All", command=self.select_all).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Deselect All", command=self.deselect_all).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Install Selected", 
                  command=self.start_installation, style="Accent.TButton").grid(row=0, column=2, padx=5)
        
        # Progress area
        progress_frame = ttk.LabelFrame(main_frame, text="Installation Progress", padding="5")
        progress_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.progress_text = scrolledtext.ScrolledText(progress_frame, height=10, width=80)
        self.progress_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        main_frame.rowconfigure(5, weight=1)
        selection_frame.columnconfigure(0, weight=1)
        selection_frame.rowconfigure(0, weight=1)
        progress_frame.columnconfigure(0, weight=1)
        progress_frame.rowconfigure(0, weight=1)
        
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.install_dir.set(directory)
            
    def select_all(self):
        for var in self.check_vars.values():
            var.set(True)
            
    def deselect_all(self):
        for var in self.check_vars.values():
            var.set(False)
            
    def log_message(self, message):
        self.progress_text.insert(tk.END, message + "\n")
        self.progress_text.see(tk.END)
        self.root.update()
        
    def start_installation(self):
        # Get selected items
        selected_items = [name for name, var in self.check_vars.items() if var.get()]
        
        if not selected_items:
            messagebox.showwarning("No Selection", "Please select at least one software component to install.")
            return
            
        # Confirm installation
        confirm = messagebox.askyesno("Confirm Installation", 
                                     f"Install {len(selected_items)} component(s) to:\n{self.install_dir.get()}\n\nContinue?")
        if not confirm:
            return
            
        # Create installation directory
        install_path = Path(self.install_dir.get())
        try:
            install_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create directory:\n{e}")
            return
            
        # Start installation in a separate thread
        self.progress_text.delete(1.0, tk.END)
        self.progress_bar.start()
        
        thread = threading.Thread(target=self.install_components, args=(selected_items,))
        thread.daemon = True
        thread.start()
        
    def install_components(self, selected_items):
        self.log_message("=" * 80)
        self.log_message("Starting Software Stack Installation")
        self.log_message(f"Installation Directory: {self.install_dir.get()}")
        self.log_message("=" * 80)
        self.log_message("")
        
        install_path = Path(self.install_dir.get())
        
        # Create an installation guide
        guide_lines = []
        guide_lines.append("Software Stack Installation Guide")
        guide_lines.append("=" * 80)
        guide_lines.append(f"Installation Directory: {install_path}")
        guide_lines.append(f"Generated: {Path(__file__).name}")
        guide_lines.append("")
        guide_lines.append("IMPORTANT: This installer provides download links and instructions.")
        guide_lines.append("Many installers require administrative privileges and interactive installation.")
        guide_lines.append("")
        
        for item_name in selected_items:
            # Find the URL for this item
            url = None
            for category, items in self.software_components.items():
                if item_name in items:
                    url = items[item_name]["url"]
                    break
            
            self.log_message(f"Processing: {item_name}")
            guide_lines.append(f"\n{item_name}")
            guide_lines.append("-" * 40)
            
            if url == "pip":
                self.log_message(f"  → Install via pip: pip install {item_name.lower()}")
                guide_lines.append(f"Installation: pip install {item_name.lower()}")
                guide_lines.append(f"Note: Requires Python to be installed first")
                
            elif url == "npm":
                package_name = item_name.lower().replace(" ", "-")
                self.log_message(f"  → Install via npm: npm install -g {package_name}")
                guide_lines.append(f"Installation: npm install -g {package_name}")
                guide_lines.append(f"Note: Requires Node.js and NPM to be installed first")
                
            elif url == "builtin":
                self.log_message(f"  → Built into Python, no installation needed")
                guide_lines.append(f"Built into Python - no separate installation needed")
                
            else:
                self.log_message(f"  → Download from: {url}")
                guide_lines.append(f"Download URL: {url}")
                guide_lines.append(f"Download the installer and run it with administrative privileges")
                
                # Create a URL shortcut file
                try:
                    url_file = install_path / f"{item_name.replace('/', '-').replace(' ', '_')}.url"
                    with open(url_file, 'w') as f:
                        f.write("[InternetShortcut]\n")
                        f.write(f"URL={url}\n")
                    self.log_message(f"  ✓ Created shortcut: {url_file.name}")
                except Exception as e:
                    self.log_message(f"  ✗ Error creating shortcut: {e}")
            
            self.log_message("")
        
        # Save installation guide
        try:
            guide_file = install_path / "INSTALLATION_GUIDE.txt"
            with open(guide_file, 'w') as f:
                f.write("\n".join(guide_lines))
            self.log_message(f"✓ Installation guide saved to: {guide_file}")
        except Exception as e:
            self.log_message(f"✗ Error saving guide: {e}")
        
        self.log_message("")
        self.log_message("=" * 80)
        self.log_message("Installation Process Complete!")
        self.log_message("=" * 80)
        self.log_message("")
        self.log_message("NEXT STEPS:")
        self.log_message("1. Check the INSTALLATION_GUIDE.txt file in your installation directory")
        self.log_message("2. Click on the .url shortcut files to download each installer")
        self.log_message("3. Run each installer with administrative privileges")
        self.log_message("4. Follow the installation wizard for each component")
        self.log_message("")
        self.log_message("NOTE: Some components (like npm and pip packages) require their")
        self.log_message("      parent tools (Node.js and Python) to be installed first.")
        self.log_message("")
        self.log_message(f"Installation directory: {install_path}")
        
        self.progress_bar.stop()
        
        # Show completion dialog
        self.root.after(0, lambda: messagebox.showinfo("Complete", 
            "Installation guide and shortcuts created!\n\n"
            f"Check {install_path} for:\n"
            "- INSTALLATION_GUIDE.txt\n"
            "- Shortcut files (.url) to download each installer"))


def main():
    root = tk.Tk()
    app = SoftwareStackInstaller(root)
    root.mainloop()


if __name__ == "__main__":
    main()
