#File Organiser 1.0

#Import Libraries
import os
from pathlib import Path

#Path to clean up
CLEANUP_PATH = '/Users/trusty/Downloads/'

#Dictionary
DIRECTORIES = {
	"HTML": [".html5", ".html", ".htm", ".xhtml"],
	"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
			   ".heif", ".psd"],
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
	"Applications": [".exe"]
}

FILE_FORMATS = {
	#Found file type
	file_format: directory
	for directory, file_formats in DIRECTORIES.items()

	#loop found file type through known file types in DIRECTORIES
	for file_format in file_formats
}

#Code Start
def organise():

	#For each 'file' in specified directory
	for entry in os.scandir(CLEANUP_PATH):

		#If file is not a file but a folder, ignore and continue
		if entry.is_dir():
			continue

		#Gets file path (some.file)
		file_path = Path(entry.name)
		full_file_path = Path(CLEANUP_PATH+entry.name)

		#Gets file extension
		file_format = file_path.suffix.lower()

		#If file type exists in DIRECTORIES
		if file_format in FILE_FORMATS:

			#Makes Folder with Directory Name
			directory_path = Path(CLEANUP_PATH+FILE_FORMATS[file_format])
			directory_path.mkdir(exist_ok = True)

			#Moves file from CLEANUP_PATH to DIRECTORIES FOLDER
			full_file_path.rename(directory_path.joinpath(file_path))

		else:
			OtherDirectory = 'Other'
			OtherPath = Path(CLEANUP_PATH+OtherDirectory)
			OtherPath.mkdir(exist_ok = True)

			full_file_path.rename(OtherPath.joinpath(file_path))

if __name__ == "__main__":
	organise()