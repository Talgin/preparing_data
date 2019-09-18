# preparing_data
Data preparation to use with our deep learning face recognition system

renamer.py - module to rename names of images in our dataset folder (format: Name_Surname_0001.png, Name_Surname_0002.png, etc.)

With any questions regarding usage, please send me a message to islamgozhayev@yandex.ru

----- ADDITIONAL NOTES -----

1. Collect dataset => refine, delete advertisement pages
2. Crop faces from images with multiple people in one folder => crop.py => python crop.py --data-dir /home/ti/path_to_uncropped_data --target-dir /home/ti/path_to_destination_directory
3. Refine folder names and images => rename_folders_v2.py (e.g. python rename_folders_v2.py --data-dir /home/ti/Downloads/crop_and_find/faces501) (this module renames folder names of each person: it merges all the letters, removing special characters (.,-, etc) and splits the remaining string into two parts in the middle with underline '_' renamer_lfw.py (rename image names according to LFW dataset format)
4. From each folder select one person's image as an anchor (you will be comparing each image in this folder with anchor image to leave only one person's images) => place these images in known_dir with and rename each one according to this person's folder name (if folder name was John_Hopkins, anchor name should be John_Hopkins.jpg)
5. Select faces that correspond only to the anchored person => recognize_and_store.py --known_dir /path/to/dir/with/anchor/people --unknown-dir /path/to/dir/with/images/divided/into/folders --target-dir /path/to/dir/where/to/save/the/resulting/folders (this module looks at the image in the known folder and compares it with other images in this person's folder)
6. Divide into Train (80), Valid (10), Test (10) 
7. Align faces with - align_dataset_mtcnn_v1.py
8. create .lst file with - insightface_pairs_gen.py => use write_lst function
9. create .rec, .idx files using - face2rec2.py  
10. create pairs.txt file using gen_pairs_lfw.py => if you don't have loop in generate() function you have to write it with range(10), because you have to create 10-folds cross validation .bin
11. create .bin file using dataset2bin.py => usage: python dataset2bin.py --data-dir /your/dataset/directory --image-size 112,112 --output /output/directory/to/dave/bin 
12. Yahoooooo, STAAAAARRRRTTTT TRRRRRRAAAAAIIIIINIIIING!!!

EXAMPLE FOLDERS: https://www.dropbox.com/s/i10tma4zqygdxdm/data.zip?dl=0

EXTRA: Parse folder with face_recognition => count number of occurences of each descriptor of the image => 
If one descriptor appears more than 10 times => write it to another folder

EXTRA1: Before cropping faces from collective images: 
- take known image
- parse folder with images of this person
- take one image
- run dlib's get_frontal_face_detector on it
- compare each face with known image using face_recognition library
- save the most similar one/ones
- check each folder by hand
