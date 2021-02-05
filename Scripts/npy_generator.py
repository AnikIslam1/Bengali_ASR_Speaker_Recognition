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
    
    for dirs in root:
        for f in files:
            k = os.path.join(root, f)
            a.setdefault (k,j)
            #print(files)
    j = j+1
    #print(a)        
        #print(dirs)
#print(a)   
#np.save(dest, a)  