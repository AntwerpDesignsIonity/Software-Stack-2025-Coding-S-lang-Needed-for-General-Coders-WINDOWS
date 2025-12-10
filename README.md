# Software Stack Installer 2025 for Windows

A comprehensive GUI-based installer for setting up a complete development environment on Windows.

**Ionity (Pty) Ltd**  
By Johan Wilhelm van Antwerp  
Centirion | +27 646 999 877 | Services@ionity.world

## Overview

This installer provides a streamlined way to set up a complete software development stack on Windows, including programming languages, frameworks, SDKs, and development tools.

## Supported Software Components

### Programming Languages
- Python (required - install first)
- Java (JDK)
- Rust
- C++ (MinGW)
- C# (.NET SDK)
- Go (Golang)
- Kotlin
- Lua
- Ruby
- Swift
- Scala
- Dart
- Ada (GNAT)
- Perl
- Visual Basic
- Objective-C
- MATLAB

### Web Technologies
- Node.js & NPM
- PHP
- TypeScript
- HTML5 / CSS / JavaScript (browser-based)

### Python Frameworks & Tools
- Flask
- Python venv (virtual environments)

### Shell & Terminal
- Git Bash
- PowerShell 7

### Cloud & Firebase
- Firebase CLI
- Firebase SDK
- Google Cloud SDK

### Mobile Development
- Android SDK (via Android Studio)

### Editors & IDEs
- Visual Studio Code (optional)

## Installation Instructions

### Step 1: Install Python (Required)

**This installer is a Python script and requires Python to be installed first.**

1. Download Python from: https://www.python.org/downloads/
2. Run the Python installer
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Complete the Python installation

### Step 2: Download the Installer

Download `software_stack_installer.py` from this repository.

### Step 3: Run the Installer

**Option A: Double-click the file**
- Double-click `software_stack_installer.py` (if .py files are associated with Python)

**Option B: Run from Command Prompt**
```cmd
python software_stack_installer.py
```

**Option C: Run from PowerShell**
```powershell
python .\software_stack_installer.py
```

### Step 4: Use the Installer

1. **Select Installation Directory**: Choose where you want to store installer shortcuts and guides (default: `%USERPROFILE%\DevelopmentTools`)

2. **Select Software Components**: Check the boxes for the software you want to install
   - Use "Select All" to choose everything
   - Use "Deselect All" to clear all selections

3. **Click "Install Selected"**: The installer will:
   - Create download shortcut files (.url) for each component
   - Generate a comprehensive installation guide
   - Display progress in real-time

4. **Follow the Installation Guide**:
   - Open the `INSTALLATION_GUIDE.txt` file in your installation directory
   - Click on the .url shortcut files to download each installer
   - Run each installer with administrative privileges
   - Follow the installation wizard for each component

## Features

- ✅ **GUI Interface**: Easy-to-use graphical interface with checkboxes
- ✅ **Customizable Location**: Choose your installation directory
- ✅ **Selective Installation**: Pick only what you need
- ✅ **Real-time Progress**: See installation progress as it happens
- ✅ **Installation Guide**: Detailed guide saved to your installation directory
- ✅ **Direct Download Links**: URL shortcuts for quick access to installers
- ✅ **Dependency Awareness**: Notes about installation order (e.g., Python before pip packages)

## Important Notes

### Installation Order

Some components depend on others:

1. **Install Python first** - Required for pip-based packages (Flask, etc.)
2. **Install Node.js** - Required for npm-based packages (TypeScript, Firebase CLI, etc.)
3. **Install other components** - Can be installed in any order

### Administrative Privileges

Most software installers require administrative privileges to install system-wide. Right-click the installer and select "Run as Administrator" when needed.

### Manual Installation

This tool generates download links and shortcuts because:
- Many installers require interactive installation (license agreements, options, etc.)
- Some installers need administrative privileges
- Users may want to customize installation options
- Different versions may be needed for different systems

## Troubleshooting

### "Python is not recognized..."
- Python is not in your PATH
- Reinstall Python and check "Add Python to PATH"

### "No module named tkinter"
- Tkinter should be included with Python on Windows
- Reinstall Python and ensure "tcl/tk and IDLE" is selected

### Installer won't start
- Make sure Python is installed
- Run from command prompt to see error messages:
  ```cmd
  python software_stack_installer.py
  ```

## System Requirements

- **Operating System**: Windows 10 or later
- **Python**: Python 3.6 or later (with tkinter)
- **Disk Space**: Varies by selected components (20GB+ recommended for full stack)
- **Internet**: Required for downloading installers

## License

See LICENSE file for details.

## Support

For support or questions:
- Email: Services@ionity.world
- Phone: +27 646 999 877

---

© 2025 Ionity (Pty) Ltd. All rights reserved.
