# Ollama Guide - Local AI on Your Computer

## What is Ollama?

Ollama is a tool that lets you run large language models (AI) **locally on your own computer**. No cloud, no API keys, no subscriptions - everything runs on your machine privately.

## Why Use Ollama?

✅ **Privacy:** All AI processing happens on your computer  
✅ **No Cost:** Free to use, no API charges  
✅ **Offline:** Works without internet (after downloading models)  
✅ **Fast:** No network latency  
✅ **Control:** You own your data and models  

## Installation

If you used the installer with `-IncludeAI` or selected option 2, Ollama is already installed!

### Verify Installation

```powershell
ollama --version
```

If not installed, visit: https://ollama.ai/download

## Getting Started

### 1. Download Your First Model

```bash
# Download Llama 2 (recommended for beginners, ~4GB)
ollama pull llama2

# Or try a smaller model first (~0.6GB)
ollama pull tinyllama

# For coding assistance (~4GB)
ollama pull codellama
```

### 2. Start a Conversation

```bash
# Run Llama 2
ollama run llama2
```

Now you can chat with the AI:
```
>>> Write a Python function to calculate fibonacci numbers

>>> Explain how async/await works in JavaScript

>>> What's the best way to structure a React app?
```

Type `/bye` to exit.

## Available Models

### General Purpose Models

| Model | Size | Best For | Command |
|-------|------|----------|---------|
| **TinyLlama** | 0.6GB | Quick testing, low resources | `ollama run tinyllama` |
| **Llama 2** | 4GB | General use, good quality | `ollama run llama2` |
| **Mistral** | 4GB | High quality, efficient | `ollama run mistral` |
| **Llama 2 13B** | 8GB | Better quality (needs more RAM) | `ollama run llama2:13b` |

### Coding Models

| Model | Size | Best For | Command |
|-------|------|----------|---------|
| **CodeLlama** | 4GB | Code generation, debugging | `ollama run codellama` |
| **CodeLlama Python** | 4GB | Python-focused | `ollama run codellama:python` |

### Other Specialized Models

| Model | Best For | Command |
|-------|----------|---------|
| **Llama 2 Uncensored** | Fewer restrictions | `ollama run llama2-uncensored` |
| **Neural Chat** | Conversational AI | `ollama run neural-chat` |
| **Starling** | Long conversations | `ollama run starling-lm` |

See all models: https://ollama.ai/library

## Basic Commands

```bash
# List downloaded models
ollama list

# Download a model
ollama pull model-name

# Run a model
ollama run model-name

# Remove a model
ollama rm model-name

# Show model info
ollama show model-name

# Get help
ollama --help
```

## Using Ollama in Your Code

### Python Example

First, install the Ollama Python library:
```bash
pip install ollama
```

Then use it in your code:
```python
import ollama

# Simple chat
response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?'
        }
    ]
)

print(response['message']['content'])
```

### Streaming Responses

```python
import ollama

stream = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': 'Write a story'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

### Code Generation Example

```python
import ollama

def generate_code(prompt):
    response = ollama.chat(
        model='codellama',
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful programming assistant.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    return response['message']['content']

# Example usage
code = generate_code('Write a Python function to sort a list of dictionaries by a key')
print(code)
```

### JavaScript/Node.js Example

First, install the package:
```bash
npm install ollama
```

Then use it:
```javascript
import ollama from 'ollama'

// Simple chat
const response = await ollama.chat({
  model: 'llama2',
  messages: [{ role: 'user', content: 'Why is the sky blue?' }],
})

console.log(response.message.content)
```

### REST API (cURL)

Ollama runs a local API server on `http://localhost:11434`

```bash
# Generate text
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Why is the sky blue?",
  "stream": false
}'

# Chat completion
curl http://localhost:11434/api/chat -d '{
  "model": "llama2",
  "messages": [
    { "role": "user", "content": "Hello!" }
  ],
  "stream": false
}'
```

## Practical Use Cases

### 1. Code Assistant

```bash
ollama run codellama
>>> Fix this Python code: def add(a b): return a + b

>>> Explain what this does: [your code here]

>>> Convert this JavaScript to TypeScript: [code]
```

### 2. Learning & Explanations

```bash
ollama run llama2
>>> Explain REST APIs in simple terms

>>> What are the differences between SQL and NoSQL?

>>> How does Docker work?
```

### 3. Writing Assistant

```bash
ollama run llama2
>>> Write a README for a Python web scraper project

>>> Create commit messages for: Added user authentication

>>> Write API documentation for [function description]
```

### 4. Code Review

```bash
ollama run codellama
>>> Review this code for bugs: [paste code]

>>> Suggest improvements for this function: [code]

>>> Is this code secure? [code]
```

## Tips & Best Practices

### Performance Tips

1. **RAM Requirements:**
   - 4GB models need ~8GB RAM
   - 7GB models need ~16GB RAM
   - 13GB models need ~32GB RAM

2. **GPU Acceleration:**
   - Ollama automatically uses your GPU if available
   - NVIDIA GPUs work best
   - AMD GPU support is experimental

3. **Choose the Right Model:**
   - Start with `tinyllama` or `llama2:7b` for testing
   - Use `codellama` specifically for programming tasks
   - Try `mistral` for better quality with similar speed

### Quality Tips

1. **Be Specific:**
   ```bash
   # Bad
   >>> Write code
   
   # Good
   >>> Write a Python function that reads a CSV file and returns a pandas DataFrame
   ```

2. **Provide Context:**
   ```bash
   >>> I'm building a REST API with Flask. Write a function to validate email addresses.
   ```

3. **Use System Prompts (in code):**
   ```python
   messages = [
       {'role': 'system', 'content': 'You are an expert Python developer.'},
       {'role': 'user', 'content': 'How do I handle exceptions?'}
   ]
   ```

### Managing Storage

Models can be large. Check your downloaded models:

```bash
# List models and their sizes
ollama list

# Remove unused models
ollama rm model-name

# Model locations:
# Windows: C:\Users\YourName\.ollama\models
```

## Troubleshooting

### Ollama Not Starting

```powershell
# Check if Ollama service is running
Get-Process ollama

# Restart Ollama
# Close Ollama from system tray and restart it
```

### Model Download Fails

```bash
# Try pulling again
ollama pull model-name

# Or download from website manually
# Visit: https://ollama.ai/library
```

### Out of Memory Errors

Try a smaller model:
```bash
# Instead of llama2:13b, use:
ollama run llama2:7b

# Or use the smallest:
ollama run tinyllama
```

### Slow Performance

1. Close other applications to free RAM
2. Use a smaller model
3. Check if GPU is being used (NVIDIA GPUs are fastest)
4. Reduce context length in API calls

### Port Already in Use

```powershell
# Find process using port 11434
netstat -ano | findstr :11434

# Kill the process (replace PID)
taskkill /F /PID <PID>
```

## Advanced Usage

### Custom Model Parameters

```python
import ollama

response = ollama.generate(
    model='llama2',
    prompt='Write a poem',
    options={
        'temperature': 0.8,  # Higher = more creative (0-1)
        'top_p': 0.9,       # Nucleus sampling
        'top_k': 40,        # Top-k sampling
        'num_predict': 200  # Max tokens to generate
    }
)
```

### Creating a Chatbot

```python
import ollama

conversation_history = []

def chat(user_message):
    conversation_history.append({
        'role': 'user',
        'content': user_message
    })
    
    response = ollama.chat(
        model='llama2',
        messages=conversation_history
    )
    
    assistant_message = response['message']
    conversation_history.append(assistant_message)
    
    return assistant_message['content']

# Usage
print(chat("Hello! What's your name?"))
print(chat("Can you help me with Python?"))
```

### Building a VS Code Extension

You can integrate Ollama into VS Code for inline code assistance. Check out the Ollama extensions in VS Code marketplace.

## Comparison with Cloud AI

| Feature | Ollama (Local) | Cloud AI (OpenAI, etc.) |
|---------|----------------|-------------------------|
| Privacy | ✅ Fully private | ❌ Data sent to cloud |
| Cost | ✅ Free | ❌ Pay per token |
| Speed | ⚡ Fast (local) | 🐌 Network latency |
| Internet | ✅ Works offline | ❌ Requires internet |
| Quality | 🟨 Good | ✅ Best |
| Setup | 🟨 Download models | ✅ Just API key |

## Resources

- **Official Website:** https://ollama.ai
- **Documentation:** https://ollama.ai/docs
- **Model Library:** https://ollama.ai/library
- **GitHub:** https://github.com/ollama/ollama
- **Discord Community:** https://discord.gg/ollama

## Example Projects

### 1. Code Reviewer CLI

```python
import ollama
import sys

def review_code(code):
    response = ollama.chat(
        model='codellama',
        messages=[
            {
                'role': 'system',
                'content': 'You are a code reviewer. Identify bugs, suggest improvements, and check for security issues.'
            },
            {
                'role': 'user',
                'content': f'Review this code:\n\n{code}'
            }
        ]
    )
    return response['message']['content']

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python code_reviewer.py <file.py>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    
    print(review_code(code))
```

### 2. Documentation Generator

```python
import ollama

def generate_docs(function_code):
    response = ollama.chat(
        model='codellama',
        messages=[
            {
                'role': 'user',
                'content': f'Generate detailed documentation for this function:\n\n{function_code}'
            }
        ]
    )
    return response['message']['content']

# Example
code = """
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
"""

print(generate_docs(code))
```

### 3. Commit Message Generator

```python
import ollama
import subprocess

def get_git_diff():
    return subprocess.check_output(['git', 'diff', '--staged']).decode('utf-8')

def generate_commit_message():
    diff = get_git_diff()
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'user',
                'content': f'Generate a concise commit message for these changes:\n\n{diff[:2000]}'
            }
        ]
    )
    
    return response['message']['content']

if __name__ == '__main__':
    print(generate_commit_message())
```

---

**Start experimenting with AI on your local machine today!** 🚀

Need help? Check the [main README](README.md) or visit https://ollama.ai/docs