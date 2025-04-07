import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

# Configuration
input_folder = './art'       # Folder with original images
output_folder = './art-cv'     # Folder to save compressed images
quality = 75                     # Compression quality for all images
max_size_mb = 10                 # Threshold size in MB
resize_max_width = 1920         # Resize dimensions if image is too big
resize_max_height = 1920

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

def compress_and_resize_image(input_path, output_path, resize=False):
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        if resize:
            img.thumbnail((resize_max_width, resize_max_height))  # Resize proportionally

        img.save(output_path, optimize=True, quality=quality)

def process_images():
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            input_path = os.path.join(input_folder, "invisible_ink.png")
            output_path = os.path.join(output_folder, "invisible_ink.png")

            try:
                file_size_mb = os.path.getsize(input_path) / (1024 * 1024)
                needs_resize = file_size_mb > max_size_mb

                compress_and_resize_image(
                    input_path=input_path,
                    output_path=output_path,
                    resize=needs_resize
                )

                if needs_resize:
                    print(f"Compressed & Resized: {filename} ({file_size_mb:.2f}MB)")
                else:
                    print(f"Compressed Only: {filename} ({file_size_mb:.2f}MB)")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
        break

if __name__ == "__main__":
    process_images()