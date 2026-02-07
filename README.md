# Xeruno – Drop-in OpenAI Replacement (Alpha)

> Replace OpenAI with **Xeruno** in 2 lines.
> Fully local. Zero external calls. Zero cost.

---

## 🚀 Quick Start

### 1️⃣ Clone and Start

```bash
git clone https://github.com/Benmebrouk/xeruno-dropin-demo.git
cd xeruno-dropin-demo
./run.sh
```

### 2️⃣ Run the demo

```bash
python demo.py
```

> Shows OpenAI-compatible local LLM handling with **streaming** and **metrics**.
> _Streaming tokens display progressively in real-time._

---

## 💡 What This Shows

* ✅ OpenAI code running **100% local**
* ✅ Same API, **no code changes required**
* ✅ Cost: **$0.00**
* ✅ Privacy: **0 bytes external**
* ✅ Streaming tokens & latency metrics visible live

> **Note:** Demo runs even if `OPENAI_API_KEY` is unset, with fallback to local LLM.

---

## ⚙️ Requirements

**System Requirements:**
* Python 3.8 or higher
* [Ollama](https://ollama.ai/) installed and running locally

**Quick Install:**
```bash
# Install Ollama (if not already installed)
# Visit: https://ollama.ai/download

# Pull a model (choose one)
ollama pull qwen2.5:7b      # Recommended: Fast, 4.7GB
# OR
ollama pull llama3.2        # Alternative: 2GB
# OR  
ollama pull phi3            # Smallest: 2.3GB
```

**Note:** The demo uses `qwen2.5:7b` by default. To use a different model, edit line 68 in `demo.py`.

---

## 📝 Alpha Disclaimer

* **Not production-ready**
* Goal: **prove drop-in concept**, get feedback
* **Works offline** (no internet needed)

---

## 📂 Folder Structure

```
.
├── demo.py           # Main demo script
├── run.sh            # Setup & start env
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 💖 Support Xeruno Development

[![Sponsor Xeruno](https://img.shields.io/badge/Sponsor-Xeruno-%23FF5F5F?style=flat-square&logo=github)](https://github.com/sponsors/Benmebrouk)

[Xeruno](https://github.com/Benmebrouk/xeruno-dropin-demo) is an **open-core project**.
The public drop-in demo is **free for non-commercial use**, but sponsoring helps sustain and grow the project.

### Why Sponsor?
Supporting Xeruno helps fund:
- **Xeruno Core** – the private engine powering the demo.
- **Open Source Tools** – like this drop-in OpenAI replacement.
- **Documentation & Tutorials** – helping everyone run local AI easily.

---

## 📜 License & Commercial Use

**Xeruno Drop-in Demo** is open-source for **non-commercial use** under the [MIT + Commercial Extension License](LICENSE.md).

*   ✅ **Free for:** Personal projects, research, evaluation, and non-profit use.
*   ❌ **Commercial Use:** Requires a commercial license for internal enterprise deployment, revenue-generating products, or API integration.

### 🚀 Commercial / Enterprise
For **commercial use**, enterprise deployment, or access to the **full Xeruno engine / SDK**:

- Contact: [nizar.benmebrouk@gmail.com](mailto:nizar.benmebrouk@gmail.com)
- Sponsor via [GitHub Sponsors](https://github.com/sponsors/Benmebrouk)

> Every sponsor helps keep Xeruno free and sustainable for the community.


---

## ⚡ Tips for HackerNews Visitors

* Simply clone the repo: `git clone https://github.com/Benmebrouk/xeruno-dropin-demo.git`
* Run `./run.sh` then `python demo.py`
* Watch streaming, metrics, and local execution in terminal
* **Optional:** Check `demo.py` to see the 50-line adapter logic.

> **Important:** No external requests unless fallback explicitly configured.
