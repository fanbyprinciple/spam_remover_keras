# USAGE
# python test_network.py --model santa_not_santa.model --image examples/santa_01.png
#python test_network.py --model santa_not_santa.model 


# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import shutil

import os
directory = 'examples'

images = []
outputs = []


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
    help="path to trained model model")
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")

args = vars(ap.parse_args())

for filename in os.listdir(directory):
    if(filename.endswith('.png')  or filename.endswith('.jpg')):
        images.append(filename)

print(images)

placement = []

for i in images:
    print('examples/'+i)
    image = cv2.imread('examples/'+i)

    orig = image.copy()
    # pre-process the image for classification
    image = cv2.resize(image, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load the trained convolutional neural network
    print("[INFO] loading network...")
    model = load_model(args["model"])

    # classify the input image
    (notSanta, santa) = model.predict(image)[0]

    # to decide where to put the image 
    decide = 0 if santa > notSanta else 1
    placement.append(decide)
    # # build the label
    # label = "Santa" if santa > notSanta else "Not Santa"
    # proba = santa if santa > notSanta else notSanta
    # label = "{}: {:.2f}%".format(label, proba * 100)

    # # draw the label on the image
    # output = imutils.resize(orig, width=400)
    # cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
    # 	0.7, (0, 255, 0), 2)

    # outputs.append(label)

    # print(outputs)
    # # # show the output image
    # cv2.imshow("Output", output)
    # cv2.waitKey(0)

print(placement)

source = 'examples/'

os.system("mkdir santa")
os.system("mkdir notSanta")

for i,filename in zip(placement,os.listdir(directory)):
    if(i):
        dest = 'santa'
        shutil.move(source+filename, dest)
    else:
        dest = 'notSanta'
        shutil.move(source+filename, dest)

