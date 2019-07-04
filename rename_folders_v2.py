import os
import pathlib
import argparse
import fnmatch
import re

parser = argparse.ArgumentParser(description='Rename folders containing collected data according to => Name_Surname => formatting')
# general
parser.add_argument('--data-dir', default='', help='full path to the directory with collected images without formatting of folder names')

args = parser.parse_args()
dataset_dir = args.data_dir

folder_names = []
for name in os.listdir(dataset_dir):
    new_name = re.sub('[^A-Za-z0-9]+', '', name)
    print(new_name)
    new_name = new_name[0].upper() + new_name[1:len(new_name)/2] + '_' + new_name[len(new_name)/2].upper() + new_name[(len(new_name)/2)+1:]
    print(new_name)
    name = os.path.join(dataset_dir, name)
    new_name = os.path.join(dataset_dir, new_name)
    # print("New Name - "+file_name.translate(None, "0123456789")) # removing numbers from name
    os.rename(name, new_name)
    folder_names.append(new_name)

'''
for name in os.listdir(dataset_dir):
    new_name = ''.join(e for e in name if e.isalnum())
    print(new_name)
    name = os.path.join(dataset_dir, name)
    new_name = os.path.join(dataset_dir, new_name)      
    os.rename(name, new_name)
''' 