import pandas as pd
from .utils import clean_column_name

def make_table(df, column):
    cols = ['year', 'quarter', column]
    table = (
        df
        [cols]
        .dropna()
    )
    return table

def make_tables(path_to_file, path_to_output, date):
    data = pd.read_csv(path_to_file, index_col=0)
    columns = data.columns
    data['year'] = date.year
    data['quarter'] = date.quarter
    data.index.rename('bank_id', inplace=True)
    for column in columns:
        clean_column = clean_column_name(column)
        data.rename(columns={column: clean_column})
        table = make_table(data, column)
        table_name = f'{clean_column}.csv'
        table.to_csv(f'{path_to_output}/{table_name}')