# Installation Steps - Software Stack Installer

This document provides the complete installation workflow for setting up your development environment using the Software Stack Installer.

## Prerequisites

✅ **Windows 10 or later**  
✅ **Internet connection** (for downloading installers)  
✅ **~20GB free disk space** (for full stack)

---

## Step-by-Step Installation Guide

### 🔷 Step 1: Install Python (REQUIRED)

Python is required to run the installer itself.

1. **Download Python:**
   - Visit: https://www.python.org/downloads/
   - Click "Download Python" (latest version)

2. **Run the Python Installer:**
   - Double-click the downloaded .exe file
   - ⚠️ **CRITICAL:** Check "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation:**
   ```cmd
   python --version
   ```
   Should display: `Python 3.x.x`

---

### 🔷 Step 2: Download the Software Stack Installer

1. **Clone or Download this Repository:**
   ```cmd
   git clone https://github.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS.git
   ```
   
   Or download as ZIP and extract

2. **Navigate to the Directory:**
   ```cmd
   cd Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS
   ```

---

### 🔷 Step 3: Run the Installer

Choose **ONE** of the following methods:

#### Method A: Double-Click (Easiest)
- Double-click `run_installer.bat`
- Or double-click `run_installer.ps1` (PowerShell)

#### Method B: Command Prompt
```cmd
python software_stack_installer.py
```

#### Method C: PowerShell
```powershell
python .\software_stack_installer.py
```

---

### 🔷 Step 4: Configure the Installer

When the GUI opens:

1. **Select Installation Directory:**
   - Default: `C:\Users\YourName\DevelopmentTools`
   - Click "Browse..." to choose a different location
   - This is where shortcuts and guides will be saved

2. **Select Software Components:**
   - ☑ Check the software you want to install
   - Use "Select All" to choose everything
   - Use "Deselect All" to clear selections
   - Python is pre-selected (required)

3. **Click "Install Selected":**
   - Confirm the installation when prompted
   - Watch the real-time progress

---

### 🔷 Step 5: Download & Install Components

After the installer finishes:

1. **Open your Installation Directory:**
   - Example: `C:\Users\YourName\DevelopmentTools`

2. **Review the Installation Guide:**
   - Open `INSTALLATION_GUIDE.txt`
   - Read the instructions for each component
   - Note the installation order

3. **Download Components:**
   - Double-click each `.url` file to open the download page
   - Download the installer for each component

4. **Install Components:**
   - Run each installer
   - ⚠️ Right-click and "Run as Administrator" if needed
   - Follow the installation wizard for each
   - Accept default settings or customize as needed

---

## Recommended Installation Order

For best results, install in this order:

### Priority 1: Core Tools
1. **Python** (already installed ✓)
2. **Git Bash** (version control)
3. **Node.js & NPM** (required for npm packages)
4. **Visual Studio Code** (code editor)

### Priority 2: Package Managers & CLI
5. **PowerShell 7** (modern shell)
6. **TypeScript** (npm package)
7. **Firebase CLI** (npm package: firebase-tools)

### Priority 3: Programming Languages
8. **Java (JDK)**
9. **Go (Golang)**
10. **Rust**
11. **C++ (MinGW/MSYS2)**
12. **C# (.NET SDK)**
13. Other languages as needed

### Priority 4: Cloud & Mobile
14. **Google Cloud SDK**
15. **Android SDK** (via Android Studio)

### Priority 5: Python Packages
16. **Flask** (pip package)
17. Other Python packages

### Priority 6: Specialized Tools
18. **Ruby**
19. **PHP**
20. **Scala**
21. **MATLAB** (requires license)
22. Other specialized languages

---

## Installation Tips

### ✅ Best Practices

1. **Read License Agreements:**
   - Some software has specific licensing terms
   - MATLAB requires a commercial license

2. **Choose Installation Paths Carefully:**
   - Use default paths when possible
   - Avoid paths with spaces for programming tools

3. **Update PATH Variables:**
   - Most installers add to PATH automatically
   - Restart your terminal after each installation

4. **Install Dependencies First:**
   - Node.js before npm packages
   - Python before pip packages

5. **Reboot When Needed:**
   - Some installers may require a system restart

### ⚠️ Common Issues

**"Command not found"**
- The tool is not in your PATH
- Restart your terminal
- Reinstall with "Add to PATH" option

**"Permission denied"**
- Run installer as Administrator
- Check antivirus isn't blocking

**"Port already in use"**
- Another service is using the port
- Stop conflicting services

---

## Verification

After installation, verify each tool:

```cmd
# Check installed versions
python --version
node --version
npm --version
git --version
java --version
rustc --version
go version
dotnet --version
code --version
```

---

## Next Steps

Once installation is complete:

1. **Configure your development environment:**
   - Set up VS Code extensions
   - Configure Git (name, email)
   - Set up SSH keys for GitHub

2. **Create test projects:**
   - Hello World in each language
   - Verify tools work correctly

3. **Explore documentation:**
   - Read official docs for each tool
   - Follow tutorials

4. **Join communities:**
   - Stack Overflow
   - GitHub
   - Reddit programming communities

---

## Uninstallation

To remove installed software:

1. Use Windows "Add or Remove Programs"
2. Search for each installed tool
3. Click "Uninstall"

Or use package managers:
```cmd
# Uninstall npm packages
npm uninstall -g typescript firebase-tools

# Uninstall pip packages
pip uninstall flask
```

---

## Support

**Need help?**

- 📧 Email: Services@ionity.world
- 📞 Phone: +27 646 999 877
- 📚 Documentation: See [README.md](README.md)
- 🚀 Quick Start: See [QUICKSTART.md](QUICKSTART.md)
- ✨ Features: See [FEATURES.md](FEATURES.md)

---

## Additional Resources

### Official Documentation Links

- **Python:** https://docs.python.org/
- **Node.js:** https://nodejs.org/docs/
- **Git:** https://git-scm.com/doc
- **VS Code:** https://code.visualstudio.com/docs
- **Java:** https://docs.oracle.com/en/java/
- **Rust:** https://doc.rust-lang.org/
- **Go:** https://go.dev/doc/
- **.NET:** https://docs.microsoft.com/dotnet/
- **TypeScript:** https://www.typescriptlang.org/docs/
- **Firebase:** https://firebase.google.com/docs
- **Google Cloud:** https://cloud.google.com/docs

### Learning Resources

- **FreeCodeCamp:** https://www.freecodecamp.org/
- **MDN Web Docs:** https://developer.mozilla.org/
- **W3Schools:** https://www.w3schools.com/
- **GitHub Learning Lab:** https://lab.github.com/
- **Codecademy:** https://www.codecademy.com/

---

**© 2025 Ionity (Pty) Ltd. All rights reserved.**

Developed by Johan Wilhelm van Antwerp  
Centurion, South Africa
