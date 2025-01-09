# Named Entity Recognition App

This application demonstrates Named Entity Recognition (NER) using Hugging Face's transformers library and Streamlit for the user interface.

## Features

- Perform Named Entity Recognition on user-provided text
- Utilizes a pre-trained BERT model fine-tuned for NER
- Interactive web interface built with Streamlit
- Displays recognized entities with their labels and confidence scores


### Clone repo
```bash
https://github.com/Atharva01/Named-Entity-Recognition.git
```
### Create a virtual environment

```bash
python3 -m venv ner \
&&
source ner/bin/activate \
&&
pip install -r requirements.txt
```

### Huggingface Token
1. Update the .env file with token
   
### Run the StreamLit App 

```bash
streamlit run streamlit.py
```

### Optional

```bash
python3 test.py --token HUGGING_FACE_ACCESS_TOKEN
```
