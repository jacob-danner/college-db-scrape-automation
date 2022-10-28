import os
import zipfile

def get_zip_filename():
    filenames = os.listdir()
    
    for f_name in filenames:
        if '.zip' in f_name:
            zip_file = f_name

    return zip_file
    

def unzip(zip_file, destination_path):
    cwd = os.getcwd()
    data_dir = f'{cwd}/{destination_path}'
    os.mkdir(data_dir)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(data_dir)


# rename files clean_dir() = main funciton. all other are helpers
def clean_element(el):
    # get substring between ()
    start = el.find('(')
    stop = el.find(')') + 1
    to_replace = el[start:stop]

    part_num = ' ' + to_replace[1]

    el = el.replace(to_replace, part_num)
    return el

def get_old_and_cleaned(filename_lengths):
    files_with_parts = [x for x in filename_lengths if filename_lengths[x] == 8]
    other_files      = [x for x in filename_lengths if filename_lengths[x] != 8]

    old_names = files_with_parts + other_files

    files_with_parts = [clean_element(x) for x in files_with_parts]
    clean_list = files_with_parts + other_files

    return old_names, clean_list 

def remove_junk(el):
    el = el.split()
    important = el[2:]
    final_name = '_'.join(important)

    return final_name

def get_pairs(old_names, cleaned_names):
    pairs = []
    for i in range(len(old_names)):
        row = (old_names[i], cleaned_names[i])
        pairs.append(row)

    return pairs

def make_new_names(dir):
    files = os.listdir(dir)
    filename_lengths = {x: len(x.split()) for x in files} # length indicates imporant attributes about a file
    old_names, cleaned_names = get_old_and_cleaned(filename_lengths)
    cleaned_names = [remove_junk(el) for el in cleaned_names]

    old_new_pairs = get_pairs(old_names, cleaned_names)

    return old_new_pairs

def clean_dir(dir):
    # delete readme
    os.remove(f'{dir}/Readme.txt')
    names = make_new_names(dir)
    for old, new in names:
        os.rename(f'{dir}/{old}', f'{dir}/{new}')