@echo off
REM ############################################################################
REM Ionity Software Stack 2025 Installer - Windows CMD Script
REM Author: Johan Wilhelm van Antwerp / Ionity
REM License: Creative Commons BY-NC-SA 4.0
REM Description: Automated installer for Python and development tools
REM              for Windows systems using winget
REM ############################################################################

setlocal enabledelayedexpansion

REM Set console colors
color 0A

REM Log file
set LOG_FILE=ionity_installer_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%.log
set LOG_FILE=%LOG_FILE: =0%

REM ############################################################################
REM Header
REM ############################################################################

echo ========================================
echo Ionity Software Stack 2025 Installer
echo ========================================
echo.
echo Installation started at %date% %time%
echo Log file: %LOG_FILE%
echo.

REM Check for administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [WARN] This script may require administrator privileges for some installations.
    echo [WARN] Please run this script as Administrator for best results.
    echo.
    pause
)

REM ############################################################################
REM Check for winget
REM ############################################################################

echo ========================================
echo Checking for Windows Package Manager
echo ========================================
echo.

winget --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] winget is not installed or not available.
    echo.
    echo Windows Package Manager ^(winget^) is required for this installer.
    echo.
    echo Please install winget by:
    echo 1. Opening Microsoft Store
    echo 2. Search for "App Installer"
    echo 3. Install or Update "App Installer"
    echo.
    echo Alternatively, download from:
    echo https://github.com/microsoft/winget-cli/releases
    echo.
    pause
    exit /b 1
)

echo [SUCCESS] winget is installed
winget --version
echo.

REM ############################################################################
REM Confirm Installation
REM ############################################################################

echo This script will install Python and common development tools on your system.
echo.
set /p CONFIRM="Do you want to continue? (Y/N): "
if /i not "%CONFIRM%"=="Y" (
    echo Installation cancelled by user
    exit /b 0
)
echo.

REM ############################################################################
REM Install Python
REM ############################################################################

echo ========================================
echo Installing Python
echo ========================================
echo.

python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [INFO] Python is already installed
    python --version
) else (
    echo [INFO] Installing Python from python.org...
    winget install -e --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
    
    if %errorLevel% equ 0 (
        echo [SUCCESS] Python installed successfully
    ) else (
        echo [ERROR] Failed to install Python
        echo Please install Python manually from https://www.python.org/downloads/windows/
    )
)
echo.

REM Refresh environment variables
call :RefreshEnv

REM ############################################################################
REM Verify Python and pip
REM ############################################################################

echo ========================================
echo Verifying Python Installation
echo ========================================
echo.

python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [SUCCESS] Python version:
    python --version
) else (
    echo [ERROR] Python is not available in PATH
    echo Please restart your terminal or computer and try again
)
echo.

pip --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [SUCCESS] pip version:
    pip --version
) else (
    echo [WARN] pip is not available in PATH
    echo Attempting to install pip...
    python -m ensurepip --default-pip
)
echo.

REM ############################################################################
REM Install Python Development Tools
REM ############################################################################

echo ========================================
echo Installing Python Development Tools
echo ========================================
echo.

echo [INFO] Upgrading pip...
python -m pip install --upgrade pip
echo.

echo [INFO] Installing virtualenv...
python -m pip install --user virtualenv
echo.

echo [INFO] Installing pipx...
python -m pip install --user pipx
python -m pipx ensurepath
echo.

echo [SUCCESS] Python development tools installed
echo.

REM ############################################################################
REM Install Git
REM ############################################################################

echo ========================================
echo Installing Git
echo ========================================
echo.

git --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [INFO] Git is already installed
    git --version
) else (
    echo [INFO] Installing Git...
    winget install -e --id Git.Git --silent --accept-package-agreements --accept-source-agreements
    
    if %errorLevel% equ 0 (
        echo [SUCCESS] Git installed successfully
    ) else (
        echo [ERROR] Failed to install Git
        echo Please install Git manually from https://git-scm.com/download/win
    )
)
echo.

REM ############################################################################
REM Install Node.js
REM ############################################################################

echo ========================================
echo Installing Node.js
echo ========================================
echo.

node --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [INFO] Node.js is already installed
    node --version
) else (
    echo [INFO] Installing Node.js...
    winget install -e --id OpenJS.NodeJS.LTS --silent --accept-package-agreements --accept-source-agreements
    
    if %errorLevel% equ 0 (
        echo [SUCCESS] Node.js installed successfully
    ) else (
        echo [ERROR] Failed to install Node.js
        echo Please install Node.js manually from https://nodejs.org/
    )
)
echo.

REM ############################################################################
REM Install Visual Studio Code
REM ############################################################################

echo ========================================
echo Installing Visual Studio Code
echo ========================================
echo.

set /p INSTALL_VSCODE="Do you want to install Visual Studio Code? (Y/N): "
if /i "%INSTALL_VSCODE%"=="Y" (
    code --version >nul 2>&1
    if %errorLevel% equ 0 (
        echo [INFO] VS Code is already installed
        code --version
    ) else (
        echo [INFO] Installing Visual Studio Code...
        winget install -e --id Microsoft.VisualStudioCode --silent --accept-package-agreements --accept-source-agreements
        
        if %errorLevel% equ 0 (
            echo [SUCCESS] VS Code installed successfully
        ) else (
            echo [ERROR] Failed to install VS Code
            echo Please install VS Code manually from https://code.visualstudio.com/
        )
    )
) else (
    echo [INFO] Skipping VS Code installation
)
echo.

REM ############################################################################
REM Install Docker Desktop
REM ############################################################################

echo ========================================
echo Installing Docker Desktop
echo ========================================
echo.

set /p INSTALL_DOCKER="Do you want to install Docker Desktop? (Y/N): "
if /i "%INSTALL_DOCKER%"=="Y" (
    docker --version >nul 2>&1
    if %errorLevel% equ 0 (
        echo [INFO] Docker is already installed
        docker --version
    ) else (
        echo [INFO] Installing Docker Desktop...
        winget install -e --id Docker.DockerDesktop --silent --accept-package-agreements --accept-source-agreements
        
        if %errorLevel% equ 0 (
            echo [SUCCESS] Docker Desktop installed successfully
            echo [WARN] You may need to restart your computer for Docker to work properly
        ) else (
            echo [ERROR] Failed to install Docker Desktop
            echo Please install Docker Desktop manually from https://www.docker.com/products/docker-desktop
        )
    )
) else (
    echo [INFO] Skipping Docker Desktop installation
)
echo.

REM ############################################################################
REM Additional Programming Languages
REM ############################################################################

echo ========================================
echo Additional Programming Languages
echo ========================================
echo.

echo Would you like to install additional programming languages?
echo 1^) Java ^(OpenJDK^)
echo 2^) Rust
echo 3^) Go
echo 4^) Ruby
echo 5^) PHP
echo 6^) All of the above
echo 7^) Skip
echo.
set /p LANG_CHOICE="Enter your choice (1-7): "

if "%LANG_CHOICE%"=="1" goto INSTALL_JAVA
if "%LANG_CHOICE%"=="2" goto INSTALL_RUST
if "%LANG_CHOICE%"=="3" goto INSTALL_GO
if "%LANG_CHOICE%"=="4" goto INSTALL_RUBY
if "%LANG_CHOICE%"=="5" goto INSTALL_PHP
if "%LANG_CHOICE%"=="6" goto INSTALL_ALL_LANGS
if "%LANG_CHOICE%"=="7" goto SKIP_LANGS
goto SKIP_LANGS

:INSTALL_JAVA
echo [INFO] Installing Java (OpenJDK)...
winget install -e --id Microsoft.OpenJDK.17 --silent --accept-package-agreements --accept-source-agreements
if "%LANG_CHOICE%"=="6" goto INSTALL_RUST
goto SKIP_LANGS

:INSTALL_RUST
echo [INFO] Installing Rust...
winget install -e --id Rustlang.Rustup --silent --accept-package-agreements --accept-source-agreements
if "%LANG_CHOICE%"=="6" goto INSTALL_GO
goto SKIP_LANGS

:INSTALL_GO
echo [INFO] Installing Go...
winget install -e --id GoLang.Go --silent --accept-package-agreements --accept-source-agreements
if "%LANG_CHOICE%"=="6" goto INSTALL_RUBY
goto SKIP_LANGS

:INSTALL_RUBY
echo [INFO] Installing Ruby...
winget install -e --id RubyInstallerTeam.Ruby --silent --accept-package-agreements --accept-source-agreements
if "%LANG_CHOICE%"=="6" goto INSTALL_PHP
goto SKIP_LANGS

:INSTALL_PHP
echo [INFO] Installing PHP...
winget install -e --id XAMPP.XAMPP --silent --accept-package-agreements --accept-source-agreements
if "%LANG_CHOICE%"=="6" goto INSTALL_ALL_LANGS
goto SKIP_LANGS

:INSTALL_ALL_LANGS
echo [SUCCESS] Additional languages installed
goto SKIP_LANGS

:SKIP_LANGS
echo.

REM ############################################################################
REM Verification
REM ############################################################################

echo ========================================
echo Verifying Installation
echo ========================================
echo.

echo Checking installed tools...
echo.

REM Refresh environment
call :RefreshEnv

REM Python
python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] Python: 
    python --version
) else (
    echo [X] Python: Not found
)

REM pip
pip --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] pip: 
    pip --version
) else (
    echo [X] pip: Not found
)

REM Git
git --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] Git: 
    git --version
) else (
    echo [X] Git: Not found
)

REM Node.js
node --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] Node.js: 
    node --version
) else (
    echo [X] Node.js: Not found
)

REM npm
npm --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] npm: 
    npm --version
) else (
    echo [X] npm: Not found
)

REM Docker
docker --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] Docker: 
    docker --version
) else (
    echo [X] Docker: Not installed
)

REM VS Code
code --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] VS Code: Installed
) else (
    echo [X] VS Code: Not installed
)

echo.

REM ############################################################################
REM Final Message
REM ############################################################################

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Installation completed successfully at %date% %time%
echo Log file saved to: %LOG_FILE%
echo.
echo Next steps:
echo 1. Restart your terminal or computer to refresh environment variables
echo 2. Verify Python: python --version
echo 3. Verify pip: pip --version
echo 4. Create a virtual environment: python -m venv myenv
echo.
echo For more information, visit:
echo - Python: https://www.python.org/
echo - Ionity: https://ionity.world
echo.
echo Author: Johan Wilhelm van Antwerp / Ionity
echo License: Creative Commons BY-NC-SA 4.0
echo.
pause
exit /b 0

REM ############################################################################
REM Helper Functions
REM ############################################################################

:RefreshEnv
REM Refresh environment variables without restarting
for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path 2^>nul') do set "SystemPath=%%b"
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul') do set "UserPath=%%b"
set "PATH=%SystemPath%;%UserPath%"
goto :eof
