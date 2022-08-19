# Convert pdf to csv

import pdfplumber
import pandas as pd

file = 'file.pdf'

lines = []

with pdfplumber.open(file) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            lines.append(line)
            print(line)

df = pd.DataFrame(lines)

df.to_csv('file.csv')
