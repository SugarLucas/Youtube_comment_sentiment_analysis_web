import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="YouTube Comment Sentiment Analysis",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load External CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
css_path = os.path.join("app","static", "style.css")
load_css(css_path)

# Title and description
st.title("Analysis 🎥")
st.subheader("Welcome to the YouTube Comment Sentiment Analysis app! 🤖")
st.markdown(
    "This tool helps content creators gain insights into the sentiment and themes of their audience's comments. "
    "Simply input a YouTube video URL to get started."
)

# Input Section
video_url = st.text_input("Enter YouTube Video URL", placeholder="https://youtu.be/abc123")

if st.button("Analyze Video"):
    if video_url:
        # Simulating analysis
        with st.spinner("Analyzing... Please wait."):
            import time
            time.sleep(2)  # Simulate processing time
            st.markdown('<div class="success-message">Analysis complete! Displaying results...</div>', unsafe_allow_html=True)

            # Sentiment Analysis Results Section
            st.header("Sentiment Analysis Results")
            st.markdown("""
            - **Positive Sentiment**: 65%
            - **Neutral Sentiment**: 20%
            - **Negative Sentiment**: 15%
            """)

            # Key Themes Section
            st.header("Key Themes")
            st.markdown("""
            - 🗨️ **Audience Engagement**: High
            - 🌟 **Popular Topics**: Content quality, humor, editing style
            - 🛠️ **Suggested Improvements**: More detailed explanations, shorter video duration
            """)

            # Suggested Videos
            st.header("Suggested Videos for Inspiration")
            st.markdown("""
            - [Similar Video 1](#)
            - [Similar Video 2](#)
            """)
    else:
        st.error("Please enter a valid YouTube URL.")

# Footer
st.markdown("---")
st.markdown("Developed by **LAAMA Team**.")