import os
import shutil
import time

# GLOBALS
DEST_FOLDERS = {"Desktop": "C:/Users/ninoc/Desktop", "Documents": "C:/Users/ninoc/Documents", "Music": "C:/Users/ninoc/Music",
                 "Pictures": "C:/Users/ninoc/Pictures", "Videos": "C:/Users/ninoc/Videos"}

downloads = "C:/Users/ninoc/Downloads"

ext_music = ('.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac')
ext_videos = ('.mp4', '.mov', '.wmv', '.avi', 'm4v')
ext_documents = ('.pdf', '.txt')
ext_zip = ('.zip')
ext_images = ('.jpg', '.png', '.jpeg',  '.gif')


def moveHandler(file):
    if file.name.lower().endswith(ext_documents):
        source_path = f"{downloads}/{file.name}"
        shutil.move(src=source_path, dst=DEST_FOLDERS["Documents"])
        print(f"moved {file.name}")

    if file.name.lower().endswith(ext_zip):
        source_path = f"{downloads}/{file.name}"
        shutil.move(src=source_path, dst="{Desktop}/Zips".format(**DEST_FOLDERS))
        print(f"moved {file.name}")

    if file.name.lower().endswith(ext_images):
        source_path = f"{downloads}/{file.name}"
        shutil.move(src=source_path, dst=DEST_FOLDERS["Pictures"])
        print(f"moved {file.name}")

    if file.name.lower().endswith(ext_videos):
        source_path = f"{downloads}/{file.name}"
        shutil.move(src=source_path, dst=DEST_FOLDERS["Videos"])
        print(f"moved {file.name}")

    if file.name.lower().endswith(ext_music):
        source_path = f"{downloads}/{file.name}"
        shutil.move(src=source_path, dst=DEST_FOLDERS["Music"])
        print(f"moved {file.name}")


if __name__ == "__main__":
    downloads_folder = os.scandir(downloads)
    with downloads_folder as entries:
        for entry in entries:
            moveHandler(entry)