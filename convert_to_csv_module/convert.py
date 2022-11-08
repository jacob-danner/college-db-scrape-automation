from .utils import clean_file, parse_line, write_csv, make_output_path
import os

def convert_to_csv(file_input_path, file_output_path):
    file_lines = clean_file(file_input_path)
    clean_lines = [parse_line(line) for line in file_lines]
    write_csv(clean_lines, file_output_path) 


def handle_quarter_folder(input_path, output_path):
    txt_files = os.listdir(input_path)
    for txt_file in txt_files:
        file_input = f'{input_path}/{txt_file}'
        file_output = make_output_path(output_path, txt_file)
        convert_to_csv(file_input, file_output)