import os
import sys
import csv
import operator
import pandas as pd
import glob
import shutil
import numpy as np
import scandir

path = r'C:\Users\anika\Desktop\CSE465\Work\Timit_Train\TIMIT_FOLDER\train'

dest = r'C:\Users\anika\Desktop\CSE465'

j = 0
a = {}

for root, dirs, files in os.walk(path):
  
    for f in files:
        k = os.path.join(root, f)           
     
        f = open(r"C:\Users\anika\Desktop\CSE465\ben_all.txt","a")
        f.writelines(k+'\n')
        f.close()
            