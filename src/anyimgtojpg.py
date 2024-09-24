from PIL import Image
import os

src_path = "../inp/"
out_path = "../out"

def conv_all_in_dir(src_path: str, out_path: str):
    print("Converting images to jpg...")

    f_names = os.listdir(src_path)

    for file in f_names:
        if(file == '.gitkeep'):
            continue
        new_f_name = file.split(".")[0]
        img = Image.open(src_path + file)
        img = img.convert('RGB')
        img.save(out_path + new_f_name + ".jpg", "JPEG")

    print("Convertion complete.")    

conv_all_in_dir(src_path, out_path)
