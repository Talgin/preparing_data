# Use this module to rename the images in your dataset folders according to 
# the name of the folder + index of the image in 0001, 0002, etc. format.
# For example, you have some dataset folder your_dataset
# In this dataset you have folders with individual person images, folders are 
# named according to the name of the person: David_Beckham, Mohammad_Ali, etc.
# In this folders you want to rename all the images according to the name of the folder
# like David_Beckham_0001.jpg, David_Beckham_0002.jpg, etc. 
# For more information on the naming you can search the LFW dataset, according to which this
# renaming format is done. 

import os
import pathlib
import argparse
import time
import random

# arguments to pass in command line 
parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')
parser.add_argument('--dataset-dir', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')

# reading the passed arguments
args = parser.parse_args()
data_dir = args.dataset_dir

for folder in os.listdir(data_dir):
    i = 1
    time.sleep(0.1)
    print(folder)
    fold = data_dir + '/' + folder
    for img in os.listdir(fold):    
        extension = img.split(".")[-1].lower()
        #if extension != "jpg":
        #    continue
        if i == 0:
            stri = '000'
        elif 0 < i < 10:
            stri = '00' + str(i)
        elif 9 < i < 100:
            stri = '0' + str(i)
        else:
            stri = str(i)
        extension = 'jpg'
        name_str = "_0" + stri + '.' + extension
        # name_str = str(random.randint(1,1000))
        os.rename(os.path.join(fold, img), os.path.join(fold, os.path.basename(fold) + name_str))
        i = i + 1
        print(os.path.basename(fold))

    # time.sleep(1)
