# Module to crop images from the subfolders of the given folder (--data-dir).
# We can think of given folder as the dataset collected from different resources (web, other datasets, etc.)
# with folder names as the names of people in Name_Surname format
# each folder containing the images of that person where each image can contain either individual person
# or multiple people. In second case we have to crop each person in this image and save each person as
# different image in our target directory (--target-dir). Code uses Python 2.7

import dlib
from PIL import Image
from skimage import io
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pathlib
import os
import argparse
import fnmatch
import random
import time

parser = argparse.ArgumentParser(description='Crop faces from jpeg images in folders containing collected data')
# general
parser.add_argument('--data-dir', default='', help='full path to the directory with collected images without folmatting of folder names')
parser.add_argument('--target-dir', default='', help='full path to the directory where our cropped images dataset should be saved')

args = parser.parse_args()
dataset_dir = args.data_dir
target_dir = args.target_dir


# code below is used to detec faces in each input image
# returns a list with face frames for each person in the input image 
def detect_faces(image):

    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left()-30, x.top()-30,
                    x.right()+30, x.bottom()+30) for x in detected_faces] #x.right(), x.bottom()
    return face_frames
'''
    face_frames = [(x.left()-30, x.top()-40,
                        (x.left()-30) + 112, (x.top()-40) + 112) for x in detected_faces] #x.right(), x.bottom()
'''

# code below parses the given folders' subfolders and taking each input crops individual person
for folderi in os.listdir(dataset_dir):
    folder = dataset_dir + '/' + folderi
    print(dataset_dir + '/' + folderi)
    target_folder = target_dir + '/' + folderi
    print(target_folder)
    try: 
        os.mkdir(target_folder)
    except:
        print('Directory ', folderi, ' exists')
        
    for image in os.listdir(folder):
        print(image)
        # Load image
        img_path = folder + '/' + image # getting an image from current folder and cropping faces from it '/home/ti/Downloads/crop_and_find/faces/bekmurat_anarbayev/BrX4cAgDlX_.jpg'
        image = io.imread(img_path)

        # Detect face_frames
        detected_faces = detect_faces(image)
        size = 112,112

        # Crop faces and plot
        print(len(detected_faces))
        path_to_save = target_folder + '/' 
        for n, face_rect in enumerate(detected_faces):
            face = Image.fromarray(image).crop(face_rect)            
            face.thumbnail(size)
            face.save(path_to_save + str(random.randint(0,99)) + str(random.randint(0,99)), 'jpeg')
