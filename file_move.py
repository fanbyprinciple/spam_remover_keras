import os
import cv2
import shutil

source = 'pics/'

placement = [0,0,0,1]

# os.system("mkdir apple")
# os.system("mkdir iphone")

for i,filename in zip(placement,os.listdir('pics')):
    if(i):
        print('apple')
        dest = 'apple'
        shutil.move(source+filename, dest)
    else:
        print('iphone')
        dest = 'iphone'
        shutil.move(source+filename, dest)
