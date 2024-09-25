from PIL import Image
import os
import logging

src_path = "../inp/"
out_path = "../out"

def conv_all_in_dir(src_path: str, out_path: str) -> None:
    print("Converting images to jpg...")

    f_names = os.listdir(src_path)
    unsupported_files = []

    for file in f_names:
        if(file == '.gitkeep'):
            continue

        new_f_name = file.split(".")[0] + ".jpg"
        try:
            img = Image.open(src_path + file)
        except:
            print("Error: The file: " + file + " was not an image")
            unsupported_files.append(file)
            logging.error("The file: " + file + " was not an image")
            continue

        img = img.convert('RGB')
        try:
            img.save(out_path + new_f_name , "JPEG")
        except:
            print("Error: The file:" + new_f_name + "could not be saved")
            logging.error("Error: The file:" + new_f_name + "could not be saved")

    print("Convertion complete.")    

conv_all_in_dir(src_path, out_path)
