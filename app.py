import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import pyperclip

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with the new API style
client = OpenAI(api_key=api_key)

# Streamlit page configuration
st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")

# Page title and description
st.title("🌐 Real-Time Language Translation Tool 🌐")
st.write("Translate text between multiple languages instantly using AI. 🌍")

# Sidebar for language settings with Urdu added
st.sidebar.title("Language Options 🌐")
languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean", "Hindi", "Arabic", "Russian", "Urdu"]
source_language = st.sidebar.selectbox("🌎 Source Language", languages)
target_language = st.sidebar.selectbox("🌍 Target Language", languages)

# Main input area for user text
text_to_translate = st.text_area("Enter text for translation ✍️", "Type here...")

# Function to perform translation using OpenAI API
def translate_text(client, text, source, target):
    prompt = f"Translate this text from {source} to {target}:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    translation_text = response.choices[0].message.content.strip()
    return translation_text

# Translation action with copy and download functionality
if st.button("🌐 Translate"):
    if text_to_translate.strip():
        translation = translate_text(client, text_to_translate, source_language, target_language)
        
        # Display the translation
        st.write("### 🎉 Translation Result:")
        st.success(translation)
        
        # Copy Button
        if st.button("📋 Copy Translation"):
            pyperclip.copy(translation)
            st.write("Copied to clipboard!")
        
        # Download as Text File
        st.download_button(
            label="📥 Download Translation as .txt",
            data=translation,
            file_name="translation.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter text to translate.")

# Sidebar instructions
st.sidebar.markdown("### 🌟 How to Use 🌟")
st.sidebar.write("""
1. Select the source and target languages.
2. Enter the text you want to translate.
3. Click 'Translate' to view the result instantly.
4. Use 'Copy' or 'Download' options for convenience.
""")
st.sidebar.info("Experience language translation with AI! 🌐")




# About section
st.sidebar.write("### About this Tool")
st.sidebar.write("This tool leverages OpenAI's language model to provide high-quality translations between a variety of languages in real-time.")