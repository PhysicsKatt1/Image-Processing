##### import #####
import pandas as pd
import numpy as np
import os.path
from glob2 import glob

##### load files #####
path = r''
folder = '/ImagesForTLDsettingInvestigation'

CSVs = glob(os.path.join(path + folder, "*.csv"), recursive = True)

pythonFile = []
for file in CSVs:
    pythonFile.append(pd.read_csv(file))

pythonFile = pd.concat(pythonFile, axis = 0)
dataFile = pd.read_excel(path + '/TLDsettingsAcrossTools.xlsx')

##### remove extra data from python file names #####
# pd.options.display.max_colwidth = 1000
#
# for entry in pythonFile['file']:
#     pythonFile['file'] = entry.removeprefix('/mnt/c/Users/kat.kaylegianstarkey/Downloads/ImagesForTLDsettingInvestigation/JPEGS/')
#     pythonFile['file'] = entry.removesuffix('.jpeg')
#
# for entry in dataFile['Image Path']:
#     dataFile['Image Path'] = entry.removesuffix('.tif')