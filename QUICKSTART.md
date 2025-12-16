# Quick Start Guide - Ionity Software Stack Installer

This is a quick reference for using the Ionity Software Stack 2025 Installer.

## Prerequisites

- Python 3.8 or higher installed
- Tkinter (usually comes with Python)

## Running the Installer

### Windows
```cmd
python scripts\ionity_installer_gui.py
```

### macOS / Linux
```bash
python3 scripts/ionity_installer_gui.py
```

## First Time Usage

1. **Launch** - Run the command above
2. **Check OS Detection** - Verify the correct OS is detected at the top
3. **Select Tools** - Choose what you want to install:
   - Use checkboxes to select individual items
   - Or click "Select All" for everything
4. **Preview** - Click "Preview Commands" to see what will run
5. **Test with Dry-Run** - Leave "Dry-Run Mode" checked for testing
6. **Review Log** - Check the log area at the bottom to see what would happen
7. **Accept Terms** - When ready to install, check "I understand and accept"
8. **Uncheck Dry-Run** - Uncheck "Dry-Run Mode" 
9. **Install** - Click "Install Selected"
10. **Monitor** - Watch the log area for progress and any errors

## Safety Features

- ✓ **Dry-Run by Default** - Won't install anything until you uncheck it
- ✓ **Preview Commands** - See exact commands before running
- ✓ **Explicit Confirmation** - Must check "I understand and accept"
- ✓ **Comprehensive Logging** - Everything logged to `installer_log.txt`

## Categories

### Languages - Core
Python, JavaScript, TypeScript, Java, C#, C++, Rust, Go, PHP, Ruby

### Languages - Extended  
Swift, Kotlin, Scala, Perl, R, Dart, Ada, Objective-C, Delphi, Assembly

### Development Tools
Git, Docker, VS Code, Firebase CLI, Google Cloud SDK, AWS CLI, Yarn, pnpm

### Specialized
MATLAB, Visual Basic, SQL Tools

## Package Managers Used

- **Windows**: winget (Windows Package Manager)
- **macOS**: Homebrew (brew)
- **Linux**: apt (Debian/Ubuntu)

## Troubleshooting

**Script won't start?**
- Ensure Python 3.8+ is installed
- Check that Tkinter is available: `python3 -c "import tkinter"`

**Permission errors?**
- Windows: Run as Administrator
- macOS/Linux: Use `sudo` when prompted

**Installation fails?**
- Check `installer_log.txt` in the repository root
- Ensure package manager is installed (winget/brew/apt)
- Some tools may need manual installation

## Log File

All actions are logged to: `installer_log.txt`

Check this file for:
- What commands were run
- Success/failure status
- Error messages
- Timestamps

## Need Help?

See the full documentation in `scripts/README.md`

## License & Attribution

Author: Johan Wilhelm van Antwerp / Ionity
License: Creative Commons BY-NC-SA 4.0
Contact: Services@ionity.world

---

**Remember**: Always use Dry-Run mode first to see what will happen!
