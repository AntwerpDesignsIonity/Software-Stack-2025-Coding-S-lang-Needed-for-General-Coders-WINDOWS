# Software Stack Installer - PowerShell Launcher
# Ionity (Pty) Ltd | Services@ionity.world

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Software Stack Installer 2025" -ForegroundColor Cyan
Write-Host "Ionity (Pty) Ltd" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
    Write-Host ""
    Write-Host "Starting installer..." -ForegroundColor Yellow
    Write-Host ""
    
    # Get the directory where this script is located
    $scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
    $installerPath = Join-Path $scriptPath "software_stack_installer.py"
    
    # Run the installer
    python $installerPath
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "ERROR: Installer failed to start" -ForegroundColor Red
        Write-Host ""
        Read-Host "Press Enter to exit"
        exit 1
    }
}
catch {
    Write-Host "ERROR: Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python first:" -ForegroundColor Yellow
    Write-Host "1. Go to: https://www.python.org/downloads/"
    Write-Host "2. Download and install Python"
    Write-Host "3. IMPORTANT: Check 'Add Python to PATH' during installation"
    Write-Host "4. Run this script again"
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Installer closed." -ForegroundColor Green
Read-Host "Press Enter to exit"
