import os
from .utils import get_date
from .table_logic import make_tables

def convert_csv_to_tables():
    input_base = './csv'
    output_base = './tables'
    os.mkdir(output_base)
    quarter_folders = os.listdir(input_base)
    for quarter_folder in quarter_folders:
        date = get_date(quarter_folder) # date has properties; date.year, date.quarter
        csv_files = os.listdir(f'{input_base}/{quarter_folder}')
        for csv in csv_files:
            input_path = f'{input_base}/{quarter_folder}/{csv}'

            # make folder for each csv so tables can be stored there
            csv_folder_name = csv.replace('.csv', '') # folder name = csv name stripped of .csv
            output_path = f'{output_base}/{csv_folder_name}'
            os.mkdir(output_path)

            # create csv tables for each column in original csv 
            make_tables(input_path, output_path, date)
            