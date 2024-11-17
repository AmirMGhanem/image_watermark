import os

from PIL import Image

def place_pins_on_image(image_path, pin_path,output_path):
    try:
        base_image = Image.open(image_path)
        if base_image.format == "PNG":
            base_image = base_image.convert("RGB")
        pin_image = Image.open(pin_path)

        image_name = image_path.split("/")[-1]


        base_image_width, base_image_height = base_image.size
        size = min(base_image_width, base_image_height)
        pin_image = pin_image.resize((int(size/20), int(size/20)))


        image_width, image_height = base_image.size
        pin_width, pin_height = pin_image.size


        padding = 0.015  # 10% padding
        pin_positions = [
            (int(padding * image_width), int(padding * image_height)),  # Top-left
            (int(image_width - padding * image_width - pin_width), int(padding * image_height)),  # Top-right
            (int(padding * image_width), int(image_height - padding * image_height - pin_height)),  # Bottom-left
            (int(image_width - padding * image_width - pin_width), int(image_height - padding * image_height - pin_height))  # Bottom-right
        ]


        for position in pin_positions:
            base_image.paste(pin_image, position, pin_image)

        # if directory does not exist, create it
        if not os.path.exists(output_path):
            os.makedirs(output_path)


        output_path= f"{output_path}/{image_name}"
        base_image.save(output_path)
        return base_image
    except Exception as e:
        raise Exception(f"Error in place_pins_on_image: {str(e)}")

