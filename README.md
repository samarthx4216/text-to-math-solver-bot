# 🧮 Text-to-Math Problem Solver Bot

A Streamlit-based chatbot that converts plain English math questions into step-by-step solutions using **Groq LLM** and **LangChain** agents.

---

## 🚀 Demo

Run locally and interact with the bot through a clean chat interface powered by Groq's fast inference.

---

## ✨ Features

- 💬 Natural language to math problem solving
- 🧠 Step-by-step reasoning using LangChain agents
- 📖 Wikipedia integration for concept lookups
- 🔢 Built-in calculator for precise computations
- ⚡ Fast inference powered by Groq (`llama-3.1-8b-instant`)
- 🖥️ Clean chat UI with Streamlit
- 🔑 Sidebar API key input — no `.env` needed

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | UI & chat interface |
| [LangChain](https://www.langchain.com/) | Agent framework |
| [Groq](https://console.groq.com/) | LLM inference |
| [Wikipedia API](https://pypi.org/project/wikipedia/) | Concept lookup |
| Python 3.10+ | Language |

---

## 🤖 How It Works

The app uses a **LangChain ZERO_SHOT_REACT agent** with 3 tools:

1. **Wikipedia** — Fetches background information on topics
2. **Calculator** — Uses `LLMMathChain` for precise math calculations
3. **Reasoning** — Uses a custom prompt to solve word problems step-by-step

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/text-to-math-solver-bot.git
cd text-to-math-solver-bot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Enter your Groq API Key in the sidebar

> Get your free API key from [console.groq.com](https://console.groq.com)

---

## 📁 Project Structure

```
text-to-math-solver-bot/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 💡 Example Questions

- *"What is the derivative of x² + 3x + 5?"*
- *"If a train travels 60 km/h for 2.5 hours, how far does it go?"*
- *"What is the Pythagorean theorem and solve: a=3, b=4, find c"*
- *"Calculate compound interest: principal=10000, rate=5%, time=3 years"*

---

## 🙌 Acknowledgements

- [Groq](https://groq.com/)
- [LangChain](https://langchain.com/)
- [Streamlit](https://streamlit.io/)
