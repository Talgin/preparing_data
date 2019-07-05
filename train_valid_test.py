# This module parses collected and refined dataset and divides it into
# Train, Validation and Test splits. 
# First, we have to read the data
# Second, we have to place it into numpy array 
import os, sys
import pathlib
import argparse
import numpy as np
import pandas as pd
# from subprocess import check_output
#print(check_output(["ls", "../input"]))
from PIL import Image
from time import time
from time import sleep
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# arguments to pass in command line 
parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')
parser.add_argument('--dataset-dir', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')

# reading the passed arguments
args = parser.parse_args()
data_dir = args.dataset_dir

onlyfiles = []

# display(_Imgdis(filename=folder + "/" + onlyfiles[i], width=112, height=112))

for folder in os.listdir(data_dir):
    i = 1
    # print(folder)
    fold = data_dir + '/' + folder
    for img in os.listdir(fold):
    	# print(img)
    	onlyfiles.append(img)


print("Working with {0} images".format(len(onlyfiles)))
print("Image examples: ")

for i in range(0, 10):
    print(onlyfiles[i])

train_files = []
y_train = []
i=0
for _file in onlyfiles:
    train_files.append(_file)
    label_in_file = _file.find("_")
    y_train.append(int(_file[0:label_in_file]))
    
print("Files in train_files: %d" % len(train_files))

# Original Dimensions
image_width = 640
image_height = 480
ratio = 4

image_width = int(image_width / ratio)
image_height = int(image_height / ratio)

channels = 3
nb_classes = 1

dataset = np.ndarray(shape=(len(train_files), channels, image_height, image_width),
                     dtype=np.float32)

i = 0
for _file in train_files:
    img = load_img(folder + "/" + _file)  # this is a PIL image
    img.thumbnail((image_width, image_height))
    # Convert to Numpy Array
    x = img_to_array(img)  
    x = x.reshape((3, 120, 160))
    # Normalize
    x = (x - 128.0) / 128.0
    dataset[i] = x
    i += 1
    if i % 250 == 0:
        print("%d images to array" % i)
print("All images to array!")