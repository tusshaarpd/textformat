import streamlit as st
import textwrap
import re

def clean_text(text):
    """Removes extra spaces, newlines, and formatting inconsistencies."""
    # Remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)
    
    # Trim leading/trailing spaces
    text = text.strip()
    
    # Wrap text into a structured format (fixed width)
    structured_text = textwrap.fill(text, width=80)
    
    return structured_text

def main():
    st.title("Text Formatter and Cleaner")
    st.write("Paste your text below to remove formatting and structure it.")
    
    user_input = st.text_area("Enter text:", height=200)
    
    if st.button("Format Text"):
        if user_input:
            formatted_text = clean_text(user_input)
            st.subheader("Formatted Output:")
            st.text_area("", formatted_text, height=200)
        else:
            st.warning("Please enter some text to format.")

if __name__ == "__main__":
    main()
