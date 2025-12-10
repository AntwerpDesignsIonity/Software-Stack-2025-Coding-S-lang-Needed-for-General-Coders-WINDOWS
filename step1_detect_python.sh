#!/bin/bash
# Step 1: Python Installation Path Detection Script
# This script automatically detects Python installations across different platforms

echo "=========================================="
echo "Python Installation Path Detection"
echo "=========================================="
echo ""

# Detect operating system
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
        echo "windows"
    else
        echo "unknown"
    fi
}

OS=$(detect_os)
echo "Detected Operating System: $OS"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detect Python installations
echo "Searching for Python installations..."
echo "--------------------------------------"

# Check for python3
if command_exists python3; then
    echo "✓ python3 found:"
    PYTHON3_PATH=$(which python3)
    echo "  Path: $PYTHON3_PATH"
    PYTHON3_VERSION=$(python3 --version 2>&1)
    echo "  Version: $PYTHON3_VERSION"
    PYTHON3_PREFIX=$(python3 -c "import sys; print(sys.prefix)" 2>/dev/null)
    echo "  Prefix: $PYTHON3_PREFIX"
    echo ""
fi

# Check for python
if command_exists python; then
    echo "✓ python found:"
    PYTHON_PATH=$(which python)
    echo "  Path: $PYTHON_PATH"
    PYTHON_VERSION=$(python --version 2>&1)
    echo "  Version: $PYTHON_VERSION"
    PYTHON_PREFIX=$(python -c "import sys; print(sys.prefix)" 2>/dev/null)
    echo "  Prefix: $PYTHON_PREFIX"
    echo ""
fi

# Platform-specific detection
case $OS in
    linux)
        echo "Linux-specific Python installations:"
        echo "--------------------------------------"
        
        # System Python
        if [ -f /usr/bin/python3 ]; then
            echo "✓ System Python: /usr/bin/python3"
        fi
        
        # Pyenv
        if [ -d "$HOME/.pyenv" ]; then
            echo "✓ Pyenv root: $HOME/.pyenv"
            if [ -d "$HOME/.pyenv/versions" ]; then
                echo "  Installed versions:"
                ls -1 "$HOME/.pyenv/versions" | sed 's/^/    - /'
            fi
        fi
        
        # Anaconda/Miniconda
        if [ -d "$HOME/anaconda3" ]; then
            echo "✓ Anaconda: $HOME/anaconda3"
        fi
        if [ -d "$HOME/miniconda3" ]; then
            echo "✓ Miniconda: $HOME/miniconda3"
        fi
        
        # User local installations
        if [ -d "$HOME/.local/bin" ]; then
            echo "✓ User local bin: $HOME/.local/bin"
        fi
        ;;
        
    macos)
        echo "macOS-specific Python installations:"
        echo "--------------------------------------"
        
        # System Python (deprecated)
        if [ -f /usr/bin/python3 ]; then
            echo "✓ System Python: /usr/bin/python3"
        fi
        
        # Python.org installation
        if [ -d "/Library/Frameworks/Python.framework" ]; then
            echo "✓ Python.org Framework: /Library/Frameworks/Python.framework"
            echo "  Versions:"
            ls -1 /Library/Frameworks/Python.framework/Versions/ | grep -E '^[0-9]' | sed 's/^/    - /'
        fi
        
        # Homebrew (Intel)
        if [ -d "/usr/local/Cellar" ]; then
            HOMEBREW_PYTHONS=$(ls -d /usr/local/Cellar/python@* 2>/dev/null)
            if [ -n "$HOMEBREW_PYTHONS" ]; then
                echo "✓ Homebrew Python (Intel):"
                echo "$HOMEBREW_PYTHONS" | sed 's/^/    - /'
            fi
        fi
        
        # Homebrew (Apple Silicon)
        if [ -d "/opt/homebrew/Cellar" ]; then
            HOMEBREW_PYTHONS=$(ls -d /opt/homebrew/Cellar/python@* 2>/dev/null)
            if [ -n "$HOMEBREW_PYTHONS" ]; then
                echo "✓ Homebrew Python (Apple Silicon):"
                echo "$HOMEBREW_PYTHONS" | sed 's/^/    - /'
            fi
        fi
        
        # Pyenv
        if [ -d "$HOME/.pyenv" ]; then
            echo "✓ Pyenv root: $HOME/.pyenv"
            if [ -d "$HOME/.pyenv/versions" ]; then
                echo "  Installed versions:"
                ls -1 "$HOME/.pyenv/versions" | sed 's/^/    - /'
            fi
        fi
        
        # Anaconda/Miniconda
        if [ -d "$HOME/anaconda3" ]; then
            echo "✓ Anaconda: $HOME/anaconda3"
        fi
        if [ -d "$HOME/miniconda3" ]; then
            echo "✓ Miniconda: $HOME/miniconda3"
        fi
        ;;
        
    windows)
        echo "Windows environment detected (Git Bash/MSYS/Cygwin)"
        echo "Note: For comprehensive Windows detection, use the PowerShell script"
        echo "--------------------------------------"
        
        # Check common Windows paths
        WINDOWS_PATHS=(
            "/c/Python3*"
            "/c/Program Files/Python3*"
            "$USERPROFILE/AppData/Local/Programs/Python/Python3*"
        )
        
        for path_pattern in "${WINDOWS_PATHS[@]}"; do
            for path in $path_pattern; do
                if [ -d "$path" ]; then
                    echo "✓ Found: $path"
                fi
            done
        done
        ;;
        
    *)
        echo "Unknown operating system"
        echo "Please refer to STEP1_PYTHON_INSTALL_PATHS.md for manual path lookup"
        ;;
esac

echo ""
echo "--------------------------------------"
echo "Detection complete!"
echo ""
echo "For detailed information about Python installation paths,"
echo "please refer to: STEP1_PYTHON_INSTALL_PATHS.md"
echo "=========================================="
