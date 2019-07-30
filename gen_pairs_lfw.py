#! encoding: utf-8

import os
import random
import argparse

class GeneratePairs:
    """
    Generate the pairs.txt file that is used for training face classifier when calling python `src/train_softmax.py`.
    Or others' python scripts that needs the file of pairs.txt.

    Doc Reference: http://vis-www.cs.umass.edu/lfw/README.txt
    """

    def __init__(self, data_dir, pairs_filepath, img_ext):
        """
        Parameter data_dir, is your data directory.
        Parameter pairs_filepath, where is the pairs.txt that belongs to.
        Parameter img_ext, is the image data extension for all of your image data.
        """
        self.data_dir = data_dir
        self.pairs_filepath = pairs_filepath
        self.img_ext = img_ext


    def generate(self):
        for i in range(10):
            self._generate_matches_pairs()
            self._generate_mismatches_pairs()


    def _generate_matches_pairs(self):
        """
        Generate all matches pairs
        """
        for name in os.listdir(self.data_dir):
            if name == ".DS_Store":
                continue

            a = []
            for file in os.listdir(self.data_dir + name):
                if file == ".DS_Store":
                    continue
                a.append(file)

            with open(self.pairs_filepath, "a") as f:
                for i in range(3):
                    temp = random.choice(a).split("_") # This line may vary depending on how your images are named.
                    w = temp[0] + "_" + temp[1]
                    l = random.choice(a).split("_")[2].lstrip("0").rstrip(self.img_ext)
                    r = random.choice(a).split("_")[2].lstrip("0").rstrip(self.img_ext)
                    f.write(w + "\t" + l + "\t" + r + "\n")


    def _generate_mismatches_pairs(self):
        """
        Generate all mismatches pairs
        """
        for i, name in enumerate(os.listdir(self.data_dir)):
            if name == ".DS_Store":
                continue

            remaining = os.listdir(self.data_dir)
            remaining = [f_n for f_n in remaining if f_n != ".DS_Store"]
            # del remaining[i] # deletes the file from the list, so that it is not chosen again
            other_dir = random.choice(remaining)
            with open(self.pairs_filepath, "a") as f: 
                for i in range(3):
                    file1 = random.choice(os.listdir(self.data_dir + name))
                    # print('first', file1, name)
                    file2 = random.choice(os.listdir(self.data_dir + other_dir))
                    # print('second', file2, other_dir)
                    number_1 = file1.split("_")[2].lstrip("0").rstrip(self.img_ext)
                    number_2 = file2.split("_")[2].lstrip("0").rstrip(self.img_ext)
                    # print(number_1, number_2)
                    # f.write(name + "\t" + file1.split("_")[2].lstrip("0").rstrip(self.img_ext) + "\n")
                    f.write(name + "\t" + number_1 + "\t" + other_dir + "\t" + number_2 + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')
    parser.add_argument('--data-dir', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
    parser.add_argument('--txt-file', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
    # reading the passed arguments
    args = parser.parse_args()
    data_dir = args.data_dir    # "out_data_crop/"
    pairs_filepath = args.txt_file         # "pairs_1.txt"
    
    img_ext = ".jpg"
    generatePairs = GeneratePairs(data_dir, pairs_filepath, img_ext)
    generatePairs.generate()

