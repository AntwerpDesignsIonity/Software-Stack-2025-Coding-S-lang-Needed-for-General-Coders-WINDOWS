# Developer Guide - Software Stack Installer

This guide is for developers who want to modify, extend, or understand the Software Stack Installer.

## Architecture Overview

### Core Components

```
software_stack_installer.py     # Main application
├── SoftwareStackInstaller      # Main GUI class
│   ├── __init__()              # Initialize GUI and data
│   ├── create_ui()             # Build the interface
│   ├── browse_directory()      # Directory selection
│   ├── select_all()            # Select all components
│   ├── deselect_all()          # Deselect all components
│   ├── start_installation()    # Validate and start
│   └── install_components()    # Install logic (threaded)
└── main()                      # Entry point
```

### Data Structure

```python
software_components = {
    "Category Name": {
        "Software Name": {
            "url": "download_url or pip/npm",
            "package": "exact_package_name",  # Optional
            "checked": True/False
        }
    }
}
```

## Adding New Software

### 1. Add to Software Components Dictionary

```python
"Your Category": {
    "Software Name": {
        "url": "https://example.com/download",
        "checked": False
    }
}
```

### 2. For pip Packages

```python
"Python Package": {
    "url": "pip",
    "package": "actual-package-name",  # PyPI package name
    "checked": False
}
```

### 3. For npm Packages

```python
"Node Package": {
    "url": "npm",
    "package": "actual-package-name",  # npm package name
    "checked": False
}
```

### 4. For Built-in Tools

```python
"Built-in Tool": {
    "url": "builtin",
    "checked": False
}
```

## Customizing the Installer

### Changing Default Installation Directory

```python
self.install_dir = tk.StringVar(value="C:\\MyCustomPath")
```

### Modifying Window Size

```python
self.root.geometry("1024x768")  # width x height
```

### Changing Default Selections

Set `"checked": True` for components you want pre-selected:

```python
"Python": {"url": "...", "checked": True}
```

### Adding New Categories

Simply add a new top-level key to `software_components`:

```python
"Database Systems": {
    "PostgreSQL": {"url": "...", "checked": False},
    "MongoDB": {"url": "...", "checked": False}
}
```

## Testing Changes

### 1. Syntax Validation

```bash
python -m py_compile software_stack_installer.py
```

### 2. Run Test Suite

```bash
python test_installer.py
```

### 3. Manual Testing

```bash
python software_stack_installer.py
```

## Code Style Guidelines

### Naming Conventions

- **Classes:** `PascalCase` (e.g., `SoftwareStackInstaller`)
- **Methods:** `snake_case` (e.g., `create_ui()`)
- **Variables:** `snake_case` (e.g., `install_dir`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `DEFAULT_PATH`)

### Documentation

```python
def method_name(self, param):
    """
    Brief description of what the method does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    pass
```

## Common Modifications

### 1. Add Progress Callback

```python
def install_components(self, selected_items, callback=None):
    for item in selected_items:
        # Process item
        if callback:
            callback(item, progress_percent)
```

### 2. Add Download Functionality

```python
import urllib.request

def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)
```

### 3. Add Custom Logging

```python
import logging

logging.basicConfig(filename='installer.log', level=logging.INFO)
logging.info(f"Installing {item_name}")
```

### 4. Add Configuration File Support

```python
import json

def save_config(self, filename="config.json"):
    config = {
        "install_dir": self.install_dir.get(),
        "selected": [k for k, v in self.check_vars.items() if v.get()]
    }
    with open(filename, 'w') as f:
        json.dump(config, f, indent=2)

def load_config(self, filename="config.json"):
    with open(filename, 'r') as f:
        config = json.load(f)
    self.install_dir.set(config["install_dir"])
    for name, var in self.check_vars.items():
        var.set(name in config["selected"])
```

## Extending Functionality

### Add Automatic Downloads

Replace URL shortcut creation with actual downloads:

```python
import urllib.request
import os

def download_installer(url, item_name, install_path):
    """Download installer file"""
    filename = f"{item_name.replace(' ', '_')}.exe"
    filepath = install_path / filename
    
    try:
        urllib.request.urlretrieve(url, filepath)
        return True
    except Exception as e:
        print(f"Error downloading {item_name}: {e}")
        return False
```

### Add Version Detection

```python
import subprocess

def get_installed_version(command):
    """Get version of installed software"""
    try:
        result = subprocess.run([command, '--version'], 
                              capture_output=True, 
                              text=True)
        return result.stdout.strip()
    except:
        return None
```

### Add Update Checking

```python
def check_updates(self):
    """Check if newer versions are available"""
    # Implement version checking logic
    pass
```

## Troubleshooting Development Issues

### tkinter Not Found

**Windows:**
- Reinstall Python with "tcl/tk and IDLE" option

**Linux (for development):**
```bash
sudo apt-get install python3-tk
```

### GUI Not Responsive During Installation

Ensure installation runs in a separate thread:

```python
thread = threading.Thread(target=self.install_components, args=(items,))
thread.daemon = True
thread.start()
```

### Encoding Issues

Use UTF-8 encoding for file operations:

```python
with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
```

## Building Executable (Optional)

To create a standalone .exe file:

### Using PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile --windowed software_stack_installer.py
```

Options:
- `--onefile`: Single executable
- `--windowed`: No console window
- `--icon=icon.ico`: Custom icon

### Using cx_Freeze

```python
# setup.py
from cx_Freeze import setup, Executable

setup(
    name="SoftwareStackInstaller",
    version="1.0",
    description="Software Stack Installer",
    executables=[Executable("software_stack_installer.py")]
)
```

```bash
python setup.py build
```

## Security Considerations

### Input Validation

Always validate user inputs:

```python
def validate_path(path):
    """Validate installation path"""
    if not path or not os.path.isabs(path):
        return False
    return True
```

### Safe File Operations

Use safe path handling:

```python
from pathlib import Path

safe_path = Path(user_input).resolve()
if not str(safe_path).startswith(str(base_path)):
    raise ValueError("Invalid path")
```

### URL Validation

Validate URLs before using them:

```python
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
```

## Testing Checklist

Before committing changes:

- [ ] Syntax validation passes
- [ ] Test suite passes
- [ ] Manual testing in GUI mode
- [ ] All categories visible
- [ ] All checkboxes functional
- [ ] Directory selection works
- [ ] Installation process completes
- [ ] Files created correctly
- [ ] No Python errors in console
- [ ] Documentation updated

## Contributing

When contributing to this project:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## Release Process

### Version Numbering

Use semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes
- **MINOR:** New features
- **PATCH:** Bug fixes

### Creating a Release

1. Update version in code
2. Update CHANGELOG
3. Test thoroughly
4. Tag the release
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

## Support and Contact

**Development Questions:**
- Create an issue on GitHub
- Email: Services@ionity.world

**Bug Reports:**
- Include Python version
- Include full error traceback
- Include steps to reproduce

**Feature Requests:**
- Describe the feature
- Explain the use case
- Suggest implementation if possible

---

**© 2025 Ionity (Pty) Ltd**

This project is maintained by Ionity (Pty) Ltd.  
For commercial support and custom development, contact Services@ionity.world.
