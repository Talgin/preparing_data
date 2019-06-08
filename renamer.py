import os
import pathlib

root = r"C:\Users\TengriLab\Desktop\DOCUMENTATION\preparing_data\our_dataset\Aiya_Shalkar"

for path, subdirs, files in os.walk(root):
    i = 1
    for name in files:
        extension = name.split(".")[-1].lower()
        if extension != "png":
            continue
        if i == 0:
            stri = '00'
        elif 0 < i < 10:
            stri = '0' + str(i)
        else:
            stri = str(i)
        os.rename(os.path.join(path, name), os.path.join(path, os.path.basename(path) + "_00" + stri + '.' + extension))
        i = i + 1
        print(os.path.basename(path))
