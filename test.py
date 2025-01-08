import subprocess
import argparse
parser = argparse.ArgumentParser(description="Hugging Face login thorugh CLI")
parser.add_argument('--token',type=str,help='Your Hugging Face Access Token')
args = parser.parse_args()
subprocess.run(
    ["python3","huggingface_login.py",args.token]
)
from service.service import NER
text = """
Microsoft is headquartered in Redmond, Washington. Satya Nadella is the CEO.
"""

ner = NER(text)
entities = ner.perform_ner()
for entity in entities:
    print(f"Entity: {entity['word']}, Label:{entity['entity_group']}, Confidence: {entity['score']:.2f}")
