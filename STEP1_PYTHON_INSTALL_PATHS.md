# Step 1: Python Installation Paths for All Platforms

This guide provides the default installation paths for Python across different operating systems and platforms. Use these paths when configuring your development environment or setting up PATH variables.

---

## Windows Installation Paths

### Python Installed via Official Installer (python.org)
- **System-wide installation (All Users):**
  - `C:\Program Files\Python3X\` (e.g., `C:\Program Files\Python312\`)
  - `C:\Program Files\Python3X\Scripts\`

- **User-specific installation (Current User only):**
  - `C:\Users\<username>\AppData\Local\Programs\Python\Python3X\`
  - `C:\Users\<username>\AppData\Local\Programs\Python\Python3X\Scripts\`

### Python from Microsoft Store
- `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\python.exe`
- `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\python3.exe`

### Python from Anaconda/Miniconda (Windows)
- **Default Anaconda:**
  - `C:\Users\<username>\Anaconda3\`
  - `C:\Users\<username>\Anaconda3\Scripts\`

- **Default Miniconda:**
  - `C:\Users\<username>\Miniconda3\`
  - `C:\Users\<username>\Miniconda3\Scripts\`

### Python from Chocolatey
- `C:\Python3X\` (e.g., `C:\Python312\`)

---

## Linux Installation Paths

### System Python (Debian/Ubuntu)
- **Python executable:**
  - `/usr/bin/python3`
  - `/usr/bin/python3.X` (e.g., `/usr/bin/python3.12`)

- **Python libraries:**
  - `/usr/lib/python3.X/`
  - `/usr/local/lib/python3.X/`

- **User-installed packages:**
  - `~/.local/lib/python3.X/site-packages/`
  - `~/.local/bin/`

### System Python (Red Hat/CentOS/Fedora)
- **Python executable:**
  - `/usr/bin/python3`
  - `/usr/bin/python3.X`

- **Python libraries:**
  - `/usr/lib64/python3.X/`
  - `/usr/local/lib64/python3.X/`

### Python Built from Source (Linux)
- **Default installation:**
  - `/usr/local/bin/python3`
  - `/usr/local/lib/python3.X/`

### Pyenv Installation (Linux)
- **Pyenv root:**
  - `~/.pyenv/`

- **Python versions:**
  - `~/.pyenv/versions/3.X.X/bin/python`
  - `~/.pyenv/versions/3.X.X/lib/python3.X/`

### Anaconda/Miniconda (Linux)
- **Default Anaconda:**
  - `~/anaconda3/`
  - `~/anaconda3/bin/python`

- **Default Miniconda:**
  - `~/miniconda3/`
  - `~/miniconda3/bin/python`

---

## macOS Installation Paths

### System Python (macOS)
- **Pre-installed Python (deprecated in newer macOS versions):**
  - `/usr/bin/python`
  - `/usr/bin/python3`

- **System Python libraries:**
  - `/System/Library/Frameworks/Python.framework/Versions/`

### Python from python.org (macOS)
- **Framework installation:**
  - `/Library/Frameworks/Python.framework/Versions/3.X/`
  - `/Library/Frameworks/Python.framework/Versions/3.X/bin/python3`

- **Symbolic links:**
  - `/usr/local/bin/python3`
  - `/usr/local/bin/python3.X`

### Homebrew Python (macOS)
- **Homebrew installation:**
  - `/usr/local/Cellar/python@3.X/` (Intel Macs)
  - `/opt/homebrew/Cellar/python@3.X/` (Apple Silicon Macs)

- **Homebrew symbolic links:**
  - `/usr/local/bin/python3` (Intel Macs)
  - `/opt/homebrew/bin/python3` (Apple Silicon Macs)

### Pyenv Installation (macOS)
- **Pyenv root:**
  - `~/.pyenv/`

- **Python versions:**
  - `~/.pyenv/versions/3.X.X/bin/python`
  - `~/.pyenv/versions/3.X.X/lib/python3.X/`

### Anaconda/Miniconda (macOS)
- **Default Anaconda:**
  - `~/anaconda3/`
  - `~/anaconda3/bin/python`

- **Default Miniconda:**
  - `~/miniconda3/`
  - `~/miniconda3/bin/python`

---

## Android Installation Paths

### Termux (Android Terminal Emulator)
- **Python installation in Termux:**
  - `/data/data/com.termux/files/usr/bin/python`
  - `/data/data/com.termux/files/usr/lib/python3.X/`

- **User packages:**
  - `/data/data/com.termux/files/home/.local/lib/python3.X/site-packages/`

### QPython (Android Python IDE)
- **QPython3 installation:**
  - `/data/data/org.qpython.qpy3/files/bin/python3`
  - `/data/data/org.qpython.qpy3/files/lib/python3.X/`

### Pydroid 3 (Android Python IDE)
- **Pydroid 3 installation:**
  - `/data/data/ru.iiec.pydroid3/files/arm-linux-androideabi/bin/python`
  - `/data/data/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.X/`

### Python Embedded in Android Apps
- **App-specific installation (varies by app):**
  - `/data/data/<app.package.name>/files/python/`
  - `/data/data/<app.package.name>/files/python/lib/python3.X/`

### Chaquopy (Python for Android Development)
- **Chaquopy in Android projects:**
  - `app/build/generated/python/assets/chaquopy/AssetFinder/requirements/`
  - Python runtime embedded in APK

---

## iOS Installation Paths

### Pythonista (iOS Python IDE)
- **Pythonista 3 installation:**
  - Application sandbox: `/var/mobile/Containers/Data/Application/<UUID>/Documents/`
  - Python modules: Built into the Pythonista app bundle

### Pyto (iOS Python IDE)
- **Pyto installation:**
  - Application sandbox: `/var/mobile/Containers/Data/Application/<UUID>/`
  - Scripts location: Accessible via Files app integration

### Carnets (Jupyter on iOS)
- **Carnets installation:**
  - Application sandbox: `/var/mobile/Containers/Data/Application/<UUID>/Documents/`
  - Notebooks and Python environment within app

### Juno (Jupyter on iOS)
- **Juno installation:**
  - Application sandbox: `/var/mobile/Containers/Data/Application/<UUID>/`
  - Python runtime embedded in application

### iSH (Linux Shell on iOS)
- **iSH Alpine Linux environment:**
  - `/usr/bin/python3`
  - `/usr/lib/python3.X/`
  - User packages: `~/.local/lib/python3.X/site-packages/`

### a-Shell (Unix Shell on iOS)
- **a-Shell Python installation:**
  - `~/Documents/bin/python3`
  - `~/Library/lib/python3.X/`

---

## Notes and Best Practices

### Environment Variables
- **Windows:** Add to `PATH` environment variable via System Properties
- **Linux/macOS:** Add to `~/.bashrc`, `~/.zshrc`, or `~/.profile`
- **Android/iOS:** Typically managed by the app or terminal emulator

### Virtual Environments
All platforms support Python virtual environments:
```bash
python -m venv /path/to/venv
source /path/to/venv/bin/activate  # Linux/macOS
/path/to/venv/Scripts/activate      # Windows
```

### Package Installation
- **System-wide:** `pip install <package>` (may require sudo/admin)
- **User-specific:** `pip install --user <package>`
- **Virtual environment:** Activate venv first, then `pip install <package>`

### Version Management
- **pyenv** (Linux/macOS): Recommended for managing multiple Python versions
- **py launcher** (Windows): Use `py -3.X` to select specific version
- **Anaconda/Miniconda** (All platforms): Comprehensive package and environment management

### Mobile Platform Limitations
- **Android:** Python runs in sandboxed environments; system-level access limited
- **iOS:** Python runs in app sandboxes due to iOS security restrictions; no system Python installation available

---

## Quick Reference Commands

### Check Python Installation Path
```bash
# Windows (Command Prompt)
where python

# Windows (PowerShell)
Get-Command python | Select-Object -ExpandProperty Definition

# Linux/macOS/Android (Termux)/iOS (iSH)
which python3
python3 -c "import sys; print(sys.executable)"
python3 -c "import sys; print(sys.prefix)"
```

### List All Python Installations
```bash
# Linux/macOS
ls -l /usr/bin/python* /usr/local/bin/python*

# Windows (PowerShell)
Get-ChildItem -Path "C:\Program Files", "C:\Users\$env:USERNAME\AppData\Local\Programs\Python" -Recurse -Include python.exe -ErrorAction SilentlyContinue
```

---

## Additional Resources

- **Official Python Downloads:** https://www.python.org/downloads/
- **Python Documentation:** https://docs.python.org/3/
- **Pyenv:** https://github.com/pyenv/pyenv
- **Anaconda:** https://www.anaconda.com/products/distribution
- **Termux (Android):** https://termux.dev/
- **Pythonista (iOS):** http://omz-software.com/pythonista/

---

**Last Updated:** December 2025  
**Compatible with:** Python 3.8 and later versions
