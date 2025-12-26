#!/usr/bin/env bash
################################################################################
# Ionity Software Stack 2025 Installer - Bash Script
# Author: Johan Wilhelm van Antwerp / Ionity
# License: Creative Commons BY-NC-SA 4.0
# Description: Automated installer for Python and development tools
#              for Linux and macOS systems
################################################################################

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Log file
LOG_FILE="ionity_installer_$(date +%Y%m%d_%H%M%S).log"

################################################################################
# Utility Functions
################################################################################

log() {
    echo -e "${GREEN}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$LOG_FILE"
}

print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

################################################################################
# OS Detection
################################################################################

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        if command -v apt-get &> /dev/null; then
            PKG_MANAGER="apt"
        elif command -v dnf &> /dev/null; then
            PKG_MANAGER="dnf"
        elif command -v pacman &> /dev/null; then
            PKG_MANAGER="pacman"
        elif command -v zypper &> /dev/null; then
            PKG_MANAGER="zypper"
        else
            PKG_MANAGER="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PKG_MANAGER="brew"
    else
        OS="unknown"
        PKG_MANAGER="unknown"
    fi
    
    log "Detected OS: $OS"
    log "Package Manager: $PKG_MANAGER"
}

################################################################################
# Privilege Check
################################################################################

check_privileges() {
    if [[ "$OS" == "linux" ]]; then
        if [[ $EUID -ne 0 ]]; then
            warn "This script may require sudo privileges for some installations."
            warn "You may be prompted for your password during installation."
        fi
    fi
}

################################################################################
# Package Manager Setup
################################################################################

setup_package_manager() {
    print_header "Setting Up Package Manager"
    
    if [[ "$OS" == "macos" ]]; then
        if ! command -v brew &> /dev/null; then
            log "Homebrew not found. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            success "Homebrew installed successfully"
        else
            log "Homebrew is already installed"
            brew update
        fi
    elif [[ "$OS" == "linux" ]]; then
        if [[ "$PKG_MANAGER" == "apt" ]]; then
            log "Updating apt package lists..."
            sudo apt-get update
        elif [[ "$PKG_MANAGER" == "dnf" ]]; then
            log "Updating dnf package lists..."
            sudo dnf check-update || true
        fi
    fi
}

################################################################################
# Python Installation
################################################################################

install_python() {
    print_header "Installing Python"
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        log "Python is already installed: $PYTHON_VERSION"
    else
        log "Installing Python..."
        
        if [[ "$OS" == "macos" ]]; then
            brew install python3
        elif [[ "$OS" == "linux" ]]; then
            if [[ "$PKG_MANAGER" == "apt" ]]; then
                sudo apt-get install -y python3 python3-pip python3-venv
            elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                sudo dnf install -y python3 python3-pip
            elif [[ "$PKG_MANAGER" == "pacman" ]]; then
                sudo pacman -S --noconfirm python python-pip
            elif [[ "$PKG_MANAGER" == "zypper" ]]; then
                sudo zypper install -y python3 python3-pip
            else
                error "Unsupported package manager. Please install Python manually from https://www.python.org/downloads/"
                return 1
            fi
        fi
        
        success "Python installed successfully"
    fi
    
    # Verify Python installation
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        log "Python version: $PYTHON_VERSION"
        
        if command -v pip3 &> /dev/null; then
            PIP_VERSION=$(pip3 --version)
            log "pip version: $PIP_VERSION"
        fi
    fi
}

################################################################################
# Python Tooling Installation
################################################################################

install_python_tools() {
    print_header "Installing Python Development Tools"
    
    # Upgrade pip
    log "Upgrading pip..."
    python3 -m pip install --upgrade pip
    
    # Install virtualenv
    log "Installing virtualenv..."
    python3 -m pip install --user virtualenv
    
    # Install pipx
    log "Installing pipx..."
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    
    success "Python development tools installed successfully"
}

################################################################################
# Development Tools Installation
################################################################################

install_dev_tools() {
    print_header "Installing Development Tools"
    
    # Git
    if ! command -v git &> /dev/null; then
        log "Installing Git..."
        if [[ "$OS" == "macos" ]]; then
            brew install git
        elif [[ "$OS" == "linux" ]]; then
            if [[ "$PKG_MANAGER" == "apt" ]]; then
                sudo apt-get install -y git
            elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                sudo dnf install -y git
            elif [[ "$PKG_MANAGER" == "pacman" ]]; then
                sudo pacman -S --noconfirm git
            elif [[ "$PKG_MANAGER" == "zypper" ]]; then
                sudo zypper install -y git
            fi
        fi
        success "Git installed successfully"
    else
        log "Git is already installed: $(git --version)"
    fi
    
    # Node.js and npm
    if ! command -v node &> /dev/null; then
        log "Installing Node.js..."
        if [[ "$OS" == "macos" ]]; then
            brew install node
        elif [[ "$OS" == "linux" ]]; then
            if [[ "$PKG_MANAGER" == "apt" ]]; then
                curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
                sudo apt-get install -y nodejs
            elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                sudo dnf install -y nodejs npm
            elif [[ "$PKG_MANAGER" == "pacman" ]]; then
                sudo pacman -S --noconfirm nodejs npm
            elif [[ "$PKG_MANAGER" == "zypper" ]]; then
                sudo zypper install -y nodejs npm
            fi
        fi
        success "Node.js installed successfully"
    else
        log "Node.js is already installed: $(node --version)"
    fi
    
    # Docker (optional - user confirmation)
    if ! command -v docker &> /dev/null; then
        read -p "Do you want to install Docker? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            log "Installing Docker..."
            if [[ "$OS" == "macos" ]]; then
                warn "Please install Docker Desktop for macOS from: https://www.docker.com/products/docker-desktop"
            elif [[ "$OS" == "linux" ]]; then
                if [[ "$PKG_MANAGER" == "apt" ]]; then
                    curl -fsSL https://get.docker.com -o get-docker.sh
                    sudo sh get-docker.sh
                    rm get-docker.sh
                    sudo usermod -aG docker $USER
                    success "Docker installed successfully. Please log out and back in for group changes to take effect."
                else
                    warn "Please install Docker manually from: https://docs.docker.com/engine/install/"
                fi
            fi
        fi
    else
        log "Docker is already installed: $(docker --version)"
    fi
}

################################################################################
# Visual Studio Code Installation
################################################################################

install_vscode() {
    print_header "Installing Visual Studio Code"
    
    if ! command -v code &> /dev/null; then
        read -p "Do you want to install Visual Studio Code? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            log "Installing Visual Studio Code..."
            if [[ "$OS" == "macos" ]]; then
                brew install --cask visual-studio-code
                success "VS Code installed successfully"
            elif [[ "$OS" == "linux" ]]; then
                if [[ "$PKG_MANAGER" == "apt" ]]; then
                    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                    sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
                    sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
                    rm -f packages.microsoft.gpg
                    sudo apt-get update
                    sudo apt-get install -y code
                    success "VS Code installed successfully"
                else
                    warn "Please install VS Code manually from: https://code.visualstudio.com/download"
                fi
            fi
        fi
    else
        log "VS Code is already installed"
    fi
}

################################################################################
# Additional Languages (Optional)
################################################################################

install_additional_languages() {
    print_header "Additional Programming Languages"
    
    echo "Would you like to install additional programming languages?"
    echo "1) Java (OpenJDK)"
    echo "2) Rust"
    echo "3) Go"
    echo "4) Ruby"
    echo "5) PHP"
    echo "6) All of the above"
    echo "7) Skip"
    read -p "Enter your choice (1-7): " lang_choice
    
    case $lang_choice in
        1|6)
            log "Installing Java (OpenJDK)..."
            if [[ "$OS" == "macos" ]]; then
                brew install openjdk
            elif [[ "$PKG_MANAGER" == "apt" ]]; then
                sudo apt-get install -y default-jdk
            elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                sudo dnf install -y java-latest-openjdk
            fi
            ;&
        2|6)
            if [[ $lang_choice == 6 ]] || [[ $lang_choice == 2 ]]; then
                log "Installing Rust..."
                curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
                source "$HOME/.cargo/env"
            fi
            ;&
        3|6)
            if [[ $lang_choice == 6 ]] || [[ $lang_choice == 3 ]]; then
                log "Installing Go..."
                if [[ "$OS" == "macos" ]]; then
                    brew install go
                elif [[ "$PKG_MANAGER" == "apt" ]]; then
                    sudo apt-get install -y golang-go
                elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                    sudo dnf install -y golang
                fi
            fi
            ;&
        4|6)
            if [[ $lang_choice == 6 ]] || [[ $lang_choice == 4 ]]; then
                log "Installing Ruby..."
                if [[ "$OS" == "macos" ]]; then
                    brew install ruby
                elif [[ "$PKG_MANAGER" == "apt" ]]; then
                    sudo apt-get install -y ruby-full
                elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                    sudo dnf install -y ruby
                fi
            fi
            ;&
        5|6)
            if [[ $lang_choice == 6 ]] || [[ $lang_choice == 5 ]]; then
                log "Installing PHP..."
                if [[ "$OS" == "macos" ]]; then
                    brew install php
                elif [[ "$PKG_MANAGER" == "apt" ]]; then
                    sudo apt-get install -y php php-cli php-common
                elif [[ "$PKG_MANAGER" == "dnf" ]]; then
                    sudo dnf install -y php php-cli
                fi
            fi
            ;;
        7)
            log "Skipping additional languages installation"
            ;;
        *)
            warn "Invalid choice. Skipping additional languages installation"
            ;;
    esac
}

################################################################################
# Verification
################################################################################

verify_installation() {
    print_header "Verifying Installation"
    
    echo "Checking installed tools..."
    echo
    
    # Python
    if command -v python3 &> /dev/null; then
        echo "✓ Python: $(python3 --version)"
    else
        echo "✗ Python: Not found"
    fi
    
    # pip
    if command -v pip3 &> /dev/null; then
        echo "✓ pip: $(pip3 --version | cut -d' ' -f1-2)"
    else
        echo "✗ pip: Not found"
    fi
    
    # Git
    if command -v git &> /dev/null; then
        echo "✓ Git: $(git --version)"
    else
        echo "✗ Git: Not found"
    fi
    
    # Node.js
    if command -v node &> /dev/null; then
        echo "✓ Node.js: $(node --version)"
    else
        echo "✗ Node.js: Not found"
    fi
    
    # npm
    if command -v npm &> /dev/null; then
        echo "✓ npm: $(npm --version)"
    else
        echo "✗ npm: Not found"
    fi
    
    # Docker
    if command -v docker &> /dev/null; then
        echo "✓ Docker: $(docker --version)"
    else
        echo "✗ Docker: Not installed"
    fi
    
    # VS Code
    if command -v code &> /dev/null; then
        echo "✓ VS Code: Installed"
    else
        echo "✗ VS Code: Not installed"
    fi
    
    echo
}

################################################################################
# Main Installation Flow
################################################################################

main() {
    print_header "Ionity Software Stack 2025 Installer"
    
    log "Installation started at $(date)"
    log "Log file: $LOG_FILE"
    
    # Detect OS and package manager
    detect_os
    
    # Check privileges
    check_privileges
    
    # Confirm installation
    echo
    echo "This script will install Python and common development tools on your system."
    echo "Detected OS: $OS"
    echo "Package Manager: $PKG_MANAGER"
    echo
    read -p "Do you want to continue? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log "Installation cancelled by user"
        exit 0
    fi
    
    # Setup package manager
    setup_package_manager
    
    # Install Python
    install_python
    
    # Install Python tools
    install_python_tools
    
    # Install development tools
    install_dev_tools
    
    # Install VS Code
    install_vscode
    
    # Install additional languages
    install_additional_languages
    
    # Verify installation
    verify_installation
    
    # Final message
    print_header "Installation Complete!"
    success "Installation completed successfully at $(date)"
    success "Log file saved to: $LOG_FILE"
    
    echo
    echo "Next steps:"
    echo "1. Restart your terminal or run: source ~/.bashrc (or ~/.zshrc)"
    echo "2. Verify Python: python3 --version"
    echo "3. Verify pip: pip3 --version"
    echo "4. Create a virtual environment: python3 -m venv myenv"
    echo
    echo "For more information, visit:"
    echo "- Python: https://www.python.org/"
    echo "- Ionity: https://ionity.world"
    echo
    echo "Author: Johan Wilhelm van Antwerp / Ionity"
    echo "License: Creative Commons BY-NC-SA 4.0"
    echo
}

# Run main installation
main
