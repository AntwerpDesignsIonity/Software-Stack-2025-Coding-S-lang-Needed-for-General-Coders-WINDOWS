# Complete Installation Guide

## Table of Contents

1. [Before You Begin](#before-you-begin)
2. [Step-by-Step Installation](#step-by-step-installation)
3. [Understanding the Components](#understanding-the-components)
4. [Advanced Options](#advanced-options)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

## Before You Begin

### System Requirements

- **Operating System:** Windows 10 (version 1809 or later) or Windows 11
- **Architecture:** 64-bit (x64)
- **Disk Space:** 
  - Core Installation: ~5GB
  - With AI Tools: ~15GB (AI models require significant space)
  - Complete Installation: ~20GB
- **RAM:** 8GB minimum (16GB recommended for AI tools)
- **Internet:** Stable broadband connection

### Preparation Steps

1. **Check Windows Version:**
   ```powershell
   winver
   ```
   Ensure you're running Windows 10 1809+ or Windows 11

2. **Check PowerShell Version:**
   ```powershell
   $PSVersionTable.PSVersion
   ```
   Should be 5.1 or higher

3. **Free Up Disk Space:**
   - Clean temporary files
   - Remove unnecessary programs
   - Ensure at least 20GB free space

4. **Backup Important Data:**
   - While the installer is safe, it's always good practice to backup

5. **Close Unnecessary Applications:**
   - Especially antivirus (temporarily)
   - IDE applications
   - Package managers

## Step-by-Step Installation

### Option A: Quick Installation (Recommended for Beginners)

**Step 1: Open PowerShell as Administrator**

- Press `Win + X`
- Select "Windows PowerShell (Admin)" or "Terminal (Admin)"
- Click "Yes" on the UAC prompt

**Step 2: Allow Script Execution**

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
```

**Step 3: Download the Installer**

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/main/Install-SoftwareStack.ps1" -OutFile "$env:USERPROFILE\Downloads\Install-SoftwareStack.ps1"
```

**Step 4: Navigate to Downloads**

```powershell
cd $env:USERPROFILE\Downloads
```

**Step 5: Run the Installer**

```powershell
.\Install-SoftwareStack.ps1
```

**Step 6: Follow the Interactive Menu**

The installer will present you with options:
- Option 1: Core Installation (recommended for most users)
- Option 2: Core + AI Tools (includes Ollama)
- Option 3: Core + Cloud SDKs
- Option 4: Complete Installation

Select your preferred option by typing the number and pressing Enter.

**Step 7: Wait for Installation**

- The installer will show progress for each component
- This may take 30-60 minutes
- Do not close the PowerShell window
- You may see UAC prompts - click "Yes"

**Step 8: Restart Your Terminal**

After installation completes, close and reopen PowerShell to refresh PATH variables.

### Option B: Advanced Installation (For Experienced Users)

**Direct Installation with Parameters:**

```powershell
# Core only
.\Install-SoftwareStack.ps1

# Core + AI Tools
.\Install-SoftwareStack.ps1 -IncludeAI

# Core + Cloud SDKs
.\Install-SoftwareStack.ps1 -IncludeCloud

# Everything
.\Install-SoftwareStack.ps1 -All
```

### Option C: Repository Clone Installation

**Step 1: Install Git (if not already installed)**

```powershell
# Install Git via Chocolatey quick install
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install git -y
```

**Step 2: Clone the Repository**

```powershell
git clone https://github.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS.git
cd Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS
```

**Step 3: Run the Installer**

```powershell
.\Install-SoftwareStack.ps1
```

## Understanding the Components

### Package Managers

**Chocolatey:**
- Primary package manager for Windows
- Used for installing most software
- Website: https://chocolatey.org

**Scoop:**
- Alternative package manager
- Used for some command-line tools
- Website: https://scoop.sh

Both are installed automatically if not present.

### Core Development Tools

| Tool | Purpose | Post-Install Command |
|------|---------|---------------------|
| Git | Version control | `git --version` |
| VS Code | Code editor | `code --version` |
| PowerShell Core | Modern shell | `pwsh --version` |
| Windows Terminal | Terminal emulator | Launch from Start menu |
| Postman | API testing | Launch from Start menu |

### Programming Languages

| Language | Use Case | Verify Installation |
|----------|----------|-------------------|
| Python | General-purpose, AI/ML | `python --version` |
| Node.js | JavaScript runtime, web | `node --version` |
| Java | Enterprise, Android | `java --version` |
| Rust | Systems programming | `rustc --version` |
| Go | Cloud, microservices | `go version` |
| PHP | Web development | `php --version` |
| Ruby | Web, scripting | `ruby --version` |
| C/C++ | Systems, performance | `cl` (MSVC) |

### AI Tools (Optional)

**Ollama:**
- Runs AI models locally on your machine
- Supports Llama 2, Mistral, CodeLlama, and more
- No cloud connection needed after model download
- Privacy-friendly - all processing happens locally

**Ollama Quick Start:**
```bash
# Check installation
ollama --version

# List available models
ollama list

# Download and run Llama 2
ollama run llama2

# Download and run CodeLlama (code generation)
ollama run codellama

# Pull a model without running
ollama pull mistral
```

**Python AI Libraries:**
- **NumPy:** Numerical computing
- **Pandas:** Data manipulation
- **Scikit-learn:** Traditional ML algorithms
- **TensorFlow:** Deep learning (Google)
- **PyTorch:** Deep learning (Meta)
- **Transformers:** NLP, Hugging Face models

### Cloud SDKs (Optional)

**Firebase CLI:**
- Manage Firebase projects
- Deploy web apps and functions
- Test locally

**Google Cloud SDK:**
- Interact with GCP services
- Deploy applications
- Manage cloud resources

**AWS CLI:**
- Control AWS services
- Automate deployments
- Script cloud operations

**Azure CLI:**
- Manage Azure resources
- Deploy applications
- Script automations

**Android SDK:**
- Build Android apps
- Use with Android Studio
- Command-line tools

## Advanced Options

### Custom Component Selection

You can modify the script to install only specific components by editing the PowerShell script:

```powershell
# Edit the script
notepad Install-SoftwareStack.ps1

# Comment out unwanted sections with #
# For example, to skip Ruby:
# Install-ChocoPackage -PackageName "ruby" -DisplayName "Ruby"
```

### Silent Installation

For automated deployments:

```powershell
.\Install-SoftwareStack.ps1 -All -Silent
```

### Environment-Specific Installations

**For Web Developers:**
```powershell
# Install core + Node.js focused tools
.\Install-SoftwareStack.ps1
# Then manually: npm install -g @angular/cli @vue/cli create-react-app
```

**For Data Scientists:**
```powershell
# Install core + AI tools
.\Install-SoftwareStack.ps1 -IncludeAI
# Then manually: pip install jupyter notebook pandas matplotlib seaborn
```

**For Mobile Developers:**
```powershell
# Install core + cloud + Android SDK
.\Install-SoftwareStack.ps1 -IncludeCloud
# Then manually install Android Studio
```

## Verification

### Complete Verification Script

Save this as `verify-installation.ps1`:

```powershell
#Requires -Version 5.1

Write-Host "Verifying Software Stack Installation..." -ForegroundColor Cyan
Write-Host ""

$tools = @(
    @{Name="Git"; Command="git --version"},
    @{Name="Python"; Command="python --version"},
    @{Name="Node.js"; Command="node --version"},
    @{Name="npm"; Command="npm --version"},
    @{Name="Java"; Command="java --version"},
    @{Name="Rust"; Command="rustc --version"},
    @{Name="Go"; Command="go version"},
    @{Name="PHP"; Command="php --version"},
    @{Name="Ruby"; Command="ruby --version"},
    @{Name="Docker"; Command="docker --version"},
    @{Name="MySQL"; Command="mysql --version"},
    @{Name="PostgreSQL"; Command="psql --version"},
    @{Name="Ollama"; Command="ollama --version"}
)

foreach ($tool in $tools) {
    try {
        $output = Invoke-Expression $tool.Command 2>&1
        if ($LASTEXITCODE -eq 0 -or $output) {
            Write-Host "✓ $($tool.Name): Installed" -ForegroundColor Green
        } else {
            Write-Host "✗ $($tool.Name): Not found" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "✗ $($tool.Name): Not found" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Verification complete!" -ForegroundColor Cyan
```

Run it:
```powershell
.\verify-installation.ps1
```

### Individual Tool Verification

**Core Tools:**
```powershell
git --version
code --version
docker --version
```

**Languages:**
```powershell
python --version
node --version
java --version
go version
rustc --version
php --version
ruby --version
```

**Databases:**
```powershell
mysql --version
psql --version
mongo --version
redis-cli --version
```

**AI Tools:**
```powershell
ollama --version
python -c "import torch; print(torch.__version__)"
python -c "import tensorflow; print(tensorflow.__version__)"
```

**Cloud Tools:**
```powershell
firebase --version
gcloud --version
aws --version
az --version
```

## Troubleshooting

### Common Installation Issues

#### Issue 1: Chocolatey Installation Fails

**Symptoms:**
- Error: "Unable to download Chocolatey installation script"
- Network errors

**Solutions:**
```powershell
# Try with TLS 1.2 explicitly
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Or install manually from https://chocolatey.org/install
```

#### Issue 2: PATH Not Updated

**Symptoms:**
- Commands not found after installation
- "is not recognized as an internal or external command"

**Solutions:**
```powershell
# Refresh PATH in current session
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Or restart PowerShell/Terminal

# Or restart computer (most reliable)
```

#### Issue 3: Permission Denied Errors

**Symptoms:**
- "Access denied" messages
- Installation fails partway through

**Solutions:**
```powershell
# Ensure running as Administrator
# Close antivirus temporarily
# Check file permissions on C:\ProgramData\chocolatey
```

#### Issue 4: Ollama Installation Fails

**Symptoms:**
- Cannot download Ollama
- Ollama not starting

**Solutions:**
```powershell
# Manual installation:
# 1. Visit https://ollama.ai/download
# 2. Download OllamaSetup.exe
# 3. Run the installer
# 4. Verify: ollama --version
```

#### Issue 5: Python/Node Package Installation Fails

**Symptoms:**
- pip or npm install errors
- SSL/TLS errors

**Solutions:**
```powershell
# For pip:
python -m pip install --upgrade pip
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name

# For npm:
npm config set strict-ssl false
npm install -g package-name
npm config set strict-ssl true
```

#### Issue 6: Disk Space Issues

**Symptoms:**
- Installation stops with disk space errors
- Computer running slow

**Solutions:**
```powershell
# Check disk space
Get-PSDrive C | Select-Object Used,Free

# Clean temporary files
Remove-Item $env:TEMP\* -Recurse -Force -ErrorAction SilentlyContinue

# Run Disk Cleanup
cleanmgr
```

### Getting Additional Help

1. **Check Installation Logs:**
   - Chocolatey logs: `C:\ProgramData\chocolatey\logs\chocolatey.log`
   
2. **Test Package Manager:**
   ```powershell
   choco --version
   choco list --local-only
   ```

3. **Verify Internet Connection:**
   ```powershell
   Test-Connection google.com -Count 2
   ```

4. **Check Windows Updates:**
   - Ensure Windows is up to date
   - Some tools require recent Windows updates

5. **Community Support:**
   - GitHub Issues
   - Stack Overflow
   - Tool-specific forums

## Post-Installation Steps

### 1. Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Install VS Code Extensions

```bash
code --install-extension ms-python.python
code --install-extension dbaeumer.vscode-eslint
code --install-extension ms-vscode.cpptools
code --install-extension rust-lang.rust-analyzer
```

### 3. Set Up Python Virtual Environments

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
myenv\Scripts\activate

# Install packages
pip install requests flask django
```

### 4. Configure Node.js Development

```bash
# Update npm
npm install -g npm

# Install global tools
npm install -g typescript nodemon eslint
```

### 5. Test Ollama (if installed)

```bash
# Pull a small model for testing
ollama pull tinyllama

# Run it
ollama run tinyllama

# Try a programming question
# Prompt: "Write a hello world in Python"
```

### 6. Set Up Firebase (if installed)

```bash
# Login
firebase login

# Initialize a project
firebase init
```

### 7. Create Your First Project

```bash
# Create project directory
mkdir my-first-project
cd my-first-project

# Initialize with Git
git init

# Create a README
echo "# My First Project" > README.md

# Make first commit
git add .
git commit -m "Initial commit"
```

## Maintenance

### Regular Updates

Run monthly to keep software up to date:

```powershell
# Update all Chocolatey packages
choco upgrade all -y

# Update Node.js packages
npm update -g

# Update Python packages
pip list --outdated
# Then update individually: pip install --upgrade package-name
```

### Backup Your Configuration

```powershell
# Backup VS Code settings
Copy-Item "$env:APPDATA\Code\User\settings.json" -Destination "backup-settings.json"

# Backup Git config
git config --list --show-origin
```

---

**Need more help?** Check the main [README.md](README.md) or open an issue on GitHub!