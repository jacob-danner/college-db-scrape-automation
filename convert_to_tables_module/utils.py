# utils
from collections import namedtuple

def get_date(folder):
    year = folder[-4:]

    month = int( folder[:2] )
    quarter = int( 12 / month ) # 6 -> 2

    Date = namedtuple('Date', ['year', 'quarter'])
    date = Date(year, quarter)
    return date

def clean_column_name(column):
    if '/' in column:
        column = column.replace('/', '-')

    return column