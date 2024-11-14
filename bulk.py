# Example usage
import os

from main import place_pins_on_image


src_folder = "images/"
new_folder = "output_images/"
pin_image_path = "pin.png"
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
for image_name in os.listdir(src_folder):
    base_image_path = os.path.join(src_folder, image_name)
    place_pins_on_image(base_image_path, pin_image_path)
#     save the image in the new folder
    new_image_path = os.path.join(new_folder, image_name)
    os.rename("output_image.jpg", new_image_path)

print("All images have been processed and saved in the output_images folder.")


