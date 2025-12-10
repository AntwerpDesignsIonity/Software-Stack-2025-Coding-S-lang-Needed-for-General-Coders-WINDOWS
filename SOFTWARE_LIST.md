# Complete Software List & Descriptions

This document provides detailed information about every piece of software included in the stack.

## Table of Contents

- [Package Managers](#package-managers)
- [Core Development Tools](#core-development-tools)
- [Programming Languages](#programming-languages)
- [Web Development](#web-development)
- [Databases](#databases)
- [AI & Machine Learning](#ai--machine-learning)
- [Cloud SDKs](#cloud-sdks)
- [Additional Tools](#additional-tools)

---

## Package Managers

### Chocolatey
- **Website:** https://chocolatey.org
- **Description:** The package manager for Windows. Similar to apt for Ubuntu or brew for macOS.
- **Why Included:** Automates software installation and updates on Windows
- **Usage:** `choco install package-name`

### Scoop
- **Website:** https://scoop.sh
- **Description:** Command-line installer for Windows focusing on portable apps
- **Why Included:** Provides additional packages not in Chocolatey
- **Usage:** `scoop install package-name`

---

## Core Development Tools

### Git
- **Website:** https://git-scm.com
- **Description:** Distributed version control system
- **Why Included:** Essential for source code management and collaboration
- **Key Features:**
  - Version control
  - Branching and merging
  - GitHub/GitLab integration
- **Usage:** `git clone`, `git commit`, `git push`

### Visual Studio Code
- **Website:** https://code.visualstudio.com
- **Description:** Lightweight but powerful source code editor
- **Why Included:** Most popular code editor with extensive extension ecosystem
- **Key Features:**
  - IntelliSense
  - Debugging
  - Git integration
  - Extensions for all languages
- **Usage:** `code .` to open current directory

### PowerShell Core
- **Website:** https://github.com/PowerShell/PowerShell
- **Description:** Cross-platform task automation and configuration management framework
- **Why Included:** Modern scripting environment for Windows
- **Key Features:**
  - Scripting and automation
  - Cross-platform (Windows, Linux, macOS)
  - Rich object manipulation
- **Usage:** `pwsh` to start PowerShell Core

### Windows Terminal
- **Website:** https://github.com/microsoft/terminal
- **Description:** Modern, fast, efficient terminal application
- **Why Included:** Better terminal experience with tabs, themes, and customization
- **Key Features:**
  - Multiple tabs
  - Custom themes
  - GPU acceleration
  - Multiple profiles (PowerShell, CMD, WSL)

### Postman
- **Website:** https://www.postman.com
- **Description:** API development and testing platform
- **Why Included:** Essential for API development and testing
- **Key Features:**
  - API testing
  - Request collections
  - Environment variables
  - Automated testing

### Docker Desktop
- **Website:** https://www.docker.com/products/docker-desktop
- **Description:** Containerization platform for Windows
- **Why Included:** Modern deployment and development environment
- **Key Features:**
  - Container management
  - Kubernetes support
  - Easy microservices development
- **Usage:** `docker run`, `docker build`

---

## Programming Languages

### Python
- **Website:** https://www.python.org
- **Description:** High-level, interpreted programming language
- **Why Included:** Most versatile language for web, data science, AI, automation
- **Key Features:**
  - Easy to learn
  - Extensive libraries (pip)
  - Data science and AI ecosystem
  - Web frameworks (Flask, Django)
- **Usage:** `python script.py`
- **Package Manager:** `pip install package-name`

### Node.js
- **Website:** https://nodejs.org
- **Description:** JavaScript runtime built on Chrome's V8 engine
- **Why Included:** Essential for modern web development
- **Key Features:**
  - JavaScript on server-side
  - Huge package ecosystem (npm)
  - Async I/O
  - Real-time applications
- **Usage:** `node app.js`
- **Package Manager:** `npm install package-name`

### Java (OpenJDK)
- **Website:** https://openjdk.org
- **Description:** Open-source implementation of Java Platform
- **Why Included:** Enterprise development, Android apps, cross-platform
- **Key Features:**
  - Object-oriented
  - Platform independent
  - Large enterprise ecosystem
  - Android development
- **Usage:** `java ClassName` or `javac ClassName.java`
- **Package Manager:** Maven, Gradle

### Rust
- **Website:** https://www.rust-lang.org
- **Description:** Systems programming language focused on safety and performance
- **Why Included:** Memory-safe systems programming without garbage collection
- **Key Features:**
  - Memory safety without GC
  - Zero-cost abstractions
  - Concurrency without data races
  - Growing ecosystem
- **Usage:** `rustc main.rs` or `cargo build`
- **Package Manager:** `cargo install package-name`

### Go (Golang)
- **Website:** https://golang.org
- **Description:** Statically typed, compiled language designed at Google
- **Why Included:** Cloud-native development, microservices, CLI tools
- **Key Features:**
  - Fast compilation
  - Built-in concurrency
  - Simple syntax
  - Excellent standard library
- **Usage:** `go run main.go` or `go build`
- **Package Manager:** `go get package-name`

### PHP
- **Website:** https://www.php.net
- **Description:** Server-side scripting language
- **Why Included:** Powers most web servers, WordPress, Laravel
- **Key Features:**
  - Web development focus
  - Large hosting support
  - Frameworks (Laravel, Symfony)
  - Database integration
- **Usage:** `php script.php`
- **Package Manager:** Composer

### Ruby
- **Website:** https://www.ruby-lang.org
- **Description:** Dynamic, object-oriented scripting language
- **Why Included:** Ruby on Rails, scripting, web development
- **Key Features:**
  - Elegant syntax
  - Ruby on Rails framework
  - Strong community
  - Scripting and automation
- **Usage:** `ruby script.rb`
- **Package Manager:** `gem install package-name`

### C/C++
- **Website:** https://docs.microsoft.com/en-us/cpp/
- **Description:** High-performance compiled languages
- **Why Included:** Systems programming, game development, performance-critical apps
- **Key Features:**
  - Direct hardware access
  - Maximum performance
  - Game engines (Unreal, Unity)
  - Operating systems
- **Usage:** Visual Studio Build Tools (MSVC)
- **Compiler:** `cl` (MSVC)

### C# (.NET)
- **Website:** https://dotnet.microsoft.com
- **Description:** Modern, object-oriented language for .NET
- **Why Included:** Windows apps, Unity game development, enterprise
- **Key Features:**
  - .NET ecosystem
  - Unity game engine
  - Cross-platform (.NET Core)
  - Strong typing
- **Usage:** `dotnet run`
- **Package Manager:** NuGet

### Kotlin
- **Website:** https://kotlinlang.org
- **Description:** Modern language for JVM, Android, and more
- **Why Included:** Android development, modern JVM alternative
- **Key Features:**
  - Interoperable with Java
  - Null safety
  - Android official language
  - Concise syntax
- **Usage:** `kotlinc file.kt` or Android Studio

### Lua
- **Website:** https://www.lua.org
- **Description:** Lightweight, embeddable scripting language
- **Why Included:** Game scripting, embedded systems
- **Key Features:**
  - Fast execution
  - Small footprint
  - Easy to embed
  - Game development (Roblox, Love2D)
- **Usage:** `lua script.lua`

### Dart
- **Website:** https://dart.dev
- **Description:** Client-optimized language for fast apps
- **Why Included:** Flutter mobile development
- **Key Features:**
  - Flutter framework
  - Optimized for UI
  - AOT and JIT compilation
  - Mobile and web development
- **Usage:** `dart run` or Flutter

### Scala
- **Website:** https://www.scala-lang.org
- **Description:** Multi-paradigm language for JVM
- **Why Included:** Big data (Apache Spark), functional programming
- **Key Features:**
  - Functional and OOP
  - Type safety
  - Apache Spark
  - Concurrency
- **Usage:** `scala script.scala`

### Perl
- **Website:** https://www.perl.org
- **Description:** High-level, general-purpose scripting language
- **Why Included:** Text processing, legacy systems, system administration
- **Key Features:**
  - Text processing
  - Regular expressions
  - System administration
  - CPAN modules
- **Usage:** `perl script.pl`

### Swift
- **Website:** https://swift.org
- **Description:** Apple's modern programming language
- **Why Included:** iOS/macOS development (Windows toolchain available)
- **Key Features:**
  - Modern syntax
  - Safe and fast
  - Apple ecosystem
  - Growing cross-platform support
- **Usage:** `swift run` (experimental on Windows)

---

## Web Development

### TypeScript
- **Website:** https://www.typescriptlang.org
- **Description:** Typed superset of JavaScript
- **Why Included:** Type-safe JavaScript development
- **Installation:** `npm install -g typescript`
- **Key Features:**
  - Static typing
  - Better IDE support
  - Large-scale application development
  - Compiles to JavaScript
- **Usage:** `tsc file.ts`

### Flask
- **Website:** https://flask.palletsprojects.com
- **Description:** Lightweight Python web framework
- **Why Included:** Quick API and web app development
- **Installation:** `pip install flask`
- **Key Features:**
  - Micro-framework
  - Easy to learn
  - RESTful APIs
  - Extensible
- **Usage:** Create app.py and run with `python app.py`

### Django
- **Website:** https://www.djangoproject.com
- **Description:** High-level Python web framework
- **Why Included:** Full-featured web development
- **Installation:** `pip install django`
- **Key Features:**
  - Batteries included
  - ORM
  - Admin interface
  - Security features
- **Usage:** `django-admin startproject myproject`

### Sass
- **Website:** https://sass-lang.com
- **Description:** CSS preprocessor
- **Why Included:** Advanced CSS with variables, nesting, mixins
- **Installation:** `npm install -g sass`
- **Key Features:**
  - Variables
  - Nesting
  - Mixins
  - Functions
- **Usage:** `sass input.scss output.css`

### Less
- **Website:** https://lesscss.org
- **Description:** CSS preprocessor
- **Why Included:** Alternative to Sass for CSS enhancement
- **Installation:** `npm install -g less`
- **Key Features:**
  - Variables
  - Mixins
  - Functions
  - JavaScript evaluation
- **Usage:** `lessc input.less output.css`

---

## Databases

### MySQL
- **Website:** https://www.mysql.com
- **Description:** Popular open-source relational database
- **Why Included:** Most popular SQL database, web hosting standard
- **Key Features:**
  - ACID compliance
  - Replication
  - Large community
  - Web hosting standard
- **Usage:** `mysql -u root -p`

### PostgreSQL
- **Website:** https://www.postgresql.org
- **Description:** Advanced open-source relational database
- **Why Included:** Feature-rich, standards-compliant SQL database
- **Key Features:**
  - Advanced SQL features
  - JSON support
  - Full-text search
  - Extensible
- **Usage:** `psql -U postgres`

### SQLite
- **Website:** https://www.sqlite.org
- **Description:** Self-contained SQL database engine
- **Why Included:** Lightweight, serverless database for development
- **Key Features:**
  - No server needed
  - Single file
  - Embedded in applications
  - Zero configuration
- **Usage:** `sqlite3 database.db`

### MongoDB
- **Website:** https://www.mongodb.com
- **Description:** NoSQL document database
- **Why Included:** Popular NoSQL option, flexible schema
- **Key Features:**
  - Document-oriented
  - Flexible schema
  - Horizontal scaling
  - JSON-like documents
- **Usage:** `mongo` or `mongosh`

### Redis
- **Website:** https://redis.io
- **Description:** In-memory data structure store
- **Why Included:** Caching, session storage, real-time applications
- **Key Features:**
  - In-memory performance
  - Pub/sub messaging
  - Caching
  - Session storage
- **Usage:** `redis-cli`

---

## AI & Machine Learning

### Ollama
- **Website:** https://ollama.ai
- **Description:** Run large language models locally
- **Why Included:** Privacy-focused local AI, no cloud required
- **Key Features:**
  - Run AI models locally
  - No API keys or cloud
  - Multiple models (Llama 2, Mistral, CodeLlama)
  - Privacy-focused
- **Usage:** `ollama run llama2`
- **Popular Models:**
  - `llama2` - General purpose AI
  - `mistral` - Fast and capable
  - `codellama` - Code generation
  - `tinyllama` - Lightweight model

### NumPy
- **Website:** https://numpy.org
- **Description:** Fundamental package for scientific computing in Python
- **Why Included:** Foundation for all Python data science and AI
- **Installation:** `pip install numpy`
- **Key Features:**
  - N-dimensional arrays
  - Mathematical functions
  - Linear algebra
  - Random number generation

### Pandas
- **Website:** https://pandas.pydata.org
- **Description:** Data manipulation and analysis library
- **Why Included:** Essential for data analysis and preprocessing
- **Installation:** `pip install pandas`
- **Key Features:**
  - DataFrame structures
  - Data cleaning
  - Time series analysis
  - CSV/Excel handling

### Scikit-learn
- **Website:** https://scikit-learn.org
- **Description:** Machine learning library for Python
- **Why Included:** Traditional ML algorithms and tools
- **Installation:** `pip install scikit-learn`
- **Key Features:**
  - Classification
  - Regression
  - Clustering
  - Model selection

### TensorFlow
- **Website:** https://www.tensorflow.org
- **Description:** End-to-end open-source ML platform by Google
- **Why Included:** Deep learning and neural networks
- **Installation:** `pip install tensorflow`
- **Key Features:**
  - Deep learning
  - Neural networks
  - Production deployment
  - TensorBoard visualization

### PyTorch
- **Website:** https://pytorch.org
- **Description:** Deep learning framework by Meta
- **Why Included:** Research-friendly deep learning
- **Installation:** `pip install torch`
- **Key Features:**
  - Dynamic computation graphs
  - Research-friendly
  - Strong GPU support
  - Growing ecosystem

### Transformers
- **Website:** https://huggingface.co/transformers
- **Description:** State-of-the-art NLP models
- **Why Included:** Access to latest NLP models (BERT, GPT, etc.)
- **Installation:** `pip install transformers`
- **Key Features:**
  - Pre-trained models
  - Text generation
  - Translation
  - Question answering

---

## Cloud SDKs

### Firebase CLI
- **Website:** https://firebase.google.com
- **Description:** Google's mobile and web application platform
- **Why Included:** Backend services, hosting, real-time database
- **Installation:** `npm install -g firebase-tools`
- **Key Features:**
  - Hosting
  - Real-time database
  - Authentication
  - Cloud functions
- **Usage:** `firebase init`, `firebase deploy`

### Google Cloud SDK
- **Website:** https://cloud.google.com/sdk
- **Description:** Tools for Google Cloud Platform
- **Why Included:** GCP service management and deployment
- **Key Features:**
  - Compute Engine
  - Cloud Storage
  - BigQuery
  - Kubernetes Engine
- **Usage:** `gcloud init`, `gcloud compute instances list`

### AWS CLI
- **Website:** https://aws.amazon.com/cli
- **Description:** Command-line interface for Amazon Web Services
- **Why Included:** AWS resource management
- **Key Features:**
  - EC2 management
  - S3 storage
  - Lambda functions
  - RDS databases
- **Usage:** `aws configure`, `aws s3 ls`

### Azure CLI
- **Website:** https://docs.microsoft.com/en-us/cli/azure
- **Description:** Command-line interface for Microsoft Azure
- **Why Included:** Azure resource management
- **Key Features:**
  - Virtual machines
  - App Service
  - SQL Database
  - Storage accounts
- **Usage:** `az login`, `az vm list`

### Android SDK
- **Website:** https://developer.android.com/studio
- **Description:** Android development tools
- **Why Included:** Android app development and testing
- **Key Features:**
  - Android emulator
  - Build tools
  - Platform tools
  - Debug tools
- **Usage:** Use with Android Studio or command-line

---

## Additional Tools

### Make / CMake
- **Description:** Build automation tools
- **Why Included:** Compiling C/C++ projects
- **Usage:** `make` or `cmake`

### Wget / cURL
- **Description:** Command-line download tools
- **Why Included:** Download files from command line
- **Usage:** `wget url` or `curl url`

### jq
- **Description:** JSON processor for command line
- **Why Included:** Parse and manipulate JSON data
- **Usage:** `echo '{"key":"value"}' | jq`

### Vim
- **Description:** Text editor
- **Why Included:** Terminal-based editing
- **Usage:** `vim file.txt`

### Notepad++
- **Description:** Source code editor
- **Why Included:** Advanced text editing for Windows
- **Usage:** Launch from Start menu

### VirtualBox
- **Description:** Virtualization software
- **Why Included:** Run other operating systems
- **Usage:** Launch from Start menu

### Vagrant
- **Description:** Virtual machine management
- **Why Included:** Develop in virtual environments
- **Usage:** `vagrant init`, `vagrant up`

---

## Quick Reference: When to Use What

| Task | Recommended Tool |
|------|-----------------|
| Web Backend | Node.js, Python (Flask/Django), PHP |
| Mobile Apps | Kotlin/Java (Android), Dart (Flutter) |
| Data Science | Python (NumPy, Pandas, Scikit-learn) |
| AI/ML | Python (TensorFlow, PyTorch, Ollama) |
| Systems Programming | Rust, C/C++, Go |
| Cloud Development | Python, Node.js, Go + Cloud SDKs |
| Game Development | C++ (Unreal), C# (Unity), Lua |
| Scripting | Python, PowerShell, Bash |
| Local AI | Ollama (privacy-focused, no cloud) |
| API Development | Node.js (Express), Python (Flask), Go |
| DevOps | Docker, Kubernetes, Cloud CLIs |

---

**Note:** This list represents the full software stack. Choose what you need based on your development goals!