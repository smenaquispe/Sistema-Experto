# abrimos el csv countries.csv

import pandas as pd

df = pd.read_csv('countries.csv')

countries = {}

def obtener_tipo_clima(temperatura):
    if temperatura < 0:
        return "muy frío"
    elif 0 <= temperatura < 10:
        return "frío"
    elif 10 <= temperatura < 20:
        return "templado"
    elif 20 <= temperatura < 30:
        return "cálido"
    elif temperatura >= 30:
        return "muy cálido"
    else:
        return "desconocido"
    
# Función para determinar la calidad de la comida basado en el índice de mejor comida
def obtener_tipo_comida(indice_comida):
    if 0 <= indice_comida < 1:
        return "muy mala"
    elif 1 <= indice_comida < 2:
        return "mala"
    elif 2 <= indice_comida < 3:
        return "regular"
    elif 3 <= indice_comida < 4:
        return "buena"
    elif 4 <= indice_comida <= 5:
        return "excelente"
    else:
        return "desconocida"

# Función para determinar la tasa de crimen
def obtener_nivel_seguridad(crime_rate):
    if 0 <= crime_rate < 20:
        return "muy seguro"
    elif 20 <= crime_rate < 40:
        return "seguro"
    elif 40 <= crime_rate < 60:
        return "regular"
    elif 60 <= crime_rate < 80:
        return "inseguro"
    elif 80 <= crime_rate <= 100:
        return "muy inseguro"
    else:
        return "desconocido"
    
def obtener_nivel_biodiversidad(biodiversity_level):
    if 0 <= biodiversity_level < 200:
        return "baja"
    elif 200 <= biodiversity_level < 400:
        return "moderada"
    elif 400 <= biodiversity_level < 600:
        return "alta"
    elif 600 <= biodiversity_level < 1000:
        return "muy alta"
    else:
        return "desconocida"
    

for i, row in df.iterrows():

    country_name = row['country']

    countries[country_name] = {
        "actividades": [],
        "atracciones": [],
        "clima": [],
        "restaurantes": [],
        "seguridad": [],
        "transporte": [],
        "alcohol": [],
        "biodiversidad": [],
        "vegetales": [],
        
    }

    # vamos a repasar cada columna
    # primero skiing y skiing resorts


    # ACTIVIDADES
    if row['skiing'] == True:
        countries[country_name]["actividades"].append("que tenga resorts donde se puede realizar ski o snowboarding")
    
    if row["surfing"] == True:
        countries[country_name]["actividades"].append("que tenga playas donde se puede surfear")
    
    # ATRACCIONES
    if row['is_biodiverse'] == True:
        countries[country_name]["atracciones"].append("que tenga una gran biodiversidad")
    
    if row["is_best_country"] == True:
        countries[country_name]["atracciones"].append("le importa que según encuestas sea un país bueno para visitar")

    # CLIMA
    if row['temperature'] != True:
        tipo_clima = obtener_tipo_clima(row['temperature'])
        countries[country_name]["clima"].append(f"que tenga un clima {tipo_clima}")

    #RESTAURANTE
    if row['best_food'] != True:
        tipo_comida = obtener_tipo_comida(row['best_food_index'])
        countries[country_name]["restaurantes"].append(f"que tenga una calidad de comida {tipo_comida}")

    #SEGURIDAD (CRIME RATE)
    if row['crime_rate'] == True:
        nivel_seguridad = obtener_nivel_seguridad(row['crime_rate'])
        countries[country_name]["seguridad"].append(f"que sea un lugar {nivel_seguridad}")

    
    # TRANSPORTE
    if row['most_traffic'] == True:
        countries[country_name]["transporte"].append("Tiene indices de trafico")

    # ALCOHOL
    if row['alcohol'] == True:
         countries[country_name]["alcohol"].append("que se pueda consumir alcohol")
    
    #Biodiversidad
    if row['is_biodiverse'] != True:
        nivel_biodiversidad = obtener_nivel_biodiversidad(row['biodiversity'])
        countries[country_name]["biodiversidad"].append("Su nivel de Biodiversidad es {nivel_biodiversidad}")

    #VEGETALES
    if row['vegetables'] == True:
         countries[country_name]["vegetales"].append("Tiene una dieta basada en vegetales")


import json
with open("countries.json", "w") as f:
    json.dump(countries, f, indent=4)