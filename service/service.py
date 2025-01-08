# service.py
from transformers import logging as transformers_logging, pipeline, AutoModelForTokenClassification, AutoTokenizer

# Suppress warnings from Hugging Face Transformers
transformers_logging.set_verbosity_error()

class NER():
    def __init__(self,text):
        # Load the Hugging Face NER pipeline
        self.model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)  # Explicitly load tokenizer
        self.model = AutoModelForTokenClassification.from_pretrained(self.model_name, ignore_mismatched_sizes=True)   
        self.ner_pipeline = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")
        self.text = text
        
    def perform_ner(self):
        """
        Perform Named Entity Recognition (NER) on the given text.
        :param text: Input text
        :return: List of entities with labels
        """
        return self.ner_pipeline(self.text)
