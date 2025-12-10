# Step 1: Python Installation Path Detection Script for Windows (PowerShell)
# This script automatically detects Python installations on Windows systems

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Python Installation Path Detection (Windows)" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Function to check if path exists and display info
function Test-PythonPath {
    param (
        [string]$Path,
        [string]$Description
    )
    
    if (Test-Path $Path) {
        Write-Host "✓ $Description" -ForegroundColor Green
        Write-Host "  Path: $Path" -ForegroundColor Gray
        
        # Try to get version if it's an executable
        if ($Path -match "python\.exe$") {
            try {
                $version = & $Path --version 2>&1
                Write-Host "  Version: $version" -ForegroundColor Gray
            }
            catch {
                Write-Host "  Version: Unable to determine" -ForegroundColor Yellow
            }
        }
        return $true
    }
    return $false
}

# Search for Python in PATH
Write-Host "Searching Python in PATH..." -ForegroundColor Yellow
Write-Host "--------------------------------------"

$pythonInPath = Get-Command python -ErrorAction SilentlyContinue
if ($pythonInPath) {
    Write-Host "✓ python.exe found in PATH" -ForegroundColor Green
    Write-Host "  Path: $($pythonInPath.Source)" -ForegroundColor Gray
    try {
        $version = python --version 2>&1
        Write-Host "  Version: $version" -ForegroundColor Gray
        $prefix = python -c "import sys; print(sys.prefix)" 2>$null
        if ($prefix) {
            Write-Host "  Prefix: $prefix" -ForegroundColor Gray
        }
    }
    catch {
        Write-Host "  Unable to get details" -ForegroundColor Yellow
    }
    Write-Host ""
}

$python3InPath = Get-Command python3 -ErrorAction SilentlyContinue
if ($python3InPath) {
    Write-Host "✓ python3.exe found in PATH" -ForegroundColor Green
    Write-Host "  Path: $($python3InPath.Source)" -ForegroundColor Gray
    Write-Host ""
}

# Check common installation locations
Write-Host "Searching common installation locations..." -ForegroundColor Yellow
Write-Host "--------------------------------------"

# System-wide installations
Write-Host "`nSystem-wide installations:" -ForegroundColor Cyan
$systemPaths = @(
    "C:\Python3*",
    "C:\Program Files\Python3*",
    "C:\Program Files (x86)\Python3*"
)

$foundSystem = $false
foreach ($pattern in $systemPaths) {
    $paths = Get-ChildItem -Path $pattern -Directory -ErrorAction SilentlyContinue
    foreach ($path in $paths) {
        $foundSystem = $true
        $pythonExe = Join-Path $path.FullName "python.exe"
        if (Test-Path $pythonExe) {
            Test-PythonPath -Path $pythonExe -Description "System Python Installation"
            Write-Host "  Scripts: $(Join-Path $path.FullName 'Scripts')" -ForegroundColor Gray
            Write-Host ""
        }
    }
}

if (-not $foundSystem) {
    Write-Host "  No system-wide installations found" -ForegroundColor Gray
}

# User-specific installations
Write-Host "`nUser-specific installations:" -ForegroundColor Cyan
$userPaths = @(
    "$env:USERPROFILE\AppData\Local\Programs\Python\Python3*"
)

$foundUser = $false
foreach ($pattern in $userPaths) {
    $paths = Get-ChildItem -Path $pattern -Directory -ErrorAction SilentlyContinue
    foreach ($path in $paths) {
        $foundUser = $true
        $pythonExe = Join-Path $path.FullName "python.exe"
        if (Test-Path $pythonExe) {
            Test-PythonPath -Path $pythonExe -Description "User Python Installation"
            Write-Host "  Scripts: $(Join-Path $path.FullName 'Scripts')" -ForegroundColor Gray
            Write-Host ""
        }
    }
}

if (-not $foundUser) {
    Write-Host "  No user-specific installations found" -ForegroundColor Gray
}

# Microsoft Store Python
Write-Host "`nMicrosoft Store Python:" -ForegroundColor Cyan
$storePython = "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps\python.exe"
if (Test-PythonPath -Path $storePython -Description "Microsoft Store Python") {
    Write-Host ""
}
else {
    Write-Host "  Not installed via Microsoft Store" -ForegroundColor Gray
}

# Anaconda/Miniconda
Write-Host "`nAnaconda/Miniconda installations:" -ForegroundColor Cyan
$condaPaths = @(
    "$env:USERPROFILE\Anaconda3",
    "$env:USERPROFILE\Miniconda3",
    "C:\Anaconda3",
    "C:\Miniconda3",
    "C:\ProgramData\Anaconda3",
    "C:\ProgramData\Miniconda3"
)

$foundConda = $false
foreach ($condaPath in $condaPaths) {
    if (Test-Path $condaPath) {
        $foundConda = $true
        $pythonExe = Join-Path $condaPath "python.exe"
        if (Test-Path $pythonExe) {
            $condaType = if ($condaPath -match "Anaconda") { "Anaconda" } else { "Miniconda" }
            Test-PythonPath -Path $pythonExe -Description "$condaType Installation"
            Write-Host "  Root: $condaPath" -ForegroundColor Gray
            Write-Host "  Scripts: $(Join-Path $condaPath 'Scripts')" -ForegroundColor Gray
            
            # List conda environments
            $envsPath = Join-Path $condaPath "envs"
            if (Test-Path $envsPath) {
                $envs = Get-ChildItem -Path $envsPath -Directory -ErrorAction SilentlyContinue
                if ($envs) {
                    Write-Host "  Environments:" -ForegroundColor Gray
                    foreach ($env in $envs) {
                        Write-Host "    - $($env.Name)" -ForegroundColor Gray
                    }
                }
            }
            Write-Host ""
        }
    }
}

if (-not $foundConda) {
    Write-Host "  No Anaconda/Miniconda installations found" -ForegroundColor Gray
}

# Chocolatey Python
Write-Host "`nChocolatey Python:" -ForegroundColor Cyan
$chocoPath = "C:\Python*"
$chocoPaths = Get-ChildItem -Path $chocoPath -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "^Python\d+$" }
$foundChoco = $false
foreach ($path in $chocoPaths) {
    $foundChoco = $true
    $pythonExe = Join-Path $path.FullName "python.exe"
    if (Test-Path $pythonExe) {
        Test-PythonPath -Path $pythonExe -Description "Chocolatey Python Installation"
        Write-Host ""
    }
}

if (-not $foundChoco) {
    Write-Host "  No Chocolatey Python installations found" -ForegroundColor Gray
}

# PyEnv-Win
Write-Host "`nPyEnv-Win installations:" -ForegroundColor Cyan
$pyenvPath = "$env:USERPROFILE\.pyenv\pyenv-win"
if (Test-Path $pyenvPath) {
    Write-Host "✓ PyEnv-Win found" -ForegroundColor Green
    Write-Host "  Root: $pyenvPath" -ForegroundColor Gray
    
    $versionsPath = Join-Path $pyenvPath "versions"
    if (Test-Path $versionsPath) {
        $versions = Get-ChildItem -Path $versionsPath -Directory -ErrorAction SilentlyContinue
        if ($versions) {
            Write-Host "  Installed versions:" -ForegroundColor Gray
            foreach ($version in $versions) {
                Write-Host "    - $($version.Name)" -ForegroundColor Gray
            }
        }
    }
    Write-Host ""
}
else {
    Write-Host "  PyEnv-Win not found" -ForegroundColor Gray
}

# Summary
Write-Host ""
Write-Host "--------------------------------------" -ForegroundColor Cyan
Write-Host "Detection complete!" -ForegroundColor Green
Write-Host ""
Write-Host "For detailed information about Python installation paths," -ForegroundColor Yellow
Write-Host "please refer to: STEP1_PYTHON_INSTALL_PATHS.md" -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor Cyan

# Offer to add to PATH
Write-Host ""
$response = Read-Host "Would you like to see instructions for adding Python to PATH? (y/n)"
if ($response -eq "y" -or $response -eq "Y") {
    Write-Host ""
    Write-Host "To add Python to your PATH:" -ForegroundColor Cyan
    Write-Host "1. Open System Properties (Win + Pause/Break)" -ForegroundColor Gray
    Write-Host "2. Click 'Advanced system settings'" -ForegroundColor Gray
    Write-Host "3. Click 'Environment Variables'" -ForegroundColor Gray
    Write-Host "4. Under 'User variables' or 'System variables', find 'Path'" -ForegroundColor Gray
    Write-Host "5. Click 'Edit' and add your Python installation path" -ForegroundColor Gray
    Write-Host "6. Also add the Scripts folder (e.g., C:\Python3X\Scripts\)" -ForegroundColor Gray
    Write-Host "7. Click 'OK' to save and restart your command prompt" -ForegroundColor Gray
}
