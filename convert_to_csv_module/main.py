import os
from .convert import handle_quarter_folder

def convert_txt_files_to_csv():
    base = './data'
    output_base = './csv'
    os.mkdir(output_base)

    quarter_folders = os.listdir(base)
    for quarter_folder in quarter_folders:
        input_path = f'{base}/{quarter_folder}'
        output_path = f'{output_base}/{quarter_folder}'
        os.mkdir(output_path) # handle_quarter_folder needs a place to put output files
        handle_quarter_folder(input_path, output_path)
        