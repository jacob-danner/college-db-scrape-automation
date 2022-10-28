import os
from scrape import download_zip
from utils import get_zip_filename, unzip, clean_dir

def main():
    download_zip()
    zip_file = get_zip_filename()
    destination_path = 'data'
    unzip(zip_file, destination_path) # unzip to path
    clean_dir(destination_path) # clean, rename files in path
    os.remove(zip_file) # get rid of used zip file

main()