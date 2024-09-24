from PIL import Image
import os

print("Converting images to jpg...")

src_path = "../inp/"
out_path = "../out"

f_names = os.listdir(src_path)
unsupported_files = []

for file in f_names:
    new_f_name = file.split(".")[0]
    img = Image.open(src_path + file)
    img = img.convert('RGB')
    img.save(out_path + new_f_name + ".jpg", "JPEG")

print("Convertion complete.")    
