# Ionity Comprehensive Language Installer - User Guide

## Overview

The Ionity Comprehensive Language Installer (`ionity_installer_gui.py`) is a conservative, auditable Tkinter-based GUI tool for installing programming languages, runtimes, SDKs, and CLI tools across Windows, macOS, and Linux platforms.

**Author:** Johan Wilhelm van Antwerp  
**Organization:** Antwerp Designs / Ionity  
**License:** Creative Commons BY-NC-SA 4.0  
**Policy:** POLICY 986 AED

## ⚠️ SAFETY FIRST

**CRITICAL SAFETY NOTES:**

1. **Test in a VM first** - Always test the installer in a virtual machine before using it on your production system
2. **Audit commands** - Review all commands in Preview mode before executing
3. **Dry-Run default** - The installer defaults to Dry-Run mode (shows commands without executing)
4. **Explicit confirmation required** - You must check "I understand and accept the risks" to execute commands
5. **Internet required** - The installer requires an internet connection for downloads and package manager operations
6. **Elevated privileges** - Some installations require administrator/sudo privileges
7. **Time requirements** - Some installations may take several minutes to complete

## Requirements

- **Python 3.8 or higher** (for security and EOL reasons)
- **tkinter** (usually included with Python)
- **Internet connection** for downloads
- **Package managers:**
  - Windows: winget (included with Windows 11 and modern Windows 10)
  - macOS: Homebrew (install from https://brew.sh/)
  - Linux: apt (Debian/Ubuntu) or appropriate package manager for your distro

## Installation

No installation required! Just run the script:

```bash
# On Windows
python scripts/ionity_installer_gui.py

# On macOS/Linux
python3 scripts/ionity_installer_gui.py
```

## Usage

### Basic Workflow

1. **Launch the installer** - Run the script using Python 3.8+
2. **Review detected OS** - The installer will detect your operating system
3. **Select languages/tools** - Check the boxes for items you want to install
4. **Preview commands** - Click "Preview Commands" to see what will be executed
5. **Review and audit** - Carefully review all commands before proceeding
6. **Enable execution** - Check "I understand and accept the risks" to enable execution
7. **Install** - Click "Install Selected" to execute the commands
8. **Monitor progress** - Watch the log for progress and any errors

### Features

#### Selection Controls

- **Select All** - Check all language/tool checkboxes
- **Deselect All** - Uncheck all checkboxes
- **Individual selection** - Check/uncheck items as needed

#### Action Buttons

- **Preview Commands** - Shows all commands that would be executed (Dry-Run)
- **Open Vendor Pages** - Opens vendor download pages in your browser for items that require manual installation
- **Install Selected** - Executes installation commands (requires confirmation checkbox)

#### Modes

- **Dry-Run Mode (Default)** - Shows commands without executing them
- **Execution Mode** - Executes commands after explicit user confirmation

#### Logging

- All actions are logged with timestamps
- Commands shown before execution
- stdout/stderr captured and displayed
- Log can be cleared with "Clear Log" button

## Supported Languages and Tools

The installer includes support for **24 programming languages and tools**:

### Package Manager Installs

These items are installed via platform-specific package managers (winget/brew/apt):

1. **JavaScript** - Node.js runtime and npm
2. **Java** - JDK (OpenJDK or Oracle)
3. **PHP** - PHP runtime and CLI
4. **Python** - Python 3 interpreter and pip
5. **Rust** - Rust toolchain (rustc, cargo)
6. **C++** - Compilers (gcc, g++, clang, MSVC Build Tools)
7. **Ruby** - Ruby interpreter and gems
8. **R** - R statistical computing environment
9. **SQL (clients & tools)** - SQLite, PostgreSQL client
10. **Go** - Go programming language
11. **Perl** - Perl interpreter
12. **Assembly (tools)** - NASM assembler
13. **Ada** - GNAT compiler (via GCC)

### npm-based Tools

These items require Node.js and are installed via npm:

14. **TypeScript** - TypeScript compiler (via npm)
15. **CSS (tooling)** - PostCSS and Autoprefixer (via npm)

### Vendor/Manual Installs

These items open vendor download pages for manual installation:

16. **MATLAB** - Commercial mathematical computing environment
17. **Visual Basic** - Part of Visual Studio (Windows only)
18. **Delphi/Object Pascal** - Commercial IDE and compiler
19. **Swift** - Swift compiler (macOS: included with Xcode)
20. **C#** - .NET SDK
21. **Kotlin** - Kotlin compiler
22. **Dart** - Dart SDK
23. **Scala** - Scala language
24. **Objective-C** - Part of Xcode (macOS only)

### Platform-Specific Notes

#### Windows (winget)

- Uses Windows Package Manager (winget)
- Requires Windows 11 or Windows 10 with App Installer
- Some installs may require administrator privileges
- Visual Basic and C# best installed via Visual Studio

#### macOS (brew)

- Uses Homebrew package manager
- Install Homebrew first: https://brew.sh/
- Swift and Objective-C require Xcode or Command Line Tools
- Run: `xcode-select --install` for Command Line Tools

#### Linux (apt)

- Commands shown for Debian/Ubuntu (apt/apt-get)
- For other distros (Fedora, Arch, etc.), adapt commands:
  - Fedora/RHEL: Use `dnf` instead of `apt`
  - Arch: Use `pacman` instead of `apt`
- Some installs require sudo privileges

## Command Structure

The installer uses these command types:

1. **Package manager commands** - Direct installation via winget/brew/apt
   ```
   winget install Python.Python.3.12
   brew install python3
   sudo apt-get install python3
   ```

2. **open_url: directives** - Opens vendor pages in browser
   ```
   open_url:https://www.mathworks.com/products/matlab.html
   ```

3. **Comments/recommendations** - Informational notes starting with #
   ```
   # Install via npm: npm install -g typescript
   ```

## Customization for Maintainers

### Adding New Languages/Tools

To add a new language or tool:

1. Add to the `self.items` list in `InstallerGUI.__init__()`:
   ```python
   ("Display Name", "key_name"),
   ```

2. Add commands in `get_commands_for_item()`:
   ```python
   "key_name": {
       "windows": ["winget install Package.Name"],
       "macos": ["brew install package"],
       "linux": ["sudo apt-get install package"],
   },
   ```

### Updating Package Names

Package names and versions are defined in `get_commands_for_item()`. Update them as needed:

```python
"python": {
    "windows": ["winget install Python.Python.3.12"],  # Update version here
    "macos": ["brew install python3"],
    "linux": ["sudo apt-get install -y python3 python3-pip"],
},
```

### Adding Distro-Specific Logic

For Linux distro-specific commands, add detection logic in `get_commands_for_item()`:

```python
# Example: detect Fedora vs Ubuntu
if self.os_type == "linux":
    try:
        with open("/etc/os-release") as f:
            if "fedora" in f.read().lower():
                return ["sudo dnf install package"]
    except:
        pass
    return ["sudo apt-get install package"]
```

## Troubleshooting

### Common Issues

**Issue:** "tkinter is not available"
- **Solution:** Install tkinter for your Python version
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-tk
  
  # Fedora
  sudo dnf install python3-tkinter
  
  # macOS/Windows: usually included
  ```

**Issue:** "Command not found" errors
- **Solution:** 
  - Windows: Install winget (comes with Windows 11)
  - macOS: Install Homebrew from https://brew.sh/
  - Linux: Ensure apt/dnf is available

**Issue:** Permission denied errors
- **Solution:** 
  - Windows: Run as Administrator
  - macOS/Linux: Commands that need sudo are prefixed automatically

**Issue:** Installation hangs or times out
- **Solution:** 
  - Check internet connection
  - Some packages are large and take time
  - Timeout is set to 5 minutes per command

### Getting Help

If you encounter issues:

1. Run in Preview mode first to see the exact commands
2. Test commands manually in your terminal
3. Check package manager documentation
4. Review the log output for error messages

## Security Considerations

### Before Running

- ✅ Review the source code in a text editor
- ✅ Audit all commands using Preview mode
- ✅ Test in a virtual machine first
- ✅ Verify checksums of downloaded files
- ✅ Keep your system and package managers up to date

### During Installation

- ✅ Monitor the log output
- ✅ Watch for unexpected errors or warnings
- ✅ Cancel if anything looks suspicious
- ✅ Don't ignore security warnings from your OS

### After Installation

- ✅ Verify installed versions: `python --version`, `node --version`, etc.
- ✅ Check for unexpected changes to your system
- ✅ Review installed applications
- ✅ Update installed software regularly

## Examples

### Example 1: Install Python, JavaScript, and Go

1. Launch the installer
2. Check boxes: Python, JavaScript, Go
3. Click "Preview Commands" to review
4. Check "I understand and accept the risks"
5. Click "Install Selected"
6. Monitor log output

### Example 2: Get MATLAB Download Page

1. Launch the installer
2. Check box: MATLAB
3. Click "Open Vendor Pages"
4. Browser opens to MATLAB download page

### Example 3: Preview All Commands

1. Launch the installer
2. Click "Select All"
3. Click "Preview Commands"
4. Review all commands in the log
5. Decide which to install

## License and Attribution

**Creative Commons BY-NC-SA 4.0 Applies**  
**Ruled by POLICY 986 AED**

**Author:** Johan Wilhelm van Antwerp  
**Organization:** Antwerp Designs / Ionity  
**Contact:** Services@ionity.world | johan van Antwerp@gmail.com  
**Phone:** +27 646999877  
**LinkedIn:** https://www.linkedin.com/in/johanvanantwerp/

## Metadata

For complete project metadata, see `.metadata/ionity_metadata.md`

## Version History

- **v1.0** (2025) - Initial release with 24 languages/tools
  - Comprehensive language support
  - Cross-platform compatibility
  - Dry-Run default mode
  - Safety-first approach

## Contributing

This is a conservative, auditable tool. When contributing:

1. Keep commands simple and transparent
2. Default to Dry-Run for safety
3. Document all changes clearly
4. Test on multiple platforms
5. Maintain audit trail in logs

## Support

For issues, questions, or contributions:

- Email: Services@ionity.world
- LinkedIn: https://www.linkedin.com/in/johanvanantwerp/

---

**Remember:** Safety first! Test in a VM, audit commands, and understand what you're installing.
