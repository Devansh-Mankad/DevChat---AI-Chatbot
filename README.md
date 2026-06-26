# ✨ Nova AI – Multilingual Voice-Enabled AI Chatbot

> A modern AI chatbot built with **Google Gemini 2.5 Flash Lite**, **Streamlit**, and **Python**, featuring multilingual conversations, voice interaction, streaming responses, and built-in AI safety mechanisms.

---

# 📖 About The Project

**Nova AI** is a general-purpose conversational AI assistant designed to provide an intuitive and intelligent chatting experience through both text and voice. Powered by **Google Gemini 2.5 Flash Lite**, the application supports multilingual communication, real-time streaming responses, conversation memory, and safety-aware interactions.

Originally developed as a healthcare assistant (**CareBot**), the project evolved into a versatile AI chatbot capable of answering questions across various domains while maintaining responsible AI practices and accessibility for users speaking multiple Indian languages.

---

# ✨ Features

## 🤖 AI Capabilities

* General-purpose conversational AI
* Powered by Google Gemini 2.5 Flash Lite
* Context-aware conversations
* Real-time streaming responses
* AI-generated topic summaries
* Automatic retry for Gemini API failures

---

## 🌍 Multilingual Support

* Automatic language detection
* Supports English, Hindi, Gujarati, Marathi, Tamil, Telugu, Bengali, Punjabi, and more
* Responds in the same language as the user
* Handles mixed-language conversations (Hinglish, etc.)

---

## 🎙️ Voice Features

* Speech-to-Text using Google Speech Recognition
* Text-to-Speech using pyttsx3
* Voice input through microphone
* Automatic voice playback of AI responses
* Graceful fallback to text-only mode when audio devices are unavailable

---

## 🛡️ Safety Features

* Crisis and self-harm detection
* Emergency helpline recommendations
* Prompt injection & jailbreak protection
* Ethical response filtering
* Responsible AI behavior through system prompts

---

## 🎨 User Experience

* Modern Streamlit interface
* Animated streaming responses
* Chat history memory
* Topic summary sidebar
* Responsive and intuitive layout

---

# 🛠️ Tech Stack

| Layer                     | Technology                   |
| ------------------------- | ---------------------------- |
| **AI Model**              | Google Gemini 2.5 Flash Lite |
| **AI SDK**                | google-genai                 |
| **Frontend**              | Streamlit                    |
| **Backend**               | Python                       |
| **Speech-to-Text**        | SpeechRecognition            |
| **Text-to-Speech**        | pyttsx3                      |
| **Environment Variables** | python-dotenv                |

---

# 📂 Project Structure

```text
nova-ai/
│
├── app.py                 # Streamlit frontend and chat interface
├── brain.py               # AI engine, prompts, voice processing
├── .env                   # Gemini API key
├── .gitignore
├── requirements.txt
└── README.md
```

The project follows a clean two-layer architecture:

* **app.py** handles the user interface and chat interactions.
* **brain.py** contains the AI logic, prompt engineering, Gemini integration, and voice processing.

---

# 🚀 Getting Started

## Prerequisites

* Python 3.9+
* Google Gemini API Key
* Internet connection
* Microphone (optional for voice features)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/nova-ai.git
cd nova-ai
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open automatically at:

```
http://localhost:8501
```

---

# ⚙️ How It Works

```text
User (Text / Voice)
        │
        ▼
Streamlit Frontend (app.py)
        │
        ▼
Conversation Memory
        │
        ▼
Prompt Processing
        │
        ▼
Google Gemini 2.5 Flash Lite
        │
        ▼
Streaming AI Response
        │
        ▼
Text & Voice Output
```

Every user message is combined with the conversation history before being sent to Gemini, allowing the assistant to maintain context throughout the chat session. Voice interactions are handled through SpeechRecognition and pyttsx3, while built-in retry logic ensures reliable communication with the Gemini API.

---

# 🌐 Supported Languages

* English
* Hindi
* Gujarati
* Marathi
* Tamil
* Telugu
* Bengali
* Punjabi
* Hinglish
* And many more supported by Gemini

---

# 🔒 Security & Safety

Nova AI follows responsible AI principles by incorporating:

* Secure API key management using `.env`
* Crisis detection for self-harm related conversations
* Prompt injection protection
* Jailbreak resistance
* Ethical response generation
* Graceful error handling and API retry mechanisms

---

# 📈 Future Enhancements

* User Authentication
* Persistent Chat History Database
* Multiple AI Model Support
* File Upload & Document Chat
* Image Understanding
* Voice Wake Word Detection
* Custom AI Personas
* Chat Export (PDF/Markdown)
* Docker Deployment
* Cloud Deployment Support
* Retrieval-Augmented Generation (RAG)

---

# 👨‍💻 Developed By
**Devansh Mankad**
* GitHub: https://github.com/Devansh-Mankad

⭐ **If you found this project useful, consider giving it a star on GitHub!**
