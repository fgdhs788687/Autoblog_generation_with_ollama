# 📰 AI Auto Blog Generator

An AI-powered blog generator that scrapes website content and automatically creates a blog post with a generated title using a local LLM via Ollama.

---

## 🚀 Features

* 🌐 Scrapes text content from any public URL
* 🤖 Generates a 200-word blog post using `gemma3:1b`
* 🏷 Automatically creates a short blog title
* 💾 Saves output to an `autoblog.html` file
* 🔁 Continuously accepts URLs until `exit()` is entered

---

## 🛠 Tech Stack

* Python
* requests
* BeautifulSoup
* Ollama (Local LLM)
* HTML

---

## 📦 Requirements

Install required Python packages:

```bash
pip install requests beautifulsoup4 ollama
```

Make sure Ollama is installed and pull the required model:

```bash
ollama pull gemma3:1b
```

---

## ▶️ How It Works

1. User enters a URL.
2. The program:

   * Scrapes all `<p>` tag content from the page.
   * Sends the scraped text to the LLM.
   * Generates:

     * A 200-word blog post
     * A short blog title
3. The result is appended to `autoblog.html`.
4. The program repeats until the user types:

```bash
exit()
```

---

## 📁 Output Format

Each blog post is saved in the following structure:

```html
<article>
    <h1>Generated Title</h1>
    <p>Generated Blog Post</p>
    <hr>
</article>
```

---

## 🧠 Example Usage

```bash
url: https://example.com
```

The program will:

* Print the generated title
* Print the generated blog post
* Save it inside `autoblog.html`

---

## ⚠️ Limitations

* Some websites that load content dynamically with JavaScript (e.g., South China Morning Post) may not scrape properly because `requests` does not execute JavaScript.
* Works best on static HTML websites (e.g., Gizmodo).
* Large pages may generate very long prompts, which can affect performance.

---

## 🔮 Future Improvements

* Extract only main article content instead of all `<p>` tags
* Add CSS styling to improve blog appearance
* Convert into a Flask web application
* Add proper error handling for invalid URLs
* Add summarization before blog generation
* Deploy as a web application

---

## 🧑‍💻 Author

**Md Faizal Razza**
Aspiring Data Scientist & AI Developer

---

## 📜 License

This project is open-source and available under the MIT License.



