# preparing_data
Data preparation to use with our deep learning face recognition system

insightface_paris_gen.py - module to generate pairs of images and their identity (1 if the same person, 0 if different)

renamer.py - module to rename names of images in our dataset folder (format: Name_Surname_0001.png, Name_Surname_0002.png, etc.)

With any questions regarding usage, please send me a message to islamgozhayev@yandex.ru

----- ADDITIONAL NOTES -----

1. Collect dataset 												=> ready ------------------------------ refine, delete advertisement pages
2. Crop faces from images with multiple people in one folder 	=> ready ------------------------------ crop.py => python crop.py --data-dir /home/ti/path_to_uncropped_data --target-dir /home/ti/																												path_to_destination_directory
3. Refine folder names and images 								=> ready ------------------------------ rename_folders_v2.py (e.g. python rename_folders_v2.py --data-dir /home/ti/Downloads/crop_and_find/																										   faces501) (this module renames folder names of each person: it merges all the letters, removing 																											sepcial characters (.,-, etc) and splits the remaining string into two parts in the middle with 																										underline '_'
																		 ------------------------------	renamer_lfw.py (rename image names according to LFW dataset format)
4. Select faces that correspond only to the anchored person 	=> ready/revise ----------------------- recognize_and_store.py --known_dir /path/to/dir/with/anchor/people --unknown-dir /path/to/dir/with/																										   images/divided/into/folders --target-dir /path/to/dir/where/to/save/the/resulting/folders (this 																											module looks at the image in the known folder and compares the images with this images in this 																											person's folder)
5. Divide into Train (80), Valid (10), Test (10)				=> in progress ------------------------ 
6. Align faces with - align_dataset_mtcnn_v1.py					=> ready
7. create .lst file with - insightface_pairs_gen.py --use write_lst function => ready
8. create .rec, .idx files using - face2rec2.py 				=> ready
9. create pairs.txt file using gen_pairs_lfw.py 				=> if you don't have loop in generate() function you have to write it with range(10), because you have to create 10-folds cross validation .bin
10. create .bin file using dataset2bin.py by setting 			=> ready ------------------------------ usage: python dataset2bin.py --data-dir /your/dataset/directory --image-size 112,112 --output /output/directory/to/dave/bin
11. Yahoooooo, STAAAAARRRRTTTT TRRRRRRAAAAAIIIIINIIIING!!!
