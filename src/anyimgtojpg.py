import logging
import os
import shutil
import tkinter as tk
from functools import partial
from tkinter import filedialog

from PIL import Image


# uses src_path as the directory source for images
# then saves them to out_path as .jpg files
def allImgToJpg(
    src_label: tk.Label,
    out_label: tk.Label,
    status_label: tk.Label,
    err_label: tk.Label,
) -> None:
    print("Converting images to jpg...")
    src_path = src_label["text"] + "\\"
    out_path = out_label["text"] + "\\"
    err_path = "err\\"

    if src_path == "\\" or out_path == "\\":
        err_label.config(text="The input or ouput directory is blank")
        return

    f_names = os.listdir(src_path)
    num_files = len(f_names)
    processed_files = 0
    unsupported_files = []

    for file in f_names:
        if file == ".gitkeep":
            continue

        new_f_name = file.split(".")[0] + ".jpg"
        file_path = src_path + file
        try:
            img = Image.open(file_path)
        except:
            if os.path.isdir(file_path):
                logging.error(file + " was a folder")
                continue

            print("Error: The file: " + file + " was not an image")
            unsupported_files.append(file)
            logging.error("The file: " + file + " was not an image")
            shutil.copy(file_path, err_path)
            continue

        img = img.convert("RGB")
        try:
            img.save(out_path + new_f_name, "JPEG")
        except:
            logging.error("Error: The file:" + new_f_name + "could not be saved")
            err_label.config(
                text="Error: The file:" + new_f_name + "could not be saved"
            )
        processed_files = processed_files + 1
        completion_percentage = processed_files / num_files
        status_label["text"] = (
            str(completion_percentage) + "% of folder contents processed"
        )

    status_label["text"] = "Convertion task complete"
    err_count = len(unsupported_files)
    if err_count > 0:
        err_label["text"] = (
            str(err_count)
            + " files were not converted \n The files were transferred to the err folder"
        )
    else:
        err_label["text"] = ""
    print("Convertion complete.")


# changes the *_selected_label text attribute to the selected directory
def get_dir_path(path_label: tk.Label) -> None:
    path_label.config(text=filedialog.askdirectory())


# Check if the err folder exists
if not os.path.isdir("err"):
    os.mkdir("err")
    gk = open("err/.gitkeep", "w")
    gk.write(".")
    gk.close()

# Python logging configuration
logging.basicConfig(
    filename="err/error.log",
    filemode="w",
    format="%(name)s → %(levelname)s: %(message)s",
)

# Start of tkinter gui

# Window Configuration
root = tk.Tk()
root.title("anyimgtojpg")
root.geometry("400x400")
root.resizable(width=False, height=False)

# User gui
src_dialog_label = tk.Label(
    root, text="Select the folder with the images to be converted:"
)
src_selected_label = tk.Label(root, text="")
src_dialog_btn = tk.Button(
    root, text="Input Folder", command=partial(get_dir_path, src_selected_label)
)
src_dialog_label.pack()
src_dialog_btn.pack()
src_selected_label.pack()

out_dialog_label = tk.Label(
    root, text="Select the folder where the images will be saved"
)
out_selected_label = tk.Label(root, text="")
out_dialog_btn = tk.Button(
    root, text="Output Folder", command=partial(get_dir_path, out_selected_label)
)
out_dialog_label.pack()
out_dialog_btn.pack()
out_selected_label.pack()

status_label = tk.Label(root, text="")
status_label.config(fg="#0A7A16")
err_label = tk.Label(root, text="")
err_label.config(fg="#FF0000")
conv_files_btn = tk.Button(
    root,
    text="Convert Images",
    command=partial(
        allImgToJpg, src_selected_label, out_selected_label, status_label, err_label
    ),
)
conv_files_btn.pack()
status_label.pack()
err_label.pack()

root.mainloop()
