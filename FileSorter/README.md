# File Organizer Script

This Python script organizes files in a directory by sorting them into subfolders based on their file extensions. For example, all `.txt` files are moved to a folder named `txt`, `.png` files to a folder named `png`, and so on. After sorting, the script removes any empty folders left behind.

## How It Works

The script performs the following steps:

1. **Prompt for Directory**  
   The user provides a directory path to organize.

2. **Sort Files**  
   - The script scans all files in the directory (including subdirectories).  
   - Each file is moved to a folder named after its extension (e.g., `.jpg` → `jpg` folder).

3. **Remove Empty Folders**  
   Any empty directories remaining after sorting are deleted.

4. **Completion Message**  
   The script confirms when the sorting process is complete.

## Example

### Before Running the Script

```
test_folder/
   ├── file1.txt
   ├── image1.png
   ├── music1.mp3
   └── subdir/
       ├── file2.txt
       └── image2.jpg
```


### After Running the Script

```
test_folder/
   ├── txt/
   │   ├── file1.txt
   │   └── file2.txt
   ├── png/
   │   └── image1.png
   ├── mp3/
   │   └── music1.mp3
   └── jpg/
       └── image2.jpg
```