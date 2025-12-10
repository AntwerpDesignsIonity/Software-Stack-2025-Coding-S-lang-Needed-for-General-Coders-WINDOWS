# Ionity Installer GUI - README

## Purpose

The `ionity_installer_gui.py` script provides a **safe, auditable, cross-platform GUI installer** for a comprehensive set of programming languages and development tools. It is built with Python 3.8+ and Tkinter, offering an interactive interface for developers to select and install tools across Windows, macOS, and Linux platforms.

## Safety Features

**IMPORTANT**: This installer is designed with safety as the primary concern:

1. **Dry-Run Mode (Default)**: The installer defaults to "Dry-Run" mode, which only displays commands without executing them.
2. **Explicit Confirmation Required**: Users must uncheck "Dry-Run" and check a confirmation checkbox that clearly states the installer will make system changes.
3. **Command Preview**: All commands are displayed in a preview window before execution.
4. **Elevation Prompts**: The installer prompts for elevation when needed (sudo/UAC) rather than executing privileged commands automatically.
5. **Comprehensive Logging**: All commands and their output (stdout/stderr) are logged to `installer.log` in the repository root.
6. **Vendor-Only Installers**: For proprietary software (MATLAB, Visual Studio, Delphi), the installer uses `open_url:` pseudo-commands to open vendor websites rather than attempting downloads.
7. **Audit Before Use**: All commands are suggestions and must be audited by the user before running.

## Supported Operating Systems

- **Windows**: Uses `winget` package manager
- **macOS**: Uses Homebrew (`brew`)
- **Linux**: Uses `apt` (Debian/Ubuntu-based distributions)

**Note**: For other Linux distributions (Fedora, Arch, etc.), maintainers should update the command mappings in `get_commands_for_item()`.

## Supported Languages & Tools

The installer includes checkboxes for the following:

### Programming Languages
- JavaScript
- Java
- PHP
- Python
- Rust
- Swift
- C++
- C#
- Ruby
- R
- SQL (SQLite)
- Kotlin
- TypeScript
- MATLAB (vendor link)
- Perl
- Go
- Dart
- Visual Basic (vendor link)
- Scala
- CSS tooling
- Assembly (NASM)
- Objective-C
- Delphi/Object Pascal (vendor link)
- Ada

### Development Tools
- Git
- Node.js
- Docker
- Visual Studio Code
- Firebase CLI
- Google Cloud SDK (gcloud)
- AWS CLI

## Usage

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually included with Python; on some Linux systems: `sudo apt install python3-tk`)

### Steps

1. **Navigate to the scripts directory**:
   ```bash
   cd scripts
   ```

2. **Run the installer**:
   ```bash
   python3 ionity_installer_gui.py
   ```
   or
   ```bash
   python ionity_installer_gui.py
   ```

3. **In the GUI**:
   - Select the languages and tools you want to install by checking the boxes
   - **By default, Dry-Run mode is enabled** - the installer will only preview commands
   - Click "Preview Commands" to see what commands would be executed
   - To actually install, uncheck "Dry-Run Mode" and check the confirmation box
   - Click "Install Selected" to begin installation

4. **Review the log**:
   - All commands and output are logged to `installer.log` in the repository root
   - Review this log to verify what was installed

### Testing in a Virtual Machine

**STRONGLY RECOMMENDED**: Test the installer in a virtual machine (VM) or container before running on your production system:
- VirtualBox, VMware, Hyper-V, or similar
- Docker container
- Cloud VM instance

This allows you to:
- Verify the commands are appropriate for your system
- Test the installation process safely
- Understand what changes will be made

## Command Auditing

**Before using this installer on a production system:**

1. Run in Dry-Run mode and review the commands
2. Check that package names are correct for your OS/distribution
3. Verify that package manager commands (winget, brew, apt) are appropriate
4. Understand that some tools may require additional configuration after installation
5. For vendor-only software, you'll be directed to the official download page

## Customization

To customize commands for your environment:

1. Open `ionity_installer_gui.py` in a text editor
2. Locate the `get_commands_for_item()` function
3. Update package names or commands for your specific needs
4. Add TODOs or comments for maintainers where needed

## Limitations & Notes

- **Distribution-specific**: Linux commands are written for Debian/Ubuntu (apt). Other distributions will need command updates.
- **Package availability**: Not all packages are available via all package managers. Some may require manual installation.
- **Vendor installers**: MATLAB, Visual Studio, and Delphi require downloading from vendor websites (the installer opens these URLs).
- **Network required**: Most installations require an internet connection to download packages.
- **Permissions**: Some installations require administrator/sudo privileges.

## Troubleshooting

- **"tkinter not found"**: Install with `sudo apt install python3-tk` (Linux) or reinstall Python with Tkinter support
- **"command not found"**: Ensure the package manager (winget, brew, apt) is installed and in your PATH
- **"permission denied"**: Some commands require sudo/administrator privileges
- **Package not available**: Check the package name for your OS/distribution

## Support & Contributions

For issues, updates, or contributions:
- Review the main README.md in the repository root
- Check `.metadata/ionity_metadata.md` for contact information
- Test changes in a VM before submitting pull requests
- Document any changes to command mappings

## License & Policy

- Creative Commons BY-NC-SA 4.0 Applies
- Ruled by POLICY 986 AED

---

**Remember**: Always audit commands before running them on your system. This installer is a tool to assist with setup, not a fully-automated solution.
