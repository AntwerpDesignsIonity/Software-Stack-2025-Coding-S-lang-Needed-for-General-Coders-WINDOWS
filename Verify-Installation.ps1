#Requires -Version 5.1

<#
.SYNOPSIS
    Verify Software Stack Installation
.DESCRIPTION
    Checks if all components of the software stack are properly installed and accessible
.NOTES
    Version: 1.0
#>

param(
    [switch]$CheckAI,
    [switch]$CheckCloud,
    [switch]$All,
    [switch]$Detailed
)

# Color output functions
function Write-Success { Write-Host "✓ $args" -ForegroundColor Green }
function Write-Failure { Write-Host "✗ $args" -ForegroundColor Red }
function Write-Warning { Write-Host "⚠ $args" -ForegroundColor Yellow }
function Write-Info { Write-Host "ℹ $args" -ForegroundColor Cyan }
function Write-Header { 
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Magenta
    Write-Host "  $args" -ForegroundColor Magenta
    Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Magenta
    Write-Host ""
}

$script:totalChecks = 0
$script:passedChecks = 0
$script:failedChecks = 0
$script:warnings = 0

function Test-Command {
    param(
        [string]$Name,
        [string]$Command,
        [string]$Category = "Core",
        [switch]$Optional
    )
    
    $script:totalChecks++
    
    try {
        $output = Invoke-Expression "$Command 2>&1" -ErrorAction Stop
        $exitCode = $LASTEXITCODE
        
        if ($exitCode -eq 0 -or $output) {
            Write-Success "$Name is installed"
            if ($Detailed) {
                $version = $output | Select-Object -First 1
                Write-Host "  Version: $version" -ForegroundColor Gray
            }
            $script:passedChecks++
            return $true
        } else {
            if ($Optional) {
                Write-Warning "$Name not found (optional)"
                $script:warnings++
            } else {
                Write-Failure "$Name not found"
                $script:failedChecks++
            }
            return $false
        }
    } catch {
        if ($Optional) {
            Write-Warning "$Name not found (optional)"
            $script:warnings++
        } else {
            Write-Failure "$Name not found"
            $script:failedChecks++
        }
        return $false
    }
}

function Test-PackageManager {
    param([string]$Name, [string]$Command)
    
    Write-Info "Checking $Name..."
    $result = Test-Command -Name $Name -Command $Command -Category "Package Manager"
    
    if ($result -and $Detailed) {
        try {
            switch ($Name) {
                "Chocolatey" {
                    $packages = choco list --local-only | Measure-Object -Line
                    Write-Host "  Installed packages: $($packages.Lines - 1)" -ForegroundColor Gray
                }
                "npm" {
                    $packages = npm list -g --depth=0 2>&1 | Measure-Object -Line
                    Write-Host "  Global packages: $($packages.Lines - 4)" -ForegroundColor Gray
                }
            }
        } catch {}
    }
}

# Main verification
Write-Header "Software Stack Installation Verification"

Write-Info "Verifying installation..."
Write-Host ""

# Package Managers
Write-Header "Package Managers"
Test-PackageManager -Name "Chocolatey" -Command "choco --version"
Test-PackageManager -Name "Scoop" -Command "scoop --version"

# Core Tools
Write-Header "Core Development Tools"
Test-Command -Name "Git" -Command "git --version"
Test-Command -Name "Visual Studio Code" -Command "code --version"
Test-Command -Name "PowerShell Core" -Command "pwsh --version"
Test-Command -Name "Docker" -Command "docker --version"
Test-Command -Name "Postman" -Command "postman --version" -Optional
Test-Command -Name "Make" -Command "make --version"
Test-Command -Name "CMake" -Command "cmake --version"
Test-Command -Name "Wget" -Command "wget --version"
Test-Command -Name "cURL" -Command "curl --version"

# Programming Languages
Write-Header "Programming Languages & Runtimes"
Test-Command -Name "Python" -Command "python --version"
Test-Command -Name "pip" -Command "pip --version"
Test-Command -Name "Node.js" -Command "node --version"
Test-Command -Name "npm" -Command "npm --version"
Test-Command -Name "Java" -Command "java --version"
Test-Command -Name "Rust" -Command "rustc --version"
Test-Command -Name "Cargo" -Command "cargo --version"
Test-Command -Name "Go" -Command "go version"
Test-Command -Name "PHP" -Command "php --version"
Test-Command -Name "Ruby" -Command "ruby --version"
Test-Command -Name "Gem" -Command "gem --version"
Test-Command -Name "Kotlin" -Command "kotlinc -version" -Optional
Test-Command -Name "Lua" -Command "lua -v" -Optional
Test-Command -Name "Dart" -Command "dart --version" -Optional
Test-Command -Name "Scala" -Command "scala -version" -Optional
Test-Command -Name "Perl" -Command "perl --version" -Optional

# TypeScript
if (Get-Command npm -ErrorAction SilentlyContinue) {
    Test-Command -Name "TypeScript" -Command "tsc --version"
}

# Databases
Write-Header "Databases"
Test-Command -Name "MySQL" -Command "mysql --version"
Test-Command -Name "PostgreSQL" -Command "psql --version"
Test-Command -Name "SQLite" -Command "sqlite3 --version"
Test-Command -Name "MongoDB" -Command "mongod --version" -Optional
Test-Command -Name "Redis" -Command "redis-cli --version" -Optional

# Python packages for web development
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Header "Python Web Frameworks"
    Write-Info "Checking Python packages..."
    
    try {
        $flaskInstalled = python -c "import flask; print(flask.__version__)" 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Flask is installed (version: $flaskInstalled)"
            $script:passedChecks++
        } else {
            Write-Warning "Flask not found (optional)"
            $script:warnings++
        }
        $script:totalChecks++
    } catch {}
    
    try {
        $djangoInstalled = python -c "import django; print(django.__version__)" 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Django is installed (version: $djangoInstalled)"
            $script:passedChecks++
        } else {
            Write-Warning "Django not found (optional)"
            $script:warnings++
        }
        $script:totalChecks++
    } catch {}
}

# AI & ML Tools (if requested or All)
if ($CheckAI -or $All) {
    Write-Header "AI & Machine Learning Tools"
    
    Test-Command -Name "Ollama" -Command "ollama --version"
    
    if (Get-Command python -ErrorAction SilentlyContinue) {
        Write-Info "Checking Python AI/ML libraries..."
        
        $aiLibraries = @("numpy", "pandas", "scikit-learn", "tensorflow", "torch", "transformers")
        
        foreach ($lib in $aiLibraries) {
            $script:totalChecks++
            try {
                $version = python -c "import $lib; print($lib.__version__)" 2>&1
                if ($LASTEXITCODE -eq 0) {
                    Write-Success "$lib is installed"
                    if ($Detailed) {
                        Write-Host "  Version: $version" -ForegroundColor Gray
                    }
                    $script:passedChecks++
                } else {
                    Write-Warning "$lib not found (optional)"
                    $script:warnings++
                }
            } catch {
                Write-Warning "$lib not found (optional)"
                $script:warnings++
            }
        }
        
        # Check if Ollama models are available
        if (Get-Command ollama -ErrorAction SilentlyContinue) {
            Write-Info "Checking Ollama models..."
            try {
                $models = ollama list 2>&1
                if ($models -match "llama2|mistral|codellama") {
                    Write-Success "Ollama models installed"
                    if ($Detailed) {
                        Write-Host $models -ForegroundColor Gray
                    }
                } else {
                    Write-Warning "No Ollama models found. Run 'ollama pull llama2' to download"
                }
            } catch {
                Write-Warning "Could not check Ollama models"
            }
        }
    }
}

# Cloud SDKs (if requested or All)
if ($CheckCloud -or $All) {
    Write-Header "Cloud SDKs & CLI Tools"
    
    Test-Command -Name "Firebase CLI" -Command "firebase --version" -Optional
    Test-Command -Name "Google Cloud SDK" -Command "gcloud --version" -Optional
    Test-Command -Name "AWS CLI" -Command "aws --version" -Optional
    Test-Command -Name "Azure CLI" -Command "az --version" -Optional
}

# Environment Variables Check
Write-Header "Environment Check"

Write-Info "Checking PATH..."
$pathEntries = $env:Path -split ';' | Where-Object { $_ -ne "" }
Write-Host "  PATH contains $($pathEntries.Count) entries" -ForegroundColor Gray

if ($Detailed) {
    Write-Host "  Key paths:" -ForegroundColor Gray
    $pathEntries | Where-Object { 
        $_ -match "python|node|java|rust|go|git|chocolatey" 
    } | ForEach-Object {
        Write-Host "    $_" -ForegroundColor DarkGray
    }
}

# Disk Space Check
Write-Header "System Resources"

$drive = Get-PSDrive C
$freeSpaceGB = [math]::Round($drive.Free / 1GB, 2)
$usedSpaceGB = [math]::Round($drive.Used / 1GB, 2)
$totalSpaceGB = [math]::Round(($drive.Free + $drive.Used) / 1GB, 2)

Write-Info "Disk Space (C:):"
Write-Host "  Total: $totalSpaceGB GB" -ForegroundColor Gray
Write-Host "  Used: $usedSpaceGB GB" -ForegroundColor Gray
Write-Host "  Free: $freeSpaceGB GB" -ForegroundColor Gray

if ($freeSpaceGB -lt 5) {
    Write-Warning "Low disk space! Less than 5GB free"
}

# Memory Check
$memory = Get-CimInstance Win32_OperatingSystem
$totalMemoryGB = [math]::Round($memory.TotalVisibleMemorySize / 1MB, 2)
$freeMemoryGB = [math]::Round($memory.FreePhysicalMemory / 1MB, 2)

Write-Info "Memory (RAM):"
Write-Host "  Total: $totalMemoryGB GB" -ForegroundColor Gray
Write-Host "  Free: $freeMemoryGB GB" -ForegroundColor Gray

# Summary
Write-Header "Verification Summary"

$percentPassed = if ($script:totalChecks -gt 0) { 
    [math]::Round(($script:passedChecks / $script:totalChecks) * 100, 1) 
} else { 0 }

Write-Host ""
Write-Host "Total Checks: $($script:totalChecks)" -ForegroundColor Cyan
Write-Host "Passed: $($script:passedChecks) " -ForegroundColor Green -NoNewline
Write-Host "($percentPassed%)"
Write-Host "Failed: $($script:failedChecks)" -ForegroundColor Red
Write-Host "Warnings: $($script:warnings)" -ForegroundColor Yellow
Write-Host ""

if ($script:failedChecks -eq 0) {
    Write-Success "All critical components are installed correctly!"
    Write-Host ""
    Write-Info "You're ready to start coding!"
} elseif ($script:failedChecks -le 3) {
    Write-Warning "Some components are missing, but core functionality is available."
    Write-Host ""
    Write-Info "You can still start coding with what's installed."
    Write-Info "Run the installer again to install missing components."
} else {
    Write-Failure "Many components are missing."
    Write-Host ""
    Write-Info "Please run the installer: .\Install-SoftwareStack.ps1"
}

if ($script:warnings -gt 0) {
    Write-Host ""
    Write-Info "Optional components not found are marked with ⚠"
    Write-Info "These are not required but may be useful for specific tasks."
}

Write-Host ""
Write-Info "Tips:"
Write-Host "  - If commands are not found, restart your terminal"
Write-Host "  - For detailed output, run with -Detailed flag"
Write-Host "  - To check AI tools, run with -CheckAI flag"
Write-Host "  - To check Cloud tools, run with -CheckCloud flag"
Write-Host "  - To check everything, run with -All flag"
Write-Host ""

# Exit code based on results
if ($script:failedChecks -eq 0) {
    exit 0
} elseif ($script:failedChecks -le 3) {
    exit 1
} else {
    exit 2
}
