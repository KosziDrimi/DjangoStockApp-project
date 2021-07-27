import pandas as pd
from pathlib import Path
import sqlite3


Path('baza_2.sqlite3').touch()

conn = sqlite3.connect('baza_2.sqlite3')
c = conn.cursor()


pkn = pd.read_csv('./data/PKN.csv', index_col=0)
kgh = pd.read_csv('./data/KGH.csv', index_col=0)
sen = pd.read_csv('./data/SEN.csv', index_col=0)

pkn.insert(0, 'Nazwa_spółki', 'PKN')
kgh.insert(0, 'Nazwa_spółki', 'KGH')
sen.insert(0, 'Nazwa_spółki', 'SEN')

pkn = pkn[['Nazwa_spółki', 'Zamkniecie']]
kgh = kgh[['Nazwa_spółki', 'Zamkniecie']]
sen = sen[['Nazwa_spółki', 'Zamkniecie']]


database = pd.concat([pkn, kgh, sen])
database.columns = ['Nazwa_spółki', 'Cena'] 

database.to_sql('app_2_price', conn, if_exists='append')
