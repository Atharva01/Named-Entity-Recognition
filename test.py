from app.ner_app import perform_ner

text = """
Microsoft is headquartered in Redmond, Washington. Satya Nadella is the CEO.
"""

entities = perform_ner(text)
for entity in entities:
    print(f"Entity: {entity['word']}, Label:{entity['entity_group']}, Confidence: {entity['score']:.2f}")