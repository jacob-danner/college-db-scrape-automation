import os
from scrape import download_zips
from utils import get_zip_filenames, get_zip_id, unzip, clean_dir

def main():
    os.mkdir('data') # top level directory for downloaded data
    download_zips(num_quarterly_periods=10)
    zip_files = get_zip_filenames()
    for z_file in zip_files:
        zip_id = get_zip_id(z_file)
        destination_path = f'data/{zip_id}'
        unzip(z_file, destination_path) # unzip to path
        clean_dir(destination_path) # clean, rename files in path
        os.remove(z_file) # get rid of used zip file

main()