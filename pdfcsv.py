import tabula
# Read a PDF File
df = tabula.read_pdf("file.pdf", pages='all')[0]
# Convert PDF into CSV
tabula.convert_into("file.pdf", "file.csv", output_format="csv", pages='all')

print(df)