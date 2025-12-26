# Ionity Software Stack 2025 - Installation Scripts

This repository contains automated installation scripts for setting up Python and common development tools across different operating systems.

## Available Scripts

### 1. `install.sh` - Bash Script (Linux/macOS)
Automated installer for Unix-based systems (Linux and macOS).

**Features:**
- Automatic OS and package manager detection
- Installs Python 3 and pip
- Installs Python development tools (virtualenv, pipx)
- Installs common development tools (Git, Node.js, npm)
- Optional installations: Docker, Visual Studio Code
- Optional additional languages: Java, Rust, Go, Ruby, PHP
- Comprehensive logging and error handling
- Interactive prompts for optional components
- Verification of installed tools

**Supported Systems:**
- macOS (using Homebrew)
- Ubuntu/Debian (using apt)
- Fedora/RHEL (using dnf)
- Arch Linux (using pacman)
- openSUSE (using zypper)

**Usage:**
```bash
# Download the script (if not cloned)
wget https://raw.githubusercontent.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/main/install.sh

# Make it executable
chmod +x install.sh

# Run the installer
./install.sh
```

**Or if you have cloned the repository:**
```bash
cd Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS
chmod +x install.sh
./install.sh
```

### 2. `install.cmd` - Windows CMD Script
Automated installer for Windows systems using Windows Package Manager (winget).

**Features:**
- Uses winget for automated package installation
- Installs Python 3 and pip
- Installs Python development tools (virtualenv, pipx)
- Installs common development tools (Git, Node.js, npm)
- Optional installations: Docker Desktop, Visual Studio Code
- Optional additional languages: Java, Rust, Go, Ruby, PHP
- Comprehensive logging and verification
- Interactive prompts for optional components
- Environment variable refresh

**Requirements:**
- Windows 10 (version 1809 or later) or Windows 11
- Windows Package Manager (winget) - comes with App Installer from Microsoft Store

**Usage:**
```cmd
REM Download the script (if not cloned)
REM Or clone the repository first

REM Run as Administrator (recommended)
REM Right-click Command Prompt and select "Run as administrator"

cd Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS
install.cmd
```

**Note:** If winget is not installed, the script will provide instructions on how to install it.

## What Gets Installed

### Core Components (All Platforms)
- **Python 3** (latest stable version)
- **pip** (Python package manager)
- **virtualenv** (Python virtual environment tool)
- **pipx** (Python application installer)
- **Git** (version control system)
- **Node.js** (JavaScript runtime)
- **npm** (Node.js package manager)

### Optional Components
- **Docker** / **Docker Desktop** (containerization platform)
- **Visual Studio Code** (code editor)

### Optional Programming Languages
- **Java (OpenJDK)** - Java development kit
- **Rust** - Systems programming language
- **Go** - Google's programming language
- **Ruby** - Dynamic programming language
- **PHP** - Web development language

## After Installation

Once the installation is complete:

1. **Restart your terminal** (or computer for Windows) to ensure all PATH changes take effect

2. **Verify installations:**
   ```bash
   # Check Python
   python3 --version  # or 'python --version' on Windows
   
   # Check pip
   pip3 --version     # or 'pip --version' on Windows
   
   # Check Git
   git --version
   
   # Check Node.js
   node --version
   
   # Check npm
   npm --version
   ```

3. **Create a Python virtual environment:**
   ```bash
   # Create a new virtual environment
   python3 -m venv myproject
   
   # Activate it (Linux/macOS)
   source myproject/bin/activate
   
   # Activate it (Windows)
   myproject\Scripts\activate
   ```

4. **Start developing!**

## Logs

Both scripts create log files in the repository directory:
- `ionity_installer_YYYYMMDD_HHMMSS.log` (Linux/macOS)
- `ionity_installer_YYYYMMDD_HHMMSS.log` (Windows)

These logs contain detailed information about the installation process, including any errors encountered.

## Troubleshooting

### Linux/macOS

**Script won't run:**
```bash
chmod +x install.sh
./install.sh
```

**Permission denied errors:**
```bash
# The script will prompt for sudo password when needed
# Make sure your user has sudo privileges
```

**Package manager not found:**
- The script will detect your package manager automatically
- If detection fails, you may need to install packages manually

### Windows

**winget not found:**
1. Open Microsoft Store
2. Search for "App Installer"
3. Install or Update "App Installer"
4. Restart your terminal and try again

**Access denied errors:**
- Run Command Prompt as Administrator
- Right-click on Command Prompt and select "Run as administrator"

**Python not in PATH:**
1. Restart your terminal
2. If still not working, restart your computer
3. Manually add Python to PATH through System Environment Variables

## Security Note

These scripts will:
- Download and install software from official sources
- Use official package managers (Homebrew, apt, winget, etc.)
- Request administrator/sudo privileges when needed
- Create log files for audit purposes

**Recommendations:**
- Review the script contents before running
- Test in a VM or non-production environment first
- Keep your system updated
- Only run with administrator privileges when necessary

## Additional Resources

- **Python Official Documentation:** https://www.python.org/
- **Python Packaging Guide:** https://packaging.python.org/
- **Git Documentation:** https://git-scm.com/doc
- **Node.js Documentation:** https://nodejs.org/docs/
- **Ionity Project:** https://ionity.world

## Support

For issues, questions, or contributions:

- **Author:** Johan Wilhelm van Antwerp
- **Email:** Services@ionity.world
- **Alternative Email:** johan van Antwerp@gmail.com
- **Phone:** +27 646999877
- **LinkedIn:** https://www.linkedin.com/in/johanvanantwerp/
- **Location:** Centurion, South Africa

## License

**Creative Commons BY-NC-SA 4.0**

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

- **BY** - Credit must be given to the creator
- **NC** - Only noncommercial uses of the work are permitted
- **SA** - Adaptations must be shared under the same terms

**Ruled by POLICY 986 AED**

## Attribution

**Project:** Ionity 2025 | VAD 2018-2025  
**Organization:** Antwerp Designs / Ionity  
**Websites:** https://ionity.world | https://ionity.live | https://ionity.today

All rights reserved | Design Engineering | IoT | Software & Hardware Development | Integrations

---

**Version:** 1.0.0  
**Last Updated:** December 2025
