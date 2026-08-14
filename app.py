import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text into different languages.")

languages = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Arabic": "ar",
    "Italian": "it",
    "Russian": "ru"
}

text = st.text_area("Enter Text")

source = st.selectbox("Source Language", languages.keys())
target = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation Completed!")

            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

            st.code(translated)

            st.download_button(
                "Download Translation",
                translated,
                file_name="translation.txt"
            )

            # Text To Speech
            tts = gTTS(text=translated, lang=languages[target])

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name)

        except Exception as e:
            st.error(f"Error: {e}")