# Text to csv
import pandas as pd
  

dataframe1 = pd.read_csv("filename.txt")

dataframe1.to_csv('file.csv', index = None)