import os
from PIL import Image

def compress_image(image_path, output_path, quality):
    """
    Compress an image while maintaining the original dimensions.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Ensure the image is in RGB mode for JPG format
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save the image with the specified quality
        img.save(output_path, "JPEG", quality=quality)
        print(f"Compressed image saved at: {output_path}")
    except Exception as e:
        print(f"Error compressing image {image_path}: {e}")


def process_directory(input_directory, output_directory, quality):
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Loop through all files in the directory
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        # Check if it's a file and ends with a valid image extension
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Set the output path for the compressed image
            output_path = os.path.join(output_directory, filename)
            
            # Compress the image
            compress_image(file_path, output_path, quality)
        else:
            print(f"Skipping non-image file: {filename}")


if __name__ == "__main__":
    # Get input from the user for directories and compression quality
    input_dir = input("Enter the path to the input directory (where original images are located): ")
    output_dir = input("Enter the path to the output directory (where compressed images will be saved): ")
    compression_quality = int(input("Enter the compression quality (1-100, higher is better quality): "))

    # Validate quality input
    if compression_quality < 1 or compression_quality > 100:
        print("Invalid quality value. Please enter a number between 1 and 100.")
    else:
        # print("Nothing heree..... ")
        # Run the batch compression
        # batch_compress_images(input_dir, output_dir, compression_quality)
        # compress_image(input_dir, output_dir, compression_quality)
        process_directory(input_dir, output_dir, compression_quality)