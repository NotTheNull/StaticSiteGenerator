import shutil
import os


def main():
    prep_core_files()

DESTINATION_FOLDER = "./public"
SOURCE_FOLDER = "./static"

def prep_core_files():
    __purge_public()
    __copy(SOURCE_FOLDER, DESTINATION_FOLDER)
    

def __purge_public():
    shutil.rmtree(DESTINATION_FOLDER)
    os.mkdir(DESTINATION_FOLDER)

def __copy(src_path, dest_path):
    if os.path.isfile(src_path):
        shutil.copy(src_path, dest_path)
    else:
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)

        for path in os.listdir(src_path):
            __copy(os.path.join(src_path, path), os.path.join(dest_path, path))

    


main()
