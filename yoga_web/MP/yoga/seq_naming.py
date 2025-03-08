import os
import hashlib

def calculate_hash(image_path):
    """
    Calculate the MD5 hash of an image file.
    Args:
        image_path: Path to the image file.
    Returns:
        Hash string for the image.
    """
    with open(image_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash

def rename_and_remove_duplicates(folder_path, output_folder):
    """
    Remove exact duplicates and rename all image files sequentially.
    Args:
        folder_path: Path to the folder containing the images.
        output_folder: Path to the folder where renamed images will be saved.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    os.makedirs(output_folder, exist_ok=True)
    seen_hashes = set()
    count = 1

    for filename in sorted(os.listdir(folder_path)): 
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):  
            old_path = os.path.join(folder_path, filename)

            
            img_hash = calculate_hash(old_path)
            if img_hash in seen_hashes:
                print(f"Duplicate found: {filename} - Skipping")
                continue
            seen_hashes.add(img_hash)

            
            new_filename = f"{count}.jpg"  
            new_path = os.path.join(output_folder, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
            count += 1

    print(f"Processing completed. Renamed {count - 1} unique files.")


input_folder = "C:/Users/inoug/Desktop/Dataset/mountain"  
output_folder = "C:/Users/inoug/Desktop/Dataset/mountain_pose"  
rename_and_remove_duplicates(input_folder, output_folder)