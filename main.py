import os
from PIL import Image
import random



# Get all image files
folder_path = r"C:\Users\ASUS\Desktop\e\collage maker\final"
images = [img for img in os.listdir(folder_path)
          if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

print(f"Total images found: {len(images)}")


template_path = r"C:\Users\ASUS\Desktop\collage maker\93f5a211e50d885f950807ef5e1c3508.jpg"
template_image = Image.open(template_path)



random.shuffle(images)

groups = [images[i:i+6] for i in range(0, len(images), 6)]

groups = [g for g in groups if len(g) == 6]

print(f"Total groups (collages): {len(groups)}")

# Overlay images on template (core logic)

positions = [
    (50, 50, 300, 300),
    (400, 50, 300, 300),
    (750, 50, 300, 300),
    (50, 400, 300, 300),
    (400, 400, 300, 300),
    (750, 400, 300, 300)
]

collages = []

for group in groups:

    temp = Image.open(template_path).copy()

    for img_name, pos in zip(group, positions):

        img_path = os.path.join(folder_path, img_name)
        img = Image.open(img_path)

        x, y, w, h = pos
        img = img.resize((w, h))

        temp.paste(img, (x, y))  # ← overlay

    collages.append(temp)

output_folder = "output_collages"
os.makedirs(output_folder, exist_ok=True)

for i, collage in enumerate(collages, start=1):
    collage.save(os.path.join(output_folder, f"collage_{i}.png"))

print("All collages saved successfully 🚀")



