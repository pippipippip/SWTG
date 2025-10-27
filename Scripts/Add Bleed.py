from PIL import Image, ImageDraw
import os

def add_bleed_pillow(input_folder, output_folder, frame_type):
    target_size = (1632, 2220)
    image_size = (1500, 2092)


    # Scale the image depending on the frame type.
    scale_ratio = 1

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        print(file)
        if not file.lower().endswith(('.png', '.jpg')):
            continue

        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path).convert("RGB")

	# Set the x, y position of the top corner based on the frame type.
        if frame_type == "withoutbleed":
            x_offset = 66
            y_offset = 60

        if frame_type == "fullart":
            x_offset = 0
            y_offset = 0

        #Create blank canvas
        new_img = Image.new("RGB", target_size, (0,0,0))
        # paste original image to centre
        new_img.paste(img, (x_offset, y_offset))        
        # Scale to 1200dpi resolution
	new_img = new_img.resize((3264, 4440), Image.LANCZOS)

        base_name = os.path.splitext(file)[0]
        out_path = os.path.join(output_folder, base_name + ".png")
        new_img.save(out_path, format="PNG", quality=95, dpi=(1200,1200))
        print("Saved")


# start of main
# From mtgcardbuilder.com creator output (without 1/8 margin)
add_bleed_pillow("..\\Cards\\Without-bleed", "..\\Cards\\1200dpi", "withoutbleed")

# Full art cards already in correct scale with bleed.
add_bleed_pillow("..\\Cards\\Fullart", "..\\Cards\\1200dpi", "fullart")
