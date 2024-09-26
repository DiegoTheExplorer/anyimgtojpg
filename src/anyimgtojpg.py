from PIL import Image
import os
import logging

import tkinter as tk
from tkinter import filedialog
from functools import partial

# uses src_path as the directory source for images
# then saves them to out_path as .jpg files
def allImgToJpg(src_label: tk.Label, out_label: tk.Label, err_label: tk.Label) -> None:
    print("Converting images to jpg...")
    src_path = src_label["text"] + "\\"
    out_path = out_label["text"] + "\\"
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
            logging.error("Error: The file:" + new_f_name + "could not be saved")
            err_label.config(text="Error: The file:" + new_f_name + "could not be saved")

    print("Convertion complete.")    

# changes the *_selected_label text attribute to the selected directory
def get_dir_path(path_label: tk.Label) -> None:
    path_label.config(text=filedialog.askdirectory())

# Start of tkinter gui
root = tk.Tk()
root.title("anyimgtojpg")

src_dialog_label = tk.Label(root, text="Select the folder with the images to be converted:")
src_selected_label = tk.Label(root)
src_dialog_btn = tk.Button(root, text="Input Folder", command=partial(get_dir_path, src_selected_label))
src_dialog_label.pack()
src_dialog_btn.pack()
src_selected_label.pack()

out_dialog_label = tk.Label(root, text="Select the folder where the images will be saved")
out_selected_label = tk.Label(root)
out_dialog_btn = tk.Button(root, text="Output Folder", command=partial(get_dir_path, out_selected_label))
out_dialog_label.pack()
out_dialog_btn.pack()
out_selected_label.pack()

err_label = tk.Label(root, text="")
conv_files_btn = tk.Button(root, text="Convert Images", command=partial(allImgToJpg, src_selected_label, out_selected_label, err_label))
conv_files_btn.pack()
err_label.pack()

root.mainloop()
