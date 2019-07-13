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
from sklearn.model_selection import train_test_split
import random
import math
import shutil

# arguments to pass in command line 
parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')
parser.add_argument('--dataset-dir', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
parser.add_argument('--target-dir', default='', help='Full path to the directory where our identified images should be saved.')

# reading the passed arguments
args = parser.parse_args()
data_dir = args.dataset_dir
target_dir = args.target_dir

onlyfiles = []
cont = 0

for folder in os.listdir(data_dir):
    i = 1
    # print(folder)
    fold = data_dir + '/' + folder
    cnt = 0 						# count the number of files in a folder
    for img in os.listdir(fold):
    	# print(img)
    	onlyfiles.append(img)
    	cnt += 1
    print(cnt)
    percent = math.ceil((cnt * 10) / 100) + 1
    
    target_folder = target_dir + '/' + folder

    # create folder for current person's test images
    print(target_folder)
    try:
    	os.mkdir(target_folder)
    except:
    	print('Such folder already exists')
    	continue

    for moving in range(0, int(percent)):
    	random_file = random.choice(os.listdir(fold))
    	print(random_file)
    	file_to_move = fold + '/' + random_file
    	new_file = target_folder + '/' + random_file
    	shutil.copyfile(file_to_move, new_file)
    	cont += 1

print(cont)
