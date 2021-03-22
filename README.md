# preparing_data
Face Data preparation process to train a model for deep learning face recognition system

renamer.py - module to rename names of images in our dataset folder (format: Name_Surname_0001.png, Name_Surname_0002.png, etc.)

With any questions regarding usage, please send me a message to islamgozhayev@yandex.ru

----- ADDITIONAL NOTES -----

1. Collect dataset => refine, delete non-people images
2. Crop faces from images with multiple people in one folder => crop.py => python crop.py --data-dir /home/ti/path_to_uncropped_data --target-dir /home/ti/path_to_destination_directory
3. Refine folder names and images => rename_folders_v2.py (e.g. python rename_folders_v2.py --data-dir /home/ti/Downloads/crop_and_find/faces501) (this module renames folder names of each person: it merges all the letters, removing special characters (.,-, etc) and splits the remaining string into two parts in the middle with underline '_' renamer_lfw.py (rename image names according to LFW dataset format)
4. From each folder select one person's image as an anchor (you will be comparing each image in this folder with anchor image to leave only one person's images) => place these images in known_dir with and rename each one according to this person's folder name (if folder name was John_Hopkins, anchor name should be John_Hopkins.jpg)
5. Select faces that correspond only to the anchored person => recognize_and_store.py --known_dir /path/to/dir/with/anchor/people --unknown-dir /path/to/dir/with/images/divided/into/folders --target-dir /path/to/dir/where/to/save/the/resulting/folders (this module looks at the image in the known folder and compares it with other images in this person's folder)
6. Align faces with - align_dataset_mtcnn_v1.py (UPD: Changed places with next, some images may not be aligned, so it is good to align first and divide into sets after) - this is revised code from https://github.com/davidsandberg/facenet/blob/master/src/align/align_dataset_mtcnn.py so, in order for this to work properly you have to place it in original folder because it has some linked modules.
7. Divide into Train (80), Valid (10), Test (10) - train_valid.py and train_test.py the remaining data will be your train set
8. create .lst file with - insightface_pairs_gen.py => use write_lst function
9. create .rec, .idx files using - face2rec2.py (UPD: This code is from https://github.com/deepinsight/insightface/tree/master/src/data directory and has link to other modules in it)
10. create pairs.txt file using gen_pairs_lfw.py => if you don't have loop in generate() function you have to write it with range(10), because you have to create 10-folds cross validation .bin (UPD: for this you have to use your validation(verification) set)
11. create .bin file using dataset2bin.py => usage: python dataset2bin.py --data-dir /your/dataset/directory --image-size 112,112 --output /output/directory/to/dave/bin (UPD: here you also pass a route to your validation(verification) set) -- dataset2bin.py uses some modules from https://github.com/deepinsight/insightface/tree/master/src/eval 
12. Yahoooooo, STAAAAARRRRTTTT TRRRRRRAAAAAIIIIINIIIING!!!

EXAMPLE FOLDERS: https://www.dropbox.com/s/i10tma4zqygdxdm/data.zip?dl=0

EXTRA1 (This process can save you some time): Before cropping faces from collective images: 
- take known image
- parse folder with images of this person
- take one image
- run dlib's get_frontal_face_detector on it
- compare each face on this image with known image using face_recognition library
- save the most similar one
- repeat this process until you finish with all of the images from this person's folder
- check each folder by hand

NOTE: There are a lot of tools like Amazon Turk, Toloka, etc. that can help you with annotations (of course it will cost some money :) ).   
