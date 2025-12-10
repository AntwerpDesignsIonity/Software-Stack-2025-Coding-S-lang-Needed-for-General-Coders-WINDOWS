@echo off
REM Software Stack Installer - Windows Launcher
REM Ionity (Pty) Ltd | Services@ionity.world

echo ========================================
echo Software Stack Installer 2025
echo Ionity (Pty) Ltd
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python first:
    echo 1. Go to: https://www.python.org/downloads/
    echo 2. Download and install Python
    echo 3. IMPORTANT: Check "Add Python to PATH" during installation
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo Python found! Starting installer...
echo.

REM Run the installer
python "%~dp0software_stack_installer.py"

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Installer failed to start
    echo.
    pause
    exit /b 1
)

echo.
echo Installer closed.
pause
