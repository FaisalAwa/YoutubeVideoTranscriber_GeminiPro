# import streamlit as st
# from dotenv import load_dotenv
# import os
# from youtube_transcript_api import YouTubeTranscriptApi
# import google.generativeai as genai

# # Load all the environment variables
# load_dotenv()

# # Configure the generative AI with the Google API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Prompt for the generative AI
# prompt = """
# You are a youtube video summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points within 250 words. Please provide the summary of the text given here:
# """

# # Function to extract transcript details from YouTube videos
# def extract_transcript_details(youtube_video_url):
#     try:
#         video_id = youtube_video_url.split("=")[1]
#         transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

#         transcript = ""
#         for i in transcript_text:
#             transcript += " " + i["text"]
        
#         return transcript

#     except Exception as e:
#         raise e

# # Function to fetch summary based on prompt from Google Gemini
# def fetch_transcript(transcript_text, prompt):
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content(prompt + transcript_text)
#     return response.text

# # Create Streamlit frontend
# st.title("YouTube Transcript to Detailed Notes Converter")
# youtube_link = st.text_input("Enter YouTube Video Link")

# if youtube_link:
#     video_id = youtube_link.split("=")[1]
#     st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# if st.button("Get Detailed Notes"):
#     transcript_text = extract_transcript_details(youtube_link)

#     if transcript_text:
#         summary = fetch_transcript(transcript_text, prompt)
#         st.markdown("## Detailed Notes:")
#         st.write(summary)


import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

# Load all the environment variables
load_dotenv()

# Configure the generative AI with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for the generative AI
prompt = """
You are a youtube video summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points within 250 words. Please provide the summary of the text given here:
"""

# Function to extract transcript details from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        
        return transcript

    except Exception as e:
        raise e

# Function to fetch summary based on prompt from Google Gemini
def fetch_transcript(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #FF0000;
            color: #FFFFFF;
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #FFFFFF;
        }
        .subheader {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #FFFFFF;
        }
        .description {
            font-size: 18px;
            color: #FFFFFF;
        }
        .stTextInput > div > input {
            background-color: #001f3f;
            color: #FFFFFF;
        }
        .stButton > button {
            background-color: #001f3f;
            color: #FFFFFF;
        }
        .stFileUploader > label {
            background-color: #001f3f;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# SVG Animation for YouTube Transcriber
st.markdown("""
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <g>
    <title>YouTube Transcriber</title>
    <rect width="100%" height="200" fill="#FF0000" />
    <rect x="10%" y="20" width="80%" height="160" fill="#FFFFFF" />
    <text x="50%" y="100" font-size="24" font-family="Arial" fill="#FF0000" text-anchor="middle">
      <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite" />
      📹 YouTube Transcriber 🎥
    </text>
  </g>
</svg>
""", unsafe_allow_html=True)

# Create Streamlit frontend
# st.set_page_config(page_title="YouTube Transcript to Detailed Notes Converter")
st.markdown('<div class="header">📹 YouTube Transcript to Detailed Notes Converter 🎥</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Enter the YouTube video link to get detailed notes! 📝</div>', unsafe_allow_html=True)

youtube_link = st.text_input("Enter YouTube Video Link")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = fetch_transcript(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
