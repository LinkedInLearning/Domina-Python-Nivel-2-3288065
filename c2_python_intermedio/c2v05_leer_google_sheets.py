import gspread
import pandas as pd


def leer_sheet_publica(sheet_id, sheet_name):
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    df = pd.read_csv(url)
    print(df.head())


def leer_sheet_privada(sheet_id, sheet_name):
    pass


sheet_id = '1qa4692UUhrM5xNyEVycAm8uC8j549NpsxUjWyimBNf4'
sheet_name = 'personas'
leer_sheet_publica(sheet_id, sheet_name)
