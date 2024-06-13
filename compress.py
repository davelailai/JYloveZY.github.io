import os
from PIL import Image

def compress_image(input_path, output_path, quality=85):
    img = Image.open(input_path)
    img.save(output_path, "JPEG", optimize=True, quality=quality)

def compress_images_in_folder(folder_path, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg','.JPG','HEIC')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            compress_image(input_path, output_path, quality)
            print(f'Compressed {filename}')

# Example usage:
input_folder = './picture'
output_folder = './compressed_images'
compress_images_in_folder(input_folder, output_folder, quality=60)
