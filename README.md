# ?? AI Video Chat Summarizer

An AI-powered application that lets you **chat with your videos** using natural language.

Upload a video, ask questions about its content, and receive intelligent responses powered by Google's Gemini multimodal models.

---

## ?? Features

- ?? Upload `.mp4`, `.mov`, and `.avi` videos
- ?? Ask natural language questions about video content
- ?? Powered by Google Gemini 2.0 Flash
- ?? Optional web search using DuckDuckGo via Phi Agent
- ?? Multimodal video understanding
- ??? Modular and maintainable project architecture
- ?? Reset conversation and clear chat history
- ? Interactive Streamlit interface

---

## ??? Tech Stack

- Python
- Streamlit
- Google Gemini 2.0 Flash
- Phi Agent
- DuckDuckGo Search
- Google Generative AI
- dotenv

---

## ?? Project Structure

```
ai-video-chat-summarizer/
?
??? agents/
?   ??? video_agent.py
?   ??? ...
?
??? utils/
?   ??? file_utils.py
?   ??? ...

??? app.py
??? requirements.txt
??? .env
??? README.md
```

---

## ?? Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-video-chat-summarizer.git
```

Go to the project

```bash
cd ai-video-chat-summarizer
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ?? Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ?? Run the application

```bash
streamlit run app.py
```

---

## ?? Example Questions

- Summarize this video.
- What is the main topic?
- List the important events.
- What objects appear in the video?
- Explain what happens in the first minute.
- Are there any people speaking?
- What is the conclusion?

---

## ?? Demo



## ?? Future Improvements

- Voice interaction
- Video timestamp references
- Support for YouTube URLs
- PDF report generation
- Multi-video conversations
- Persistent chat history
- Vector database for long videos
- Support for multiple LLM providers

---

## ?? Contributing

Contributions are welcome.

Feel free to open issues or submit pull requests.

---

## ?? License

This project is licensed under the MIT License.
