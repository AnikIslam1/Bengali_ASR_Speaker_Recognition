import os
import sys
import csv
import operator
import pandas as pd
import glob
import shutil


df = pd.read_csv('D:\DATA_SET\dataset\main.tsv', delimiter = '\t')

group = pd.Series(df.groupby('userid').voiceid.unique())

for i in group.index:
    folder_path = os.path.join(r'D:\DATA_SET\dataset\sorted',i)
    
    if os.path.exists(folder_path):
        for f in group[i]:
            file_name = str(f)+'.flac'
            source = os.path.join(r'D:\DATA_SET\data', file_name)
            shutil.copy(source,folder_path)
            print(source)
    else:
        os.makedirs(folder_path)         
        for f in group[i]:
            file_name = str(f)+'.txt'      
            source = os.path.join(r'D:\DATA_SET\data',file_name)
            shutil.copy(source,folder_path)
 