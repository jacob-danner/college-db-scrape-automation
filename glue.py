import typer

from extract_data_module.main import get_data_folder
from convert_to_csv_module.main import convert_txt_files_to_csv
from convert_to_tables_module.main import convert_csv_to_tables

def main(num_quarterly_periods):
    num_quarterly_periods = int(num_quarterly_periods)
    print(f'downloading the data from the last {num_quarterly_periods} quarterly periods...')    
    get_data_folder(num_quarterly_periods)
    print('converting downloaded .txt files to .csv fromat...')    
    convert_txt_files_to_csv()
    print('extracting sql ready tables from each .csv file')
    convert_csv_to_tables()

if __name__ == "__main__":
    typer.run(main)