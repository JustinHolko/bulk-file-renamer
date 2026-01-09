import os

def bulk_rename(folder_path, prefix="file", add_numbers=True):
    """
    Rename all files in the given folder.
    
    Parameters:
    - folder_path: path to the folder containing files
    - prefix: string to add at the start of each file
    - add_numbers: whether to append incremental numbers
    """
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        for i, filename in enumerate(files, start=1):
            name, ext = os.path.splitext(filename)
            new_name = prefix
            if add_numbers:
                new_name += f"_{i}"
            new_name += ext
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        print(f"Renamed {len(files)} files successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    bulk_rename(folder, prefix="renamed")
