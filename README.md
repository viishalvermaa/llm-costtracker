# 🚀 costtracker

<p align="center">
  <b>Track your LLM API cost in real time — with one line of code.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/status-active-success.svg" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" />
  <img src="https://img.shields.io/badge/built%20with-GenAI-purple.svg" />
</p>

---

## ✨ Why costtracker?

Building with LLMs is easy.  
**Tracking cost isn’t.**

costtracker solves this by giving you:

> ⚡ Instant cost visibility for every API call

No dashboards. No setup. No complexity.

---

## 🔥 Features

- 📊 Real-time token + cost tracking  
- ⚡ One-line integration (`track(response)`)  
- 🧠 Works with OpenAI-compatible APIs for now (Gemini included)  
- 🪶 Lightweight & zero-config  
- 🧱 Built for developers  

---

## ⚡ Quick Demo

```python
from costtracker import track

track(response)
```

## ⚡ Output
```
Model: gemini-2.5-flash-lite
Tokens: 13 (input: 4, output: 9)
Cost: $0.000011
```

## 📦 Installation
```
pip install -e .
```

## ⚙️ Setup

Create a .env file in your root directory:
```.env
GEMINI_API_KEY=your_api_key_here
```

## 🧪 Usage
```python
import os
from dotenv import load_dotenv
from openai import OpenAI
from costtracker import track

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {"role": "user", "content": "Hello there!"}
    ]
)

track(response)
```

## 💡 Use Cases

- 🧑‍💻 AI app developers tracking API usage
- 🚀 Startup teams controlling LLM costs
- 📊 Experimentation with prompt optimization
- 🧪 GenAI project building

## 🤝 Contributing

- Contributions are welcome!
- Feel free to open issues or submit PRs.

## ⭐ If you like this project

**Give it a star**

## 📄 License

MIT License