import os
from PIL import Image, ExifTags

def compress_image(input_path, output_path, quality=85):
    try:
        img = Image.open(input_path)
        
        # Check if image has EXIF data
        if hasattr(img, '_getexif'):
            exif = img._getexif()
            if exif:
                orientation = exif.get(274)
                if orientation in [3, 6, 8]:
                    # Rotate image according to EXIF orientation
                    img = img.rotate({
                        3: 180,
                        6: 270,
                        8: 90
                    }[orientation], expand=True)

        # Save the image without flipping or rotating
        img.save(output_path, "JPEG", optimize=True, quality=quality, exif=img.info.get('exif'))
        print(f'Compressed {os.path.basename(input_path)}')
    except Exception as e:
        print(f'Error compressing {os.path.basename(input_path)}: {e}')

def compress_images_in_folder(folder_path, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename.rsplit('.', 1)[0] + '.jpg')  # Output as JPEG
            compress_image(input_path, output_path, quality)

# Example usage:
input_folder = './original_image'
output_folder = './picture'
compress_images_in_folder(input_folder, output_folder, quality=30)
