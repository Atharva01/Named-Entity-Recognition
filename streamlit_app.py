# streamlit_app.py
import subprocess
subprocess.run(
                ["python3", "huggingface_login.py"]
                )

import streamlit as st
from service.service import NER

# Streamlit App Title
st.title("Named Entity Recognition (NER) Application")

# Input Text Area
text_input = st.text_area(
    "Enter your text here:",
    height=150,
)

# Run NER when the button is clicked
if st.button("Extract Entities"):
    if text_input.strip():
        st.subheader("Extracted Entities")
        ner = NER(text_input)
        entities  = ner.perform_ner()
        if entities:
            # Display results
            for entity in entities:
                st.write(f"**Entity**: {entity['word']} | **Label**: {entity['entity_group']} | **Confidence**: {entity['score']:.2f}")
        else:
            st.write("No entities detected!")
    else:
        st.warning("Please enter some text to process.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Hugging Face Transformers")
