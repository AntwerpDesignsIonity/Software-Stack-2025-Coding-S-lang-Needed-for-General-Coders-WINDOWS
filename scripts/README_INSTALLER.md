# Ionity GUI Installer

A safe, cross-platform GUI installer for common development tools and SDKs.

**Author:** Johan Wilhelm van Antwerp // Antwerp Ecosystems Designs Ionity ÆĐï  
**License:** MIT (see LICENSE file)

## Overview

The Ionity GUI Installer (`ionity_installer_gui.py`) is a Tkinter-based graphical installer that helps you install common SDKs, CLIs, runtimes, and developer tools across Windows, macOS, and Linux platforms. It emphasizes safety by defaulting to a dry-run mode and requiring explicit user confirmation before making any system changes.

## Features

- ✅ **Cross-platform support**: Windows (winget/choco), macOS (Homebrew), Debian-based Linux (apt)
- ✅ **Dry-Run mode**: Preview all commands before execution (default mode)
- ✅ **Safety first**: Explicit confirmation required for system modifications
- ✅ **Detailed logging**: See exactly what commands are being executed
- ✅ **Progress tracking**: Visual progress bar and status updates
- ✅ **Comprehensive coverage**: 15+ common development tools including:
  - Git, Node.js, Python packages, Rust, Java, PHP, Docker
  - VS Code, Firebase CLI, Google Cloud SDK, AWS CLI
  - Package managers: npm, yarn, pnpm, composer
  - And more...

## System Requirements

### Minimum Requirements
- **Python:** 3.8 or higher
- **GUI Framework:** tkinter (usually included with Python)
- **Operating System:** 
  - Windows 10 or higher (with winget or chocolatey)
  - macOS 10.14 or higher (with Homebrew)
  - Debian/Ubuntu Linux (with apt)

### Package Managers
The script automatically detects your package manager:
- **Windows:** winget (preferred) or chocolatey
- **macOS:** Homebrew
- **Linux:** apt (Debian/Ubuntu-based)

If no package manager is detected, the script will show you the commands to run manually.

## Installation

1. Ensure Python 3.8+ is installed:
   ```bash
   python3 --version
   ```

2. Verify tkinter is available (usually pre-installed):
   ```bash
   python3 -c "import tkinter"
   ```

3. If tkinter is missing:
   - **Debian/Ubuntu:** `sudo apt install python3-tk`
   - **macOS/Windows:** Reinstall Python from official sources

## Usage

### Basic Usage

Run the installer script:

```bash
python3 scripts/ionity_installer_gui.py
```

Or on Windows:

```bash
python scripts\ionity_installer_gui.py
```

### Step-by-Step Workflow

1. **Launch the installer**
   - The GUI will open and detect your operating system
   - Default mode is Dry-Run (safe preview mode)

2. **Select items to install**
   - Check individual items or use "Select All"
   - Review the description for each item

3. **Preview commands (Dry-Run)**
   - Keep "Dry-Run Mode" checked (default)
   - Click "Install Selected Items"
   - Review the log to see what commands would be executed
   - **No actual changes are made in Dry-Run mode**

4. **Execute installation (optional)**
   - Uncheck "Dry-Run Mode"
   - Check "I understand this will modify my system"
   - Click "Install Selected Items"
   - Confirm the final warning dialog
   - Monitor progress in the log window

### Command-Line Options

The script currently runs entirely through the GUI. No command-line arguments are required.

## Safety Warnings & Limitations

### ⚠️ Important Safety Notes

1. **Test on a VM first**: Always test the installer on a disposable virtual machine or test environment before running on your production system

2. **Review in Dry-Run mode**: Always run in Dry-Run mode first to see what commands will be executed

3. **Administrator privileges**: Some installations require administrator/root privileges:
   - Windows: May prompt for UAC elevation
   - macOS/Linux: May require `sudo` password

4. **Internet connection required**: All packages are downloaded from official sources during installation

5. **Existing installations**: The script does not check if software is already installed - it will attempt to install/upgrade

6. **System modifications**: Installation will modify system files, PATH, and may install dependencies

### Known Limitations

1. **Platform coverage**:
   - Fully supported: Windows (winget/choco), macOS (Homebrew), Debian/Ubuntu (apt)
   - Limited support: Other Linux distributions (shows manual commands)
   - Not supported: BSD, Solaris, other Unix variants

2. **Package availability**: Not all packages are available on all platforms through package managers

3. **GUI-only applications**: Some applications like Figma don't have CLI installers - the script will provide download links instead

4. **Version control**: The script installs the latest available version from the package manager - specific versions must be installed manually

5. **Offline installation**: Not supported - requires internet connection to download packages

6. **Rollback**: No automatic rollback functionality - use your package manager to uninstall if needed

## Troubleshooting

### "tkinter is not available"
Install tkinter for your system:
- Debian/Ubuntu: `sudo apt install python3-tk`
- macOS: Included with Python from python.org
- Windows: Included with Python from python.org

### "No package manager detected"
Install a package manager:
- **Windows:** Install [winget](https://github.com/microsoft/winget-cli) (Windows 11+) or [Chocolatey](https://chocolatey.org/)
- **macOS:** Install [Homebrew](https://brew.sh/)
- **Linux:** For non-Debian distributions, adapt the commands manually

### Installation fails
1. Check the log output for specific error messages
2. Ensure you have an internet connection
3. Verify you have sufficient permissions (admin/sudo)
4. Try running the command manually from the log to see detailed errors
5. Check if the package name is correct for your OS

### Command timeouts
Some large packages (like Docker, VS Code) may take time to download and install. The script has a 5-minute timeout per command. If needed, install these manually.

## Extending the Installer

To add new packages, edit `ionity_installer_gui.py` and add entries to the `_define_install_items()` method:

```python
"New Package": {
    "description": "Description of the package",
    "commands": {
        "winget": ["winget", "install", "--id", "Publisher.Package", "-e"],
        "choco": ["choco", "install", "package-name", "-y"],
        "brew": ["brew", "install", "package-name"],
        "apt": ["sudo", "apt", "install", "-y", "package-name"]
    }
}
```

## Security Considerations

1. **Command execution**: The script executes system commands - review the code before running
2. **Package sources**: All packages come from official package manager repositories
3. **No binary downloads**: The script does not download or embed binaries directly
4. **Open source**: Inspect the script source code to verify behavior
5. **Logging**: All commands are logged before execution for transparency

## Support & Contribution

This script is provided as-is under the MIT License. For issues or improvements:

1. Test thoroughly in a VM environment
2. Document any platform-specific issues
3. Submit changes with clear descriptions
4. Maintain backward compatibility where possible

## Additional Resources

- **Python Installation:** https://www.python.org/downloads/
- **Homebrew (macOS):** https://brew.sh/
- **Chocolatey (Windows):** https://chocolatey.org/
- **winget (Windows):** https://github.com/microsoft/winget-cli

## License

MIT License - Copyright (c) 2025 Johan Wilhelm van Antwerp // Antwerp Ecosystems Designs Ionity ÆĐï

See LICENSE file in repository root for full license text.

---

**Last Updated:** December 2025  
**Version:** 1.0.0
