import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="YouTube Comment Sentiment Analysis",
    page_icon="📊",
    layout="centered"
)

# Title and Description
st.title("Analysis 🎥")
st.subheader("Welcome to the YouTube Comment Sentiment Analysis app!")
st.markdown(
    "This tool helps content creators gain insights into the sentiment and themes of their audience's comments. "
    "Simply input a YouTube video URL to get started."
)

# Input Section
video_url = st.text_input("Enter YouTube Video URL", placeholder="https://youtu.be/abc123")

if st.button("Analyze Video"):
    if video_url:
        with st.spinner("Analyzing... Please wait."):
            # Placeholder API call
            try:
                response = requests.get("https://example.com/api", params={"url": video_url})  # Replace with real API
                if response.status_code == 200:
                    data = response.json()
                    st.success("Analysis complete! Displaying results...")

                    # Sentiment Analysis Results
                    st.header("Sentiment Analysis Results")
                    st.write(f"**Positive Sentiment**: {data['positive']}%")
                    st.write(f"**Neutral Sentiment**: {data['neutral']}%")
                    st.write(f"**Negative Sentiment**: {data['negative']}%")

                    # Key Themes
                    st.header("Key Themes")
                    st.write("📈 **Audience Engagement**:", data["key_themes"]["engagement"])
                    st.write("🌟 **Popular Topics**:", ", ".join(data["key_themes"]["topics"]))
                    st.write("🛠 **Suggested Improvements**:", ", ".join(data["key_themes"]["improvements"]))

                    # Suggested Videos
                    st.header("Suggested Videos for Inspiration")
                    for video in data["suggested_videos"]:
                        st.markdown(f"[{video['title']}]({video['url']})")
                else:
                    st.error("Error fetching data. Please try again.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")

# Footer
st.markdown("---")
st.markdown("Developed by LAAMA Team.")