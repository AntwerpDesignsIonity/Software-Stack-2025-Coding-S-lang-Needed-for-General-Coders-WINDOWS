# Quick Start Guide

Get your complete development environment set up in minutes!

## 🚀 For Absolute Beginners

**1. Open PowerShell as Administrator**
   - Press `Windows Key + X`
   - Click "Windows PowerShell (Admin)" or "Terminal (Admin)"
   - Click "Yes" when Windows asks for permission

**2. Copy and paste this command:**
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/main/Install-SoftwareStack.ps1" -OutFile "$env:USERPROFILE\Downloads\Install-SoftwareStack.ps1"; Set-Location $env:USERPROFILE\Downloads; .\Install-SoftwareStack.ps1
```

**3. Follow the menu:**
   - Type `1` for Core Installation (most users)
   - Type `2` if you want AI tools like Ollama
   - Type `4` for everything

**4. Wait for installation** (30-60 minutes)

**5. Restart your computer**

**6. Done!** You now have a complete coding environment.

---

## 📋 What Did This Install?

### Core (Option 1):
- ✅ Git, VS Code, PowerShell, Windows Terminal
- ✅ Python, Node.js, Java, Rust, Go, PHP, Ruby
- ✅ MySQL, PostgreSQL, MongoDB, Redis
- ✅ Docker, Make, CMake, and more

### With AI (Option 2):
- ✅ Everything in Core
- ✅ **Ollama** - Run AI models locally (no cloud needed!)
- ✅ Python AI libraries (TensorFlow, PyTorch, etc.)

### With Cloud (Option 3):
- ✅ Everything in Core
- ✅ Firebase CLI, Google Cloud SDK
- ✅ AWS CLI, Azure CLI
- ✅ Android SDK

### Everything (Option 4):
- ✅ All of the above!

---

## 🎯 What Can I Do Now?

### Try Ollama (Local AI) - If you installed it:
```bash
# In PowerShell or Terminal:
ollama run llama2

# Ask it anything:
"Write a hello world program in Python"
```

### Create a Python Project:
```bash
# Create folder
mkdir my-python-project
cd my-python-project

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install packages
pip install requests flask

# Create a simple script
echo "print('Hello, World!')" > hello.py
python hello.py
```

### Create a Node.js Project:
```bash
# Create folder
mkdir my-node-project
cd my-node-project

# Initialize
npm init -y

# Install Express
npm install express

# Create app
echo "const express = require('express'); const app = express(); app.get('/', (req, res) => res.send('Hello World!')); app.listen(3000, () => console.log('Server running on http://localhost:3000'));" > app.js

# Run it
node app.js
```

### Open VS Code:
```bash
# Open current directory
code .

# Or open a specific folder
code C:\Users\YourName\Projects
```

---

## ✅ Verify Your Installation

Run these commands to check everything is working:

```powershell
# Core tools
git --version
python --version
node --version

# If you installed AI tools:
ollama --version

# If you installed Cloud tools:
firebase --version
```

---

## 🆘 Something Not Working?

### Commands Not Found?
**Restart your terminal!** Close PowerShell completely and open it again.

Still not working? **Restart your computer.**

### Installation Failed?
1. Make sure you ran as Administrator
2. Check your internet connection
3. Check you have at least 10GB free space
4. Try running just the core installation first

### Need More Help?
- See full [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for detailed troubleshooting
- Check [README.md](README.md) for complete documentation

---

## 📚 Next Steps

1. **Learn Git:**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. **Install VS Code Extensions:**
   - Python
   - JavaScript/TypeScript
   - GitLens
   - Prettier

3. **Try Building Something:**
   - Web app with Flask or Node.js
   - Data analysis with Python and Pandas
   - Chat with local AI using Ollama
   - Mobile app with Flutter

4. **Join Communities:**
   - GitHub
   - Stack Overflow
   - Reddit programming communities
   - Discord coding servers

---

## 🎓 Learning Resources

### For Beginners:
- **Python:** https://www.python.org/about/gettingstarted/
- **JavaScript:** https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- **Git:** https://git-scm.com/book/en/v2

### For Ollama/AI:
- **Ollama Docs:** https://ollama.ai/docs
- **Try CodeLlama:** `ollama run codellama` (AI for code)

### For Web Development:
- **Node.js Guides:** https://nodejs.org/en/docs/guides/
- **Flask Tutorial:** https://flask.palletsprojects.com/tutorial/
- **React:** https://react.dev/learn

---

**Congratulations! You're ready to start coding! 🎉**