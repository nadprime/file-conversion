from docx2csv import extract_tables, extract
tables = extract_tables('some_file.docx')
extract(filename='some_file.docx', format="csv", singlefile=False)