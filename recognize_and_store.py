# Given module performs face recognition to refine images of our dataset
# It reads and image from the given known directory and compares it with the images in a directory with unkown images
# The known person image name should be identical with the name of the folder where unknown people's images are stored.
# E.g. if the known person's image name is Talgin_Kotalgin.jpg then the folder containing the images that should be parsed 
# for this person should be named Talgin_Kotalgin too. 
# So the algorithm reads first image from the folder (--known-dir) with known people images (say Talgin_Kotalgin.jpg first)
# then it finds the folder with the same name (Talgin_Kotalgin) from unknown images directory (--unknown-dir)
# then it compares each image in this directory with the anchor image (Talgin_Kotalgin.jpg)
# In case of positive match we create a directory for this person in another target folder (--target-dir)
# and save all matching images in here.
# As the face recognition tool we used A. Geitgey's https://github.com/ageitgey/face_recognition library
# Instructions on how to install and requirements could be found in the above github directory
# With any questions regarding this module email me to islamgozhayev@tengrilab.kz or write to +77751033311 (WhatsApp) 
# Good luck!
import face_recognition
import argparse
import shutil, os

# arguments to pass in command line 
parser = argparse.ArgumentParser(description='Crop faces from jpeg images in folders containing collected data')
parser.add_argument('--known-dir', default='', help='Full path to the directory with known person image file. Note: directory should contain images with known persons named according to the name of the person')
parser.add_argument('--unknown-dir', default='', help='Full path to the directory where our unknown images are stored. E.g. it should be the directory with subdirectories containing images of unknown people')
parser.add_argument('--target-dir', default='', help='Full path to the directory where our identified images should be saved.')

# reading the passed arguments
args = parser.parse_args()
known_dir = args.known_dir
unknown_dir = args.unknown_dir
target_dir = args.target_dir

lost_dir = []
lost_embeddings = []
# Open the known_dir, get one person's image and search similar people in unknown_dir
for image in os.listdir(known_dir):
    print(unknown_dir + '/' + image)    
    known_person = face_recognition.load_image_file(known_dir + '/' + image)
    
    # Try to get the embeddings from the given person's image, if not found throw exception
    # and store this image in a lost_embeddings list
    try:
        known_person_encoding = face_recognition.face_encodings(known_person)[0]
    except:
        print('Face encodings cannot be extracted!')
        lost_embeddings.append(image)
        continue

    target_folder = target_dir + '/' + image
    print(target_folder)
    try:
    	os.mkdir(target_folder)
    except:
    	print('Directory with this name already exists!')
    	continue

    person_folder = unknown_dir + '/' + image
    cnt = 0
    i = 1

    # Trying to create a folder for the given person, if the desired person's folder doesn't 
    # exist throw exception and continue with the next person
    try:
        for img in os.listdir(person_folder):
        	# getting encodings of current image in our folder
        	unknown_person = face_recognition.load_image_file(person_folder + '/' + img)
        	encodings = face_recognition.face_encodings(unknown_person)
        	if len(encodings) > 0:                             # if we found a person, then get its encodings
        		unknown_person_encoding = encodings[0] 
        	else:                                              # if no person found in the image, leave this image
        		print('No face found in the image: ', img)
        		continue

        	# compare encodings of current folder image and the anchor image
        	results = face_recognition.compare_faces([known_person_encoding], unknown_person_encoding, 0.50)

        	if results[0] == True:                             # if two people encodings are similar, then save it according to LFW format
        		print(img, ' is the same person')
        		if i == 0:
        			stri = '00'
        		elif 0 < i < 10:
        			stri = '0' + str(i)
        		else:
        			stri = str(i)
        		shutil.copy(person_folder + '/' + img, target_folder + '/' + image + "_00" + stri)
        		i += 1
        	else:
        		print(img, ' is NOT THIS person')
        	cnt += 1
        print('Total images processed in this directory: ', cnt)
    except:
        print('There is NO FOLDER with this name')
        lost_dir.append(image)
        continue
