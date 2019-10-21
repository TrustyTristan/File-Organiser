# File Organiser 1.1

# Import Libraries
import os
from pathlib import Path

# Path to clean up
Cleanup_Path = '/Users/trusty/Downloads/'

# Dictionary
Directories = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
               ".heif", ".psd"],
    "Vectors": [".ai", ".svg", ".eps", ".dxf"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".txt", ".in", ".out", ".pdf"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Scripts": [".py", ".sh", ".bat", ".ps1"],
    "Arduino": [".ino"],
    "XML": [".xml"],
    "Applications": [".exe"],
    "Fonts": [".ttf", ".ttc", ".pfb", ".pfm", ".otf", ".tfil", ".ffil",
              ".dfont", ".pfa", ".afm", ".woff", ".eot"]
}

File_Formats = {
    # Found file type
    file_format: directory
    for directory, file_formats in Directories.items()

    # loop found file type through known file types in Directories
    for file_format in file_formats
}


# Start


def organise():

    # For each 'file' in specified Cleanup_Path
    for entry in os.scandir(Cleanup_Path):

        # Gets the name of the file
        file_path = Path(entry.name)

        # If file is not a file but a directory or a system file,
        # ignore and continue
        if entry.is_dir() or str(file_path).startswith("."):
            continue
        # Creates the full path to the file we want to sort
        full_file_path = Path(Cleanup_Path+entry.name)

        # Gets file extension
        file_format = file_path.suffix.lower()

        # If file type exists in Directories
        if file_format in File_Formats:

            # Makes Folder with Directory Name
            directory_path = Path(Cleanup_Path+File_Formats[file_format])
            directory_path.mkdir(exist_ok=True)

            # Moves file from Cleanup_Path to Directories FOLDER
            full_file_path.rename(directory_path.joinpath(file_path))

        else:
            OtherDirectory = "Other"
            OtherPath = Path(Cleanup_Path+OtherDirectory)
            OtherPath.mkdir(exist_ok=True)

            full_file_path.rename(OtherPath.joinpath(file_path))


if __name__ == "__main__":
    organise()