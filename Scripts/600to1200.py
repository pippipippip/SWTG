from PIL import Image, ImageDraw
import os

input_folder = "C:\\Users\\Phillip\\Documents\\SWTG5 Rewritten\\For printing"


for file in os.listdir(input_folder):
    print(file)
    if not file.lower().endswith(('.png', '.jpg')):
        continue

    img_path = os.path.join(input_folder, file)
    img = Image.open(img_path).convert("RGB")
    img = img.resize((3264, 4440), Image.LANCZOS)

    base_name = os.path.splitext(file)[0]
    out_path = os.path.join("C:\\Users\\Phillip\\Documents\\SWTG5 Rewritten\\1200", base_name + ".png")
    img.save(out_path, format="PNG", quality=95, dpi=(1200,1200))
    print("Saved")
