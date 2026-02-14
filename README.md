# 📰 AI Auto Blog Generator

An AI-powered blog generator that scrapes website content and automatically creates a blog post with a generated title using a local LLM via Ollama.

## 🚀 Features
1. 🌐 Scrapes text content from any public URL
2. 🤖 Generates a 200-word blog post using gemma3:1b
3. 🏷 Automatically creates a short blog title
4. 💾 Saves output to an autoblog.html file
5. 🔁 Continuously accepts URLs until exit() is entered

## 🛠 Tech Stack
- Python
- requests
- BeautifulSoup
- ollama (local LLM)
- HTML

## 📦 Requirements
- Install required packages:
-     pip install requests beautifulsoup4 ollama
- Make sure you have Ollama installed and the model pulled:
-     ollama pull gemma3:1b

## ▶️ How It Works
1. User enters a URL
2. The program:
   1. Scrapes all <p> tag content
   2. Sends scraped text to the LLM
   3. Generates:
     1. A blog post (200 words)
     2. A short title
3. Appends the result to autoblog.html
4. Repeats until exit() is entered

## 🧠 Example Usage
    url: https://example.com


