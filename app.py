import streamlit as st
from agents.video_agent import initialize_agent, analyze_video_with_agent
from utils.file_utils import save_temp_files
from config.config import configure_env
from pathlib import Path
import os

# Configure environment
configure_env()

# Page setup
st.set_page_config(page_title=("Video Chat AI"), page_icon="🎥", layout="wide")
st.title("🎥🎥 AI Chat with videos")
st.caption("Gemini 2.0 & Phi Agent")


# sidebar
st.sidebar.header("Upload video")
video_files=st.sidebar.file_uploader("Upload a video", type=["mp4", "avi"])

video_path=None
if video_files:
    video_path=save_temp_files(video_files)
    st.sidebar.video(video_path)
    st.sidebar.success("Video uploaded successfully")


# session state for chat and files
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

if "agent" not in st.session_state:
    st.session_state.agent=initialize_agent()

# logic area
if video_files and video_path:
    st.subheader("Chat with the video")
    # chat input
    user_input=st.chat_input(" Ask something about the video")

    if user_input:
        st.session_state.chat_history.append({"role":"user", "content":user_input})

        # process with AI agent
        with st.spinner("Analyzing video ..."):
            try:
                response=analyze_video_with_agent(st.session_state.agent, video_path, user_input)
                st.session_state.chat_history.append({"role":"analyst", "content":response})
            except Exception as e:
                error_msg=f"Error : {e}"
                st.session_state.chat_history.append({"role":"analyst", "content":error_msg}) 
# render full convo
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# reset button
if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history=[]
    if video_path:
        Path(video_path).unlink(missing_ok=True)
    st.rerun()
else:
    st.info("Upload a video for a conversation")