import pandas as pd
from pathlib import Path
import sqlite3


Path('baza_2.sqlite3').touch()

conn = sqlite3.connect('baza_2.sqlite3')
c = conn.cursor()


pkn = pd.read_csv('./data/PKN.csv', index_col=0)
kgh = pd.read_csv('./data/KGH.csv', index_col=0)
sen = pd.read_csv('./data/SEN.csv', index_col=0)

pkn = pkn['Zamkniecie']
kgh = kgh['Zamkniecie']
sen = sen['Zamkniecie']

database = pd.concat([pkn, kgh, sen], axis = 1)
database.columns = ['Cena_PKN', 'Cena_KGH', 'Cena_SEN' ] 


database.to_sql('app_2_price', conn, if_exists='append')
