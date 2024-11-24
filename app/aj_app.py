import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

# Configure the Streamlit page
st.set_page_config(
    page_title="YouTube Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

def mock_analyze_video(video_url):
    """
    Mock function to simulate video analysis.
    In production, this would make API calls to the backend.
    """
    return {
        'video_info': {
            'title': 'Sample Video',
            'views': 150000,
            'likes': 12000,
            'comments': 3500,
        },
        'sentiment_analysis': {
            'positive': 65,
            'neutral': 20,
            'negative': 15,
        },
        'top_themes': [
            {'theme': 'Product Quality', 'mentions': 450},
            {'theme': 'Customer Service', 'mentions': 320},
            {'theme': 'Price', 'mentions': 280},
            {'theme': 'Features', 'mentions': 250},
            {'theme': 'User Experience', 'mentions': 200},
        ],
        'temporal_data': [
            {'date': '2024-01', 'sentiment_score': 0.8},
            {'date': '2024-02', 'sentiment_score': 0.75},
            {'date': '2024-03', 'sentiment_score': 0.85},
            {'date': '2024-04', 'sentiment_score': 0.82},
        ],
        'similar_videos': [
            {'title': 'Similar Video 1', 'url': 'https://youtube.com/watch1', 'performance_score': 0.92},
            {'title': 'Similar Video 2', 'url': 'https://youtube.com/watch2', 'performance_score': 0.88},
            {'title': 'Similar Video 3', 'url': 'https://youtube.com/watch3', 'performance_score': 0.85},
        ]
    }

def display_video_metrics(video_info):
    """Display basic video metrics in a row of cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Views", f"{video_info['views']:,}")
    with col2:
        st.metric("Likes", f"{video_info['likes']:,}")
    with col3:
        st.metric("Comments", f"{video_info['comments']:,}")
    with col4:
        engagement_rate = round((video_info['likes'] + video_info['comments']) / video_info['views'] * 100, 2)
        st.metric("Engagement Rate", f"{engagement_rate}%")

def plot_sentiment_distribution(sentiment_data):
    """Create a pie chart for sentiment distribution"""
    fig = go.Figure(data=[go.Pie(
        labels=list(sentiment_data.keys()),
        values=list(sentiment_data.values()),
        hole=.3,
        marker_colors=['#2ecc71', '#95a5a6', '#e74c3c']
    )])
    fig.update_layout(title="Comment Sentiment Distribution")
    st.plotly_chart(fig)

def plot_themes(themes_data):
    """Create a horizontal bar chart for top themes"""
    df = pd.DataFrame(themes_data)
    fig = px.bar(df, 
                 x='mentions', 
                 y='theme',
                 orientation='h',
                 title="Top Comment Themes")
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)

def plot_temporal_analysis(temporal_data):
    """Create a line chart for sentiment over time"""
    df = pd.DataFrame(temporal_data)
    fig = px.line(df, 
                  x='date', 
                  y='sentiment_score',
                  title="Sentiment Trend Over Time")
    fig.update_layout(yaxis_range=[0, 1])
    st.plotly_chart(fig)

def main():
    # Header
    st.title("📊 YouTube Comment Sentiment Analysis")
    st.markdown("""
    Analyze audience sentiment and get actionable insights for your YouTube content.
    Enter a YouTube video URL below to get started.
    """)
    
    # URL input
    video_url = st.text_input("Enter YouTube Video URL", 
                             placeholder="https://www.youtube.com/watch?v=...")
    
    if st.button("Analyze Video"):
        if video_url:
            with st.spinner("Analyzing video comments..."):
                # In production, this would make an API call to your backend
                analysis_results = mock_analyze_video(video_url)
                
                # Display results
                st.subheader("Video Overview")
                display_video_metrics(analysis_results['video_info'])
                
                # Create two columns for the charts
                col1, col2 = st.columns(2)
                
                with col1:
                    plot_sentiment_distribution(analysis_results['sentiment_analysis'])
                
                with col2:
                    plot_themes(analysis_results['top_themes'])
                
                # Temporal analysis
                st.subheader("Sentiment Trend Analysis")
                plot_temporal_analysis(analysis_results['temporal_data'])
                
                # Similar videos recommendations
                st.subheader("Similar High-Performing Videos")
                for video in analysis_results['similar_videos']:
                    with st.expander(f"📹 {video['title']} (Performance Score: {video['performance_score']})"):
                        st.write(f"URL: {video['url']}")
                        st.progress(video['performance_score'])
                
                # Export options
                st.subheader("Export Analysis")
                if st.download_button(
                    label="Download Analysis Report (JSON)",
                    data=json.dumps(analysis_results, indent=2),
                    file_name=f"sentiment_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                ):
                    st.success("Report downloaded successfully!")
                
        else:
            st.warning("Please enter a valid YouTube URL")

    st.markdown("---")
    st.markdown("Developed by **LAAMA Team**.")

if __name__ == "__main__":
    main()
