#Requires -RunAsAdministrator

<#
.SYNOPSIS
    Complete Software Stack Installer for Windows - 2025 Edition
.DESCRIPTION
    Automated installer for comprehensive coding environment including AI tools like Ollama
    Supports fresh installations on any Windows system
.NOTES
    Version: 1.0
    Requires: Windows 10/11, PowerShell 5.1+, Administrator privileges
#>

param(
    [switch]$IncludeAI,
    [switch]$IncludeCloud,
    [switch]$All,
    [switch]$Silent
)

# Color output functions
function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

function Write-Success { Write-ColorOutput Green "✓ $args" }
function Write-Info { Write-ColorOutput Cyan "ℹ $args" }
function Write-Warning { Write-ColorOutput Yellow "⚠ $args" }
function Write-Error { Write-ColorOutput Red "✗ $args" }
function Write-Header { 
    Write-Host ""
    Write-ColorOutput Magenta "═══════════════════════════════════════════════════════════════"
    Write-ColorOutput Magenta "  $args"
    Write-ColorOutput Magenta "═══════════════════════════════════════════════════════════════"
    Write-Host ""
}

# Check if running as administrator
function Test-Administrator {
    $user = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($user)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Install Chocolatey package manager
function Install-Chocolatey {
    Write-Info "Checking for Chocolatey..."
    if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
        Write-Info "Installing Chocolatey package manager..."
        Set-ExecutionPolicy Bypass -Scope Process -Force
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        Write-Success "Chocolatey installed successfully"
    } else {
        Write-Success "Chocolatey already installed"
    }
}

# Install Scoop package manager (alternative for some tools)
function Install-Scoop {
    Write-Info "Checking for Scoop..."
    if (!(Get-Command scoop -ErrorAction SilentlyContinue)) {
        Write-Info "Installing Scoop package manager..."
        Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
        Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
        Write-Success "Scoop installed successfully"
    } else {
        Write-Success "Scoop already installed"
    }
}

# Install a package using Chocolatey
function Install-ChocoPackage {
    param(
        [string]$PackageName,
        [string]$DisplayName = $PackageName
    )
    Write-Info "Installing $DisplayName..."
    try {
        choco install $PackageName -y --ignore-checksums
        if ($LASTEXITCODE -eq 0) {
            Write-Success "$DisplayName installed"
        } else {
            Write-Warning "$DisplayName installation completed with warnings"
        }
    } catch {
        Write-Error "Failed to install $DisplayName"
    }
}

# Core Development Tools
function Install-CoreTools {
    Write-Header "Installing Core Development Tools"
    
    $coreTools = @(
        @{Name="git"; Display="Git"},
        @{Name="vscode"; Display="Visual Studio Code"},
        @{Name="powershell-core"; Display="PowerShell Core"},
        @{Name="windows-terminal"; Display="Windows Terminal"},
        @{Name="postman"; Display="Postman"}
    )
    
    foreach ($tool in $coreTools) {
        Install-ChocoPackage -PackageName $tool.Name -DisplayName $tool.Display
    }
}

# Programming Languages & Runtimes
function Install-Languages {
    Write-Header "Installing Programming Languages & Runtimes"
    
    $languages = @(
        @{Name="python"; Display="Python"},
        @{Name="nodejs-lts"; Display="Node.js LTS"},
        @{Name="openjdk"; Display="Java OpenJDK"},
        @{Name="rust"; Display="Rust"},
        @{Name="golang"; Display="Go (Golang)"},
        @{Name="php"; Display="PHP"},
        @{Name="ruby"; Display="Ruby"},
        @{Name="kotlin"; Display="Kotlin"},
        @{Name="lua"; Display="Lua"},
        @{Name="dart-sdk"; Display="Dart SDK"},
        @{Name="scala"; Display="Scala"},
        @{Name="perl"; Display="Perl"}
    )
    
    foreach ($lang in $languages) {
        Install-ChocoPackage -PackageName $lang.Name -DisplayName $lang.Display
    }
    
    # Install C/C++ Build Tools
    Write-Info "Installing Visual Studio Build Tools (C/C++)..."
    Install-ChocoPackage -PackageName "visualstudio2022buildtools" -DisplayName "Visual Studio 2022 Build Tools"
    Install-ChocoPackage -PackageName "visualstudio2022-workload-vctools" -DisplayName "C++ Build Tools"
    
    # Install Swift (if available)
    Write-Info "Checking for Swift..."
    Install-ChocoPackage -PackageName "swift" -DisplayName "Swift"
}

# Databases & SQL Tools
function Install-Databases {
    Write-Header "Installing Database Tools"
    
    $databases = @(
        @{Name="mysql"; Display="MySQL"},
        @{Name="postgresql"; Display="PostgreSQL"},
        @{Name="sqlite"; Display="SQLite"},
        @{Name="mongodb"; Display="MongoDB"},
        @{Name="redis"; Display="Redis"}
    )
    
    foreach ($db in $databases) {
        Install-ChocoPackage -PackageName $db.Name -DisplayName $db.Display
    }
}

# Web Development Frameworks & Tools
function Install-WebTools {
    Write-Header "Installing Web Development Tools"
    
    Write-Info "Installing TypeScript, Flask, and web frameworks..."
    
    # TypeScript via npm
    if (Get-Command npm -ErrorAction SilentlyContinue) {
        npm install -g typescript
        Write-Success "TypeScript installed globally"
    }
    
    # Python web frameworks
    if (Get-Command python -ErrorAction SilentlyContinue) {
        python -m pip install --upgrade pip
        python -m pip install flask django
        Write-Success "Flask and Django installed"
    }
    
    # Install Sass, Less for CSS preprocessing
    if (Get-Command npm -ErrorAction SilentlyContinue) {
        npm install -g sass less
        Write-Success "CSS preprocessors installed"
    }
}

# AI & Machine Learning Tools (Optional)
function Install-AITools {
    Write-Header "Installing AI & Machine Learning Tools"
    
    # Install Ollama (Local AI)
    Write-Info "Installing Ollama - Local AI Platform..."
    try {
        $ollamaInstaller = "$env:TEMP\OllamaSetup.exe"
        Write-Info "Downloading Ollama..."
        Invoke-WebRequest -Uri "https://ollama.ai/download/OllamaSetup.exe" -OutFile $ollamaInstaller
        Start-Process -FilePath $ollamaInstaller -ArgumentList "/SILENT" -Wait
        Remove-Item $ollamaInstaller -Force
        Write-Success "Ollama installed successfully"
        Write-Info "Run 'ollama run llama2' to get started with local AI"
    } catch {
        Write-Warning "Could not install Ollama automatically. Please visit https://ollama.ai for manual installation"
    }
    
    # Python AI/ML libraries
    if (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Info "Installing Python AI/ML libraries..."
        python -m pip install numpy pandas scikit-learn tensorflow torch transformers
        Write-Success "Python AI/ML libraries installed"
    }
    
    # Install CUDA Toolkit (for GPU acceleration) - optional
    Write-Info "CUDA Toolkit can be installed manually from: https://developer.nvidia.com/cuda-downloads"
}

# Cloud SDKs & CLI Tools (Optional)
function Install-CloudTools {
    Write-Header "Installing Cloud SDKs & CLI Tools"
    
    # Firebase CLI
    if (Get-Command npm -ErrorAction SilentlyContinue) {
        npm install -g firebase-tools
        Write-Success "Firebase CLI installed"
    }
    
    # Google Cloud SDK
    Install-ChocoPackage -PackageName "gcloudsdk" -DisplayName "Google Cloud SDK"
    
    # AWS CLI
    Install-ChocoPackage -PackageName "awscli" -DisplayName "AWS CLI"
    
    # Azure CLI
    Install-ChocoPackage -PackageName "azure-cli" -DisplayName "Azure CLI"
    
    # Android SDK
    Write-Info "Installing Android SDK..."
    Install-ChocoPackage -PackageName "android-sdk" -DisplayName "Android SDK"
}

# Additional Development Tools
function Install-AdditionalTools {
    Write-Header "Installing Additional Development Tools"
    
    $tools = @(
        @{Name="docker-desktop"; Display="Docker Desktop"},
        @{Name="virtualbox"; Display="VirtualBox"},
        @{Name="vagrant"; Display="Vagrant"},
        @{Name="make"; Display="Make"},
        @{Name="cmake"; Display="CMake"},
        @{Name="wget"; Display="Wget"},
        @{Name="curl"; Display="cURL"},
        @{Name="jq"; Display="jq (JSON processor)"},
        @{Name="vim"; Display="Vim"},
        @{Name="notepadplusplus"; Display="Notepad++"}
    )
    
    foreach ($tool in $tools) {
        Install-ChocoPackage -PackageName $tool.Name -DisplayName $tool.Display
    }
}

# Main installation function
function Start-Installation {
    Write-Header "Software Stack 2025 - Complete Installation"
    
    if (!(Test-Administrator)) {
        Write-Error "This script requires Administrator privileges. Please run as Administrator."
        exit 1
    }
    
    Write-Info "Starting comprehensive software stack installation..."
    Write-Info "This may take a while depending on your internet connection..."
    Write-Host ""
    
    # Install package managers
    Install-Chocolatey
    Install-Scoop
    
    # Core installations (always)
    Install-CoreTools
    Install-Languages
    Install-Databases
    Install-WebTools
    Install-AdditionalTools
    
    # Optional: AI Tools
    if ($IncludeAI -or $All) {
        Install-AITools
    } else {
        Write-Info "Skipping AI Tools installation. Use -IncludeAI flag to install."
    }
    
    # Optional: Cloud Tools
    if ($IncludeCloud -or $All) {
        Install-CloudTools
    } else {
        Write-Info "Skipping Cloud SDKs installation. Use -IncludeCloud flag to install."
    }
    
    Write-Header "Installation Complete!"
    Write-Success "All selected software has been installed."
    Write-Host ""
    Write-Info "IMPORTANT: Please restart your terminal or computer to ensure all PATH changes take effect."
    Write-Host ""
    Write-Info "Next steps:"
    Write-Host "  1. Restart your terminal/PowerShell"
    Write-Host "  2. Verify installations with: git --version, python --version, node --version, etc."
    Write-Host "  3. Configure your development environment"
    if ($IncludeAI -or $All) {
        Write-Host "  4. Start Ollama: 'ollama run llama2' for local AI"
    }
    Write-Host ""
}

# Interactive menu if no parameters provided
function Show-Menu {
    Clear-Host
    Write-Header "Software Stack 2025 Installer"
    
    Write-Host "Select installation type:"
    Write-Host ""
    Write-Host "  1. Core Installation (Git, VSCode, Languages, Databases)"
    Write-Host "  2. Core + AI Tools (includes Ollama and ML libraries)"
    Write-Host "  3. Core + Cloud SDKs (Firebase, Google Cloud, AWS, Azure)"
    Write-Host "  4. Complete Installation (Everything)"
    Write-Host "  5. Custom Selection"
    Write-Host "  Q. Quit"
    Write-Host ""
    
    $choice = Read-Host "Enter your choice (1-5, Q)"
    
    switch ($choice) {
        "1" { Start-Installation }
        "2" { $script:IncludeAI = $true; Start-Installation }
        "3" { $script:IncludeCloud = $true; Start-Installation }
        "4" { $script:All = $true; Start-Installation }
        "5" { Show-CustomMenu }
        "Q" { Write-Info "Installation cancelled."; exit 0 }
        default { Write-Warning "Invalid choice. Please try again."; Start-Sleep 2; Show-Menu }
    }
}

function Show-CustomMenu {
    Clear-Host
    Write-Header "Custom Installation Selection"
    
    Write-Host "Select components to install (Y/N):"
    Write-Host ""
    
    $installCore = (Read-Host "Install Core Tools & Languages? (Y/N)").ToUpper() -eq "Y"
    $installAI = (Read-Host "Install AI Tools (Ollama, ML libraries)? (Y/N)").ToUpper() -eq "Y"
    $installCloud = (Read-Host "Install Cloud SDKs? (Y/N)").ToUpper() -eq "Y"
    
    if (!$installCore -and !$installAI -and !$installCloud) {
        Write-Warning "No components selected. Exiting..."
        exit 0
    }
    
    $script:IncludeAI = $installAI
    $script:IncludeCloud = $installCloud
    
    Start-Installation
}

# Entry point
if ($All -or $IncludeAI -or $IncludeCloud) {
    # If parameters provided, run directly
    Start-Installation
} else {
    # Show interactive menu
    if (!$Silent) {
        Show-Menu
    } else {
        Start-Installation
    }
}
