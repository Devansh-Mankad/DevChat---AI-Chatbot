import streamlit as st
import time
from brain import (
    get_carebot_response,
    summarize_symptoms,
    listen_to_user,
)

# 1. PAGE CONFIG
st.set_page_config(
    page_title="Nova AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. GLOBAL STYLES
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Root & Body ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main > div {
    background: linear-gradient(145deg, #f5f3ff 0%, #eef2ff 50%, #f0f9ff 100%);
    min-height: 100vh;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e7eb;
    box-shadow: 3px 0 20px rgba(109, 40, 217, 0.06);
}

[data-testid="stSidebar"] .stButton > button {
    background: #f5f3ff;
    color: #6d28d9;
    border: 1px solid #ddd6fe;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.85rem;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #ede9fe;
    border-color: #7c3aed;
    transform: translateY(-1px);
    box-shadow: 0 3px 10px rgba(109, 40, 217, 0.15);
}

/* ── Chat messages ── */
.stChatMessage {
    border-radius: 18px;
    margin-bottom: 6px;
    padding: 2px 6px;
}

/* ── Chat input container ── */
.stChatInputContainer {
    padding-right: 80px !important;
    border-radius: 16px !important;
    background: #ffffff !important;
    box-shadow: 0 2px 20px rgba(109, 40, 217, 0.1) !important;
    border: 1.5px solid #ddd6fe !important;
}

/* ── Chat input field ── */
.stChatInputContainer textarea {
    border: none !important;
    background: transparent !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    color: #1e1b4b !important;
}

.stChatInputContainer textarea::placeholder {
    color: #a5b4fc !important;
}

/* ── 🎙️ Mic button — glowing violet orb ── */
button[data-testid="baseButton-mic_btn"] {
    position: fixed;
    bottom: 16px;
    right: 22px;
    z-index: 9999;
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%);
    color: white;
    font-size: 22px;
    border: none;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.5),
                0 0 0 0 rgba(124, 58, 237, 0.4);
    animation: pulse-glow 2.5s ease-in-out infinite;
    transition: transform 0.2s ease;
}

button[data-testid="baseButton-mic_btn"]:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 28px rgba(124, 58, 237, 0.65);
}

@keyframes pulse-glow {
    0%   { box-shadow: 0 4px 20px rgba(124,58,237,0.45), 0 0 0 0   rgba(124,58,237,0.3); }
    50%  { box-shadow: 0 4px 20px rgba(124,58,237,0.45), 0 0 0 10px rgba(124,58,237,0); }
    100% { box-shadow: 0 4px 20px rgba(124,58,237,0.45), 0 0 0 0   rgba(124,58,237,0); }
}

/* ── Quick-action chips ── */
.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 12px 0 20px;
}

.chip {
    background: #ffffff;
    border: 1.5px solid #ddd6fe;
    color: #5b21b6;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.18s ease;
    white-space: nowrap;
}

.chip:hover {
    background: #ede9fe;
    border-color: #7c3aed;
    transform: translateY(-1px);
    box-shadow: 0 3px 10px rgba(109,40,217,0.12);
}

/* ── Welcome card ── */
.welcome-card {
    background: linear-gradient(135deg, rgba(124,58,237,0.07), rgba(79,70,229,0.05));
    border: 1.5px dashed rgba(124,58,237,0.3);
    border-radius: 20px;
    padding: 24px 28px;
    margin-bottom: 24px;
}

/* ── Divider tweak ── */
hr {
    border-color: #ede9fe !important;
}
</style>
""", unsafe_allow_html=True)



# 3. SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []
if "voice_query" not in st.session_state:
    st.session_state.voice_query = None


# 4. SIDEBAR
with st.sidebar:
    # Branding
    st.markdown("""
        <div style="text-align:center; padding:12px 0 18px;">
            <div style="font-size:2.6rem; line-height:1;">✨</div>
            <h2 style="
                margin: 6px 0 2px;
                font-weight: 800;
                font-size: 1.5rem;
                background: linear-gradient(135deg, #7c3aed, #4f46e5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">Nova AI</h2>
            <p style="color:#9ca3af; font-size:0.78rem; margin:0;">
                Your intelligent companion
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Clear button
    if st.button("🗑️  Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.voice_query = None
        st.rerun()

    st.divider()

    # Conversation Topics Summary
    st.markdown("""
        <p style="font-weight:600; font-size:0.85rem; color:#374151; margin:0 0 8px;">
            💬 Topics Discussed
        </p>
    """, unsafe_allow_html=True)

    if st.session_state.messages:
        with st.container(border=True):
            summary = summarize_symptoms(st.session_state.messages)
            st.markdown(
                f"<div style='font-size:0.82rem; color:#4b5563; line-height:1.6;'>{summary}</div>",
                unsafe_allow_html=True,
            )
    else:
        st.markdown(
            "<p style='color:#c4b5fd; font-size:0.82rem; font-style:italic;'>"
            "Topics will appear here as you chat.</p>",
            unsafe_allow_html=True,
        )

    st.divider()

    # What Nova can do
    st.markdown("""
        <p style="font-weight:600; font-size:0.85rem; color:#374151; margin:0 0 10px;">
            🚀 What I can help with
        </p>
        <div style="font-size:0.8rem; color:#6b7280; line-height:2;">
            💻 &nbsp;Coding &amp; Debugging<br>
            📚 &nbsp;Research &amp; Learning<br>
            ✍️ &nbsp;Writing &amp; Editing<br>
            🌍 &nbsp;Translation &amp; Languages<br>
            🧮 &nbsp;Maths &amp; Science<br>
            🍳 &nbsp;Recipes &amp; Lifestyle<br>
            🎨 &nbsp;Creative &amp; Brainstorming<br>
            💼 &nbsp;Career &amp; Professional<br>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Footer
    st.markdown("""
        <div style="text-align:center; font-size:0.72rem; color:#c4b5fd; padding-top:4px;">
            Powered by Gemini · 2026 Edition<br>
            🛡️ Safe · 🌐 Multilingual · 🎙️ Voice-ready
        </div>
    """, unsafe_allow_html=True)


# 5. MAIN HEADER
st.markdown("""
    <div style="padding: 8px 0 0;">
        <h1 style="
            font-size: 2.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 60%, #0ea5e9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 2px;
            line-height: 1.15;
        ">✨ Nova</h1>
        <p style="color:#6b7280; font-size:0.9rem; margin:0 0 4px;">
            Ask me anything — coding, writing, research, recipes, and more.
            &nbsp;·&nbsp; 🌐 Multilingual &nbsp;·&nbsp; 🎙️ Voice-enabled
        </p>
    </div>
""", unsafe_allow_html=True)

st.divider()


# 6. WELCOME CARD  (shown only on fresh chat)
if not st.session_state.messages:
    st.markdown("""
        <div class="welcome-card">
            <h3 style="color:#4c1d95; margin:0 0 8px; font-size:1.1rem;">
                👋 Hey! I'm Nova, your general-purpose AI assistant.
            </h3>
            <p style="color:#374151; margin:0; line-height:1.7; font-size:0.9rem;">
                I'm here to help with <b>any topic</b> — just type or speak your question.
                I understand <b>English, Hindi, Gujarati, Marathi, Tamil</b> and many more languages.
                Use the <b>🎙️ mic button</b> in the corner to talk to me hands-free.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Quick-action chips
    st.markdown("""
        <p style="font-size:0.82rem; color:#7c3aed; font-weight:600; margin-bottom:4px;">
            Try asking:
        </p>
        <div class="chip-row">
            <span class="chip">💻 Debug my Python code</span>
            <span class="chip">✍️ Write a cover letter</span>
            <span class="chip">🍳 Quick dinner recipe</span>
            <span class="chip">🌍 Translate to Hindi</span>
            <span class="chip">📚 Explain quantum computing</span>
            <span class="chip">🧮 Solve a math problem</span>
        </div>
    """, unsafe_allow_html=True)


# 7. CHAT HISTORY
for message in st.session_state.messages:
    avatar = "✨" if message["role"] == "assistant" else "🧑"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# 8. INPUT — TEXT & VOICE
prompt    = st.chat_input("Ask me anything...")
mic_clicked = st.button("🎙️", key="mic_btn")

user_query = None

if prompt:
    user_query = prompt
elif mic_clicked:
    with st.spinner("🎙️ Listening..."):
        voice_text = listen_to_user()
        if voice_text:
            user_query = voice_text
            st.toast(f"🎙️ Heard: {voice_text}", icon="🎤")
        else:
            st.warning("Could not understand audio. Please try again or type your question.")


# 9. RESPONSE PIPELINE
if user_query:
    # Save & display user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_query)

    # Generate & stream Nova's response
    with st.chat_message("assistant", avatar="✨"):
        response_placeholder = st.empty()

        with st.spinner("Nova is thinking..."):
            response = get_carebot_response(user_query, st.session_state.messages)

        # Word-by-word streaming effect
        full_text = ""
        for word in response.split(" "):
            full_text += word + " "
            time.sleep(0.02)
            response_placeholder.markdown(full_text + "▌")

        # Final render — no cursor
        response_placeholder.markdown(full_text.strip())

        # Persist to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_text.strip(),
        })

    st.rerun()
