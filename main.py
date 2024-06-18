import numpy as np
import pandas as pd

csv_path = "resorts.csv"

df = pd.read_csv(csv_path, encoding='cp1252', delimiter=',')

"""
df.head

   ID                        Resort   Latitude   Longitude  ... Child friendly Snowparks  Nightskiing Summer skiing
0   1                      Hemsedal  60.928244    8.383487  ...            Yes       Yes          Yes            No
1   2              Geilosiden Geilo  60.534526    8.206372  ...            Yes       Yes          Yes            No
2   3                          Golm  47.057810    9.828167  ...            Yes        No           No            No
3   4  Red Mountain Resort-Rossland  49.105520 -117.846280  ...            Yes       Yes          Yes            No
4   5                       Hafjell  61.230369   10.529014  ...            Yes       Yes          Yes            No

"""

# voy a extraer la columna country y contar cuantas veces aparece cada país

countries = {}

for country in df["Country"]:
    if country in countries:
        countries[country] += 1
    else:
        countries[country] = 1

print(countries)