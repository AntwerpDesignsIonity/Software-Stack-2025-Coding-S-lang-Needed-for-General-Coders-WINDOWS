# Software Stack 2025 - Complete Coding Environment for Windows

**Automated installer for a comprehensive development environment on Windows systems**

A complete, automated software stack installer designed for fresh Windows installations. This installer provides everything general coders need, from core development tools to optional AI platforms like Ollama.

## 🚀 Quick Start

### Prerequisites

- **Windows 10 or Windows 11** (64-bit)
- **PowerShell 5.1 or higher** (comes with Windows)
- **Administrator privileges**
- **Stable internet connection** (installations download packages from the internet)
- **At least 10GB of free disk space** (more recommended for full installation)

### One-Command Installation

**For Interactive Menu (Recommended for first-time users):**

> ⚠️ **Security Note:** Always verify the source before running remote scripts. Review the script content first if security is a concern.

```powershell
# Option 1: Download first, then review and run (Recommended)
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/main/Install-SoftwareStack.ps1" -OutFile "Install-SoftwareStack.ps1"
# Review the file, then run:
.\Install-SoftwareStack.ps1

# Option 2: Direct execution (only if you trust the source)
Set-ExecutionPolicy Bypass -Scope Process -Force; iwr -useb https://raw.githubusercontent.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/main/Install-SoftwareStack.ps1 | iex
```

**For Direct Installation with AI Tools:**
```powershell
# Run this in PowerShell as Administrator:
.\Install-SoftwareStack.ps1 -IncludeAI
```

**For Complete Installation (Everything):**
```powershell
# Run this in PowerShell as Administrator:
.\Install-SoftwareStack.ps1 -All
```

## 📦 What's Included

### Core Development Tools (Always Installed)

- **Git** - Version control system
- **Visual Studio Code** - Code editor
- **PowerShell Core** - Modern PowerShell
- **Windows Terminal** - Modern terminal application
- **Postman** - API testing tool
- **Docker Desktop** - Containerization platform
- **Make** / **CMake** - Build automation tools
- **cURL** / **Wget** - Command-line data transfer
- **Vim** / **Notepad++** - Text editors

### Programming Languages & Runtimes

- **Python 3.x** - With pip package manager
- **Node.js LTS** - With npm package manager
- **Java OpenJDK** - Latest stable version
- **Rust** - Systems programming language
- **Go (Golang)** - Google's programming language
- **PHP** - Server-side scripting
- **Ruby** - Dynamic programming language
- **C/C++** - Via Visual Studio Build Tools
- **C#** - With .NET SDK
- **Kotlin** - JVM language
- **Lua** - Lightweight scripting
- **Dart** - Flutter and web development
- **Scala** - JVM functional language
- **Perl** - Text processing language
- **TypeScript** - JavaScript with types
- **Swift** - Apple's programming language (Windows support)

### Web Development

- **HTML5/CSS3** - Built into browsers
- **JavaScript/TypeScript** - With Node.js
- **Flask** - Python web framework
- **Django** - Python web framework
- **Sass/Less** - CSS preprocessors

### Databases & SQL

- **MySQL** - Relational database
- **PostgreSQL** - Advanced relational database
- **SQLite** - Lightweight database
- **MongoDB** - NoSQL document database
- **Redis** - In-memory data store

### 🤖 AI & Machine Learning Tools (Optional)

Install with `-IncludeAI` flag or select option 2 in menu.

- **Ollama** - Run AI models locally (Llama 2, Mistral, etc.)
- **Python AI Libraries:**
  - NumPy - Numerical computing
  - Pandas - Data analysis
  - Scikit-learn - Machine learning
  - TensorFlow - Deep learning
  - PyTorch - Deep learning
  - Transformers - NLP models

**Getting Started with Ollama:**
```bash
# After installation, run:
ollama run llama2

# Or try other models:
ollama run mistral
ollama run codellama
```

### ☁️ Cloud SDKs & Tools (Optional)

Install with `-IncludeCloud` flag or select option 3 in menu.

- **Firebase CLI** - Google's mobile/web platform
- **Google Cloud SDK** - GCP development tools
- **AWS CLI** - Amazon Web Services tools
- **Azure CLI** - Microsoft Azure tools
- **Android SDK** - Android app development

## 💻 Installation Guide

### Method 1: Interactive Menu (Recommended)

1. **Open PowerShell as Administrator**
   - Right-click Windows Start button
   - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"

2. **Download and run the installer:**
   ```powershell
   # Download the installer
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/main/Install-SoftwareStack.ps1" -OutFile "Install-SoftwareStack.ps1"
   
   # Run the installer
   .\Install-SoftwareStack.ps1
   ```

3. **Follow the interactive menu** to select what you want to install

### Method 2: Command-Line Installation

**Core Installation Only:**
```powershell
.\Install-SoftwareStack.ps1
```

**Core + AI Tools (with Ollama):**
```powershell
.\Install-SoftwareStack.ps1 -IncludeAI
```

**Core + Cloud SDKs:**
```powershell
.\Install-SoftwareStack.ps1 -IncludeCloud
```

**Complete Installation (Everything):**
```powershell
.\Install-SoftwareStack.ps1 -All
```

### Method 3: Clone Repository

```powershell
# Clone the repository
git clone https://github.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS.git

# Navigate to directory
cd Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS

# Run installer
.\Install-SoftwareStack.ps1
```

## ⚙️ Installation Process

The installer will:

1. ✅ Check for Administrator privileges
2. ✅ Install Chocolatey package manager (if not present)
3. ✅ Install Scoop package manager (if not present)
4. ✅ Install core development tools
5. ✅ Install programming languages and runtimes
6. ✅ Install databases
7. ✅ Install web development tools
8. ✅ Install AI tools (if selected)
9. ✅ Install cloud SDKs (if selected)
10. ✅ Update system PATH variables

**Estimated Time:** 30-60 minutes (depending on internet speed and selections)

## 🔍 Post-Installation Verification

After installation completes, **restart your terminal** and verify installations:

```powershell
# Check core tools
git --version
code --version
python --version
node --version

# Check languages
java --version
rustc --version
go version
php --version
ruby --version

# Check databases
mysql --version
psql --version

# Check AI tools (if installed)
ollama --version

# Check cloud tools (if installed)
firebase --version
gcloud --version
aws --version
```

## 🛠️ Troubleshooting

### Common Issues

**1. "Execution Policy" Error**
```powershell
# Run this first:
Set-ExecutionPolicy Bypass -Scope Process -Force
```

**2. "Not Running as Administrator"**
- Right-click PowerShell and select "Run as Administrator"

**3. Chocolatey Installation Fails**
- Check your internet connection
- Temporarily disable antivirus
- Try running: `choco --version` to see if it's already installed

**4. PATH Not Updated**
- Restart your terminal or computer
- Manually refresh PATH:
  ```powershell
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  ```

**5. Ollama Not Starting**
- Visit https://ollama.ai for manual installation
- Ensure you have sufficient disk space (AI models are large)

**6. Node.js or npm Issues**
- Run: `npm install -g npm` to update npm
- Check Node.js installation: `node --version`

### Getting Help

- Check installation logs in PowerShell output
- Visit package websites for specific software issues
- For Ollama issues: https://ollama.ai/docs
- For Chocolatey issues: https://chocolatey.org/docs

## 📚 Using Your New Environment

### Python Development

```bash
# Create virtual environment
python -m venv myproject
myproject\Scripts\activate

# Install packages
pip install requests flask
```

### Node.js Development

```bash
# Create new project
npm init -y

# Install packages
npm install express
```

### AI/ML with Ollama

```bash
# List available models
ollama list

# Download and run a model
ollama run llama2

# Use in your code (Python example)
pip install ollama
```

```python
import ollama
response = ollama.chat(model='llama2', messages=[
  {'role': 'user', 'content': 'Why is the sky blue?'}
])
print(response['message']['content'])
```

### Firebase Development

```bash
# Login to Firebase
firebase login

# Initialize project
firebase init

# Deploy
firebase deploy
```

## 🔄 Updating Software

### Update All Chocolatey Packages
```powershell
choco upgrade all -y
```

### Update Specific Tools
```powershell
choco upgrade python -y
choco upgrade nodejs -y
choco upgrade git -y
```

### Update npm Packages
```bash
npm update -g
```

### Update pip Packages
```bash
pip list --outdated
pip install --upgrade package-name
```

## 🗑️ Uninstallation

To remove installed software:

```powershell
# Uninstall specific package
choco uninstall package-name -y

# List installed packages
choco list --local-only
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Support

If this installer helped you set up your development environment, please consider giving it a star!

## 📞 Contact & Issues

- Report issues on GitHub: [Issues Page](https://github.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/issues)
- For questions about specific software, please refer to their official documentation

## 🎯 Roadmap

- [ ] Linux installation script
- [ ] macOS installation script
- [ ] More AI tools integration (LocalAI, LM Studio)
- [ ] IDE configurations included
- [ ] Development environment profiles (Web Dev, Mobile Dev, Data Science, etc.)

---

**Made with ❤️ for developers who want to get started quickly**
