# Ionity Installer Scripts

This directory contains the automated installer scripts for the Ionity Software Stack 2025.

## Main Script: ionity_installer_gui.py

A comprehensive, Tkinter-based GUI installer that helps users install common developer SDKs, CLIs, and runtimes across Windows, macOS, and Debian-based Linux.

### Features

- **Safe by Default**: Runs in dry-run mode by default (preview only)
- **Multi-Platform**: Supports Windows (winget), macOS (Homebrew), and Linux (apt)
- **Comprehensive**: Includes 30+ languages and development tools
- **User-Friendly**: Tabbed interface with categorized selections
- **Auditable**: Preview all commands before execution
- **Logging**: All actions logged to `installer_log.txt`

### Supported Languages & Tools

#### Languages - Core
- Python, JavaScript/Node.js, TypeScript
- Java, C#/.NET, C++
- Rust, Go, PHP
- Ruby

#### Languages - Extended
- Swift, Kotlin, Scala, Perl
- R, Dart, Ada
- Objective-C, Delphi/Object Pascal
- Assembly (NASM)

#### Specialized Tools
- MATLAB (vendor link)
- Visual Basic (Visual Studio link)
- SQL Tools (SQLite, PostgreSQL)

#### Development Tools
- Git, Docker, Visual Studio Code
- Firebase CLI, Google Cloud SDK, AWS CLI
- Yarn, pnpm

### Usage

#### Prerequisites
- Python 3.8 or higher
- Tkinter (usually included with Python)

#### Running the Installer

```bash
python3 scripts/ionity_installer_gui.py
```

Or on Windows:
```cmd
python scripts\ionity_installer_gui.py
```

#### Step-by-Step

1. **Launch** - Run the script to open the GUI
2. **Review** - Check the detected operating system
3. **Select** - Choose which tools to install (or "Select All")
4. **Preview** - Click "Preview Commands" to see exactly what will be executed
5. **Dry-Run** - Test with dry-run mode enabled (default)
6. **Accept** - Check "I understand and accept" when ready to install
7. **Install** - Uncheck "Dry-Run Mode" and click "Install Selected"

### Safety Features

- **Dry-Run Default**: Commands are only displayed, not executed
- **Explicit Confirmation**: Must accept terms before installation
- **Command Preview**: See exact commands before running
- **Vendor Links**: Proprietary software (MATLAB, Visual Studio) opens vendor pages instead of attempting downloads
- **Comprehensive Logging**: All actions timestamped and logged

### OS-Specific Notes

#### Windows
- Uses `winget` as the primary package manager
- Some installations may require administrator privileges
- Run from an elevated PowerShell/CMD if needed

#### macOS
- Uses Homebrew (`brew`) as the package manager
- Install Homebrew first: https://brew.sh/
- Some tools require Xcode Command Line Tools

#### Linux (Debian/Ubuntu)
- Uses `apt` package manager
- Most commands require `sudo` privileges
- For other distributions, commands may need adjustment

### Logging

All installer actions are logged to:
```
installer_log.txt
```

Located in the repository root directory. Each log entry includes:
- Timestamp
- Action type (command, URL, success/failure)
- Output/error messages

### Customization

To add or modify installation commands, edit the `get_commands_for_item()` method in `ionity_installer_gui.py`. The method returns OS-specific commands for each item.

### Troubleshooting

**Issue**: Script won't start
- **Solution**: Ensure Python 3.8+ is installed and Tkinter is available

**Issue**: "Module not found" errors
- **Solution**: Install required Python packages (though this script uses only stdlib)

**Issue**: Installation fails
- **Solution**: Check the log file for detailed error messages. Some tools may require manual intervention or different package names on your system.

**Issue**: Permission denied
- **Solution**: Run as administrator (Windows) or with sudo (Linux/macOS)

### License

Author: Johan Wilhelm van Antwerp / Ionity
License: Creative Commons BY-NC-SA 4.0

### Contact

- Email: Services@ionity.world
- Email (Alt): johan van Antwerp@gmail.com
- Phone: +27 646999877
- LinkedIn: https://www.linkedin.com/in/johanvanantwerp/

### Attribution

Ruled by POLICY 986 AED | Ionity 2025 | All Rights Reserved
