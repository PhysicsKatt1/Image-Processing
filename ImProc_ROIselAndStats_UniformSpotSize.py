#### This script converts batches of .tif files to .jpeg for memory allocation purposes then allows you
##### to select your ROI. To select an ROI, run the script. Left click at the center of your ROI when an image
##### opens then hit ESC to close the image and exit the for loop. Adjust the variable r until the blue masking
##### circle fully covers your spot. Basic image stats are saved to a .csv in the same folder your images are in.

##### import #####
import cv2 as cv2
import numpy as np
import pandas as pd
from glob2 import glob
import os.path
from itertools import chain
from PIL import Image

##### set radius #####
r = 120

##### load files and convert to jpeg to save memory #####
path = r''
folder = '/PythonImageProcessing/TestImages'

newPath = r'/mnt/c/Users/kat.kaylegianstarkey/Downloads' + folder + '/JPEGS'   # saves jpegs in separate folder
if not os.path.exists(newPath):
   os.makedirs(newPath)

print('Converting .tif to .jpeg')
for infile in os.listdir(path + folder):
    if infile[-3:] == 'tif':
       outfile = infile[:-3] + 'jpeg'
       im = Image.open(path + folder + '/' + infile)
       out = im.convert('L')
       out.save(newPath + '/' + outfile, "JPEG", quality=90)

AllFiles = glob(os.path.join(newPath, "**", "*.jpeg"), recursive = True)
AllMaskFiles = glob(os.path.join(newPath, "**", "*.jpeg"), recursive = True)

ALLfiles = []
ALLmaskFiles = []
for allfiles, allmaskfiles in zip(AllFiles, AllMaskFiles):
   af = cv2.imread(allfiles)
   amf = cv2.imread(allmaskfiles)
   ALLfiles.append(af)
   ALLmaskFiles.append(amf)

##### Process images #####
N = np.arange(0, len(AllFiles))
ROImean = []
ROIstddev = []
backgroundMean = []
backgroundStdev = []
totalMean = []
totalStddev = []
cnr = []

for file, maskFile, n in zip(ALLfiles, ALLmaskFiles, N):
   ##### select ROI #####
   print('Opening image number {}'.format(n))
   ROIx = []
   ROIy = []
   backgroundX = []
   backgroundY = []
   def drawCircle(click, x, y, flags, params):
      if click == cv2.EVENT_LBUTTONDOWN:
         cv2.circle(maskFile, (x, y), r, 255, -1)
         roiMask = np.where(maskFile == 255)
         bgMask = np.where(maskFile != 255)
         ROIx.append(roiMask[1]), ROIy.append(roiMask[0])
         backgroundX.append(bgMask[1]), backgroundY.append(bgMask[0])

   while True:
      cv2.namedWindow('image')
      cv2.setMouseCallback('image', drawCircle)
      cv2.imshow('image', maskFile)
      if cv2.waitKey(1) == 27:
         break

   cv2.destroyAllWindows()

   print('Finding ROI and background')
   r_x = list(chain(*ROIx))
   r_y = list(chain(*ROIy))
   ROI = file[r_y][r_x]

   b_x = list(chain(*backgroundX))
   b_y = list(chain(*backgroundY))

   len1, len2 = int(len(b_x) / 3), int(2 * len(b_x) / 3)
   x1 = b_x[:len1]
   x2 = b_x[len1:len2]
   y1 = b_y[:len1]
   y2 = b_y[len1:len2]

   bg1 = file[y1][x1]                # this and the following line if code breaks while "Finding ROI and background"
   background = (bg1)[y2][x2]

   # background = file[y1][x1]           # uncomment if preceeding 2 lines are commented
                                    # estimates background from a sample of pixels assuming uniform background intensity

   ##### analyze image #####
   print('Calculating statistics')
   ROImean.append(np.mean(ROI))
   ROIstddev.append(np.std(ROI))
   backgroundMean.append(np.mean(background))
   backgroundStdev.append(np.std(background[:77200]))  # an estimate because the full array causes memory allocation issues
   totalMean.append(np.mean(file))
   totalStddev.append(np.std(file))

   del ROIx, ROIy, backgroundX, backgroundY, r_x, r_y, ROI, b_x, b_y, background, x1, x2, y1, y2

for roimean, backgroundmean, roistddev, backgroundstddev in zip(ROImean, backgroundMean, ROIstddev, backgroundStdev):
   cnr.append(abs(roimean - backgroundmean) / (np.sqrt(roistddev **2 + backgroundstddev**2)))

##### save image data #####
print('Saving')
imageData = pd.DataFrame({'file':AllFiles,'ROImean':ROImean, 'ROIstddev':ROIstddev,
                         'backgroundMean':backgroundMean, 'backgroundStddev':backgroundStdev,
                        'totalMean':totalMean, 'totalStddev':totalStddev, 'cnr':cnr})
imageData.to_csv(path + folder + '/ImageStats.csv', index = True)