# 🖥️ TerminalAI

Translate natural language into terminal commands using GPT-4.

## 💡 Features
- 🔤 Converts plain English to shell commands
- 💻 Use via CLI, FastAPI, or Streamlit
- 🐳 Includes Docker support

## 🚀 CLI Example
```bash
python cli.py run "list all files including hidden ones"
```

## 💻 Local Dev
```bash
uvicorn main:app --reload
streamlit run ui.py
```

## 🐳 Docker
```bash
docker build -t terminalai .
docker run -e OPENAI_API_KEY=your-key -p 8000:8000 terminalai
```

## 📄 License
MIT
