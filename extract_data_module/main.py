import os
from .scrape import download_zips
from .utils import get_zip_filenames, get_zip_id, unzip, clean_dir

def get_data_folder(num_quarterly_periods):
    base = './data'
    os.mkdir(base) # top level directory for downloaded data
    download_zips(num_quarterly_periods)
    zip_files = get_zip_filenames()
    for z_file in zip_files:
        zip_id = get_zip_id(z_file)
        destination_path = f'{base}/{zip_id}'
        unzip(z_file, destination_path) # unzip to path
        clean_dir(destination_path) # clean, rename files in path
        os.remove(z_file) # get rid of used zip file