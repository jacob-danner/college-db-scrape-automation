import pandas as pd
import csv

# CLEAN FILE
# return cleaned list of file_lines
def clean_file(filename):
    file = open(filename, 'r')
    file_lines = file.readlines()

    # throw away junk descriptor line at index 1
    del file_lines[1]

    cleaned = []
    for line in file_lines:
        line = line.replace('\n', '')
        line = line[:-1] # remove trailing \t. 
        cleaned.append(line)
    
    return cleaned



# PARSE LINES
# helper for parse_line
def if_na_then_fill(column):
    if column == '':
        return pd.NA
    else:
        return column

def parse_line(line: str):
    line = line.split('\t')
    line = [if_na_then_fill(column) for column in line]    
    return line

    
    
    
# CREATE OUTPUT PATH FOR CSV
def make_output_path(base_path, filename):
    output_filename = filename.replace('txt', 'csv') 
    output_path = f'{base_path}/{output_filename}'
    return output_path


# OUTPUT TO CSV
def write_csv(rows, output_filename):
    with open(output_filename, 'w') as f:
        write = csv.writer(f)
        write.writerows(rows)