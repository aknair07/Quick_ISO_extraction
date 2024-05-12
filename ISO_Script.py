import zipfile
import shutil
import os
from selenium import webdriver


zip_directory = ""
directory = ""
re_download = directory + "\\re_download"

def remove_text_file():
    ''' Deletes any files that are not of the .ISO format.  '''
    test = os.listdir( directory )
    for item in test:
        if item.endswith(".TXT") or item.endswith(".pkg") or item.endswith(".rap"):
            os.remove( os.path.join( directory, item ) )
    return

def count_iso():
    ''' Counts the number of iso files in the current directoy. '''
    c = 0
    directory = "F:\\PS3ISO"
    test = os.listdir( directory )
    for item in test:
        if item.endswith(".iso"):
            c += 1
    return c

def unzip_files():
    ''' Unzips all files in the source directory into destination directory. '''
    test = os.listdir( zip_directory )
    c = count_iso()
    for item in test:
        if item.endswith(".zip"):
            with zipfile.ZipFile(os.path.join( zip_directory, item ),"r") as zip_ref:
                print(f'Extracting {item}')
                zip_ref.extractall( directory )
                remove_text_file()
            new_c = count_iso()
            if new_c > c:
                print('Extraction Successfull')
                os.remove(os.path.join( zip_directory, item ))
                c = new_c
            else:
                shutil.move(os.path.join( zip_directory, item ), os.path.join( re_download, item ))
                print("###############################")
                print(f'Re-Donwload {item}')
                print("###############################")
    return


