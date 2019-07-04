import dlib
from PIL import Image
from skimage import io
import matplotlib
import pathlib
import os
import argparse
import fnmatch


def detect_faces(image):
    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    print(len(detected_faces))
    if len(detected_faces) > 1:
    	face_frames = [(x.left()-20, x.top()-30, (x.left()-20) + 112, (x.top()-30) + 112) for x in detected_faces]
    elif len(detected_faces) == 1:
    	face_frames = [(x.left(), x.top(), x.right()+20, x.bottom()+20) for x in detected_faces]    	

    return face_frames

# Load image
img_path = 'name5.jpeg'
# img_path = folder + '/' + image # getting an image from current folder and cropping faces from it '/home/ti/Downloads/crop_and_find/faces/bekmurat_anarbayev/BrX4cAgDlX_.jpg'
image = io.imread(img_path)

# Detect face_frames
detected_faces = detect_faces(image)

size = 112,112
# Crop faces and plot

for n, face_rect in enumerate(detected_faces):
    face = Image.fromarray(image).crop(face_rect)
    face.thumbnail(size)
    face.save("alibek"+ str(n) + '.thumbnail', 'jpeg')    