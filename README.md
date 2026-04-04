# 🚀 costtracker

<p align="center">
  <b>Track your LLM API cost in your terminal in real time — with one command.</b>
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

- 📊 Real-time cost tracking  
- ⚡ One-line integration  
- 🧠 Works with OpenAI and Gemini models (present)  
- 🪶 Lightweight & zero-config  
- 🧱 Built for developers  

---

## ⚡ Quick Demo

```python
pip install costtracker

costtracker run file.py
```

## ⚡ Output
```
Model: gemini-2.5-flash-lite
Tokens: 13 (input: 4, output: 9)
Cost: $0.000011
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
from costtracker import track
from google import genai

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)

response=client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Hello there!"
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
