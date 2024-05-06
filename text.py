import streamlit as st
from googleapiclient.discovery import build

# Load API key and create YouTube API service
api_key = "YOUR_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

# Example: Search for video by keyword
search_response = youtube.search().list(q="Python programming", type="video").execute()
videos = search_response.get("items", [])

# Display video details
for video in videos:
    st.write(f"Title: {video['snippet']['title']}")
    st.write(f"Description: {video['snippet']['description']}")
    st.write(f"Video ID: {video['id']['videoId']}")
