import pandas as pd
import os
import chardet  

file = r"pandas_selector/file.csv"
def detect_encoding(file_path): 
    with open(file_path, 'rb') as file: 
        detector = chardet.universaldetector.UniversalDetector() 
        for line in file: 
            detector.feed(line) 
            if detector.done: 
                break
        detector.close() 
    return detector.result['encoding'] 


encoding = detect_encoding(file) 
print(f'The encoding of the file is: {encoding}') 

df = pd.read_csv(file, na_filter=False, sep=';', encoding= 'ISO-8859-1')
print(df)