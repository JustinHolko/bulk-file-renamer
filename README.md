---

# Bulk File Renamer

A simple Python tool to quickly rename and organize large groups of files.

---

## Features

* Bulk rename all files in a folder
* Add a prefix and sequential numbers
* Keeps original file extensions intact
* Minimal setup, easy to use

---

## Installation

1. Make sure you have **Python 3** installed.

2. Clone this repository:

   git clone [https://github.com/JustinHolko/bulk-file-renamer.git](https://github.com/JustinHolko/bulk-file-renamer.git)

3. Navigate into the folder:

   cd bulk-file-renamer

---

## Usage

1. Run the script:

   python bulk_renamer.py

2. Enter the **full folder path** when prompted.

3. Enter a **prefix** for renamed files (default example: `renamed`).

4. All files in the folder will be renamed automatically.

---

## Example

Original files in folder:

```
photo 1.jpg
photo 2.jpg
document.txt
```

After running:

```
renamed_1.jpg
renamed_2.jpg
renamed_3.txt
```

---

## Future Improvements

* Trim spaces and special characters in filenames
* Add a **preview mode** before renaming
* GUI version for drag-and-drop functionality
* Custom rename patterns

---

## License

MIT License

---
