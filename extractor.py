
# declaramos los archivos de donde extraeremos la información

# Archivo de actividades

path_skiing = "./actividades/skiing.json"
path_surfing = "./actividades/surfing.json"

# Archivo de atracciones

path_biodiverse = "./atracciones/biodiverse.json"
path_best_countries = "./atracciones/best-countries.json"
path_worst_countries = "./atracciones/worst-countries.json"

# Archivo de restaurantes

path_alcohol = "./restaurantes/alcohol.json"
path_best_food = "./restaurantes/best-food.json"
path_national_dishes = "./restaurantes/national-dishes.json"
path_vegetables = "./restaurantes/vegetables.json"

# Archivo de seguridad

path_car_accidents = "./seguridad/car-accidents.json"
path_crime_rate = "./seguridad/crime-rate.json"
path_drug_use = "./seguridad/drug-use.json"
path_most_dangerous = "./seguridad/most-dangerous.json"

# archivo de transporte

path_most_traffic = "./transporte/most-traffic.json"

# archivo de clima

path_global_weather = "./clima/GlobalWeatherRepository.csv"


countries = {}

# Cargamos la información de los archivos
import json

# Actividades
skiing = json.load(open(path_skiing))

for el in skiing:
    country = el["country"]
    skiing_resorts = el["SkiingCountries_SkiResorts"]

    if country not in countries:
        countries[country] = {}

    countries[country]["skiing"] = True
    countries[country]["skiing_resorts"] = skiing_resorts

surfing = json.load(open(path_surfing))
for el in surfing:
    country = el["country"]
    best_place_to_surfing = el["BestCountriesForSurfingFamousSpots"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["surfing"] = True
    countries[country]["best_place_to_surfing"] = best_place_to_surfing

# Atracciones

biodiverse = json.load(open(path_biodiverse))
for el in biodiverse:
    country = el["country"]
    biodiversity = el["BiodiversityIndex"]

    if country not in countries:
        countries[country] = {}

    countries[country]["is_biodiverse"] = True
    countries[country]["biodiversity"] = biodiversity

best_countries = json.load(open(path_best_countries))
for el in best_countries:
    country = el["country"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["is_best_country"] = True

worst_countries = json.load(open(path_worst_countries))
for el in worst_countries:
    country = el["country"]
    possible_reasons = el["PossibleThreats"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["is_worst_country"] = True
    countries[country]["possible_reasons"] = possible_reasons

# Restaurantes

alcohol = json.load(open(path_alcohol))
for el in alcohol:
    country = el["country"]
    consumption = el["AlcoholConsumptionBothSexes2019"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["alcohol"] = True
    countries[country]["alcohol_consumption"] = consumption

best_food = json.load(open(path_best_food))
for el in best_food:
    country = el["country"]
    best_food = el["WhatCountryHasBestFood2022AvgScore"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["best_food"] = True
    countries[country]["best_food_index"] = best_food

national_dishes = json.load(open(path_national_dishes, encoding="utf-8"))
for el in national_dishes:
    country = el["country"]
    dish = el["CountriesNationalDishes"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["traditional_dish"] = dish

vegetables = json.load(open(path_vegetables))
for el in vegetables:
    country = el["country"]
    consumption = el["VegetableConsumption2020"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["vegetables"] = True
    countries[country]["vegetable_consumption"] = consumption

# Seguridad

car_accidents = json.load(open(path_car_accidents))
for el in car_accidents:
    country = el["country"]

    # accidente por millon de personas
    accidents = el["CountriesWithMostCarAccidentsAccidentsPerMillionPeople2019"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["most_car_accidents"] = True
    countries[country]["car_accidents"] = accidents


crime_rate = json.load(open(path_crime_rate))
for el in crime_rate:
    country = el["country"]
    rate = el["crimeRateByCountry_crimeIndex"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["crime_rate"] = rate
    
drug_use = json.load(open(path_drug_use))
for el in drug_use:
    country = el["country"]
    rate = el["DrugUseDisorder2019"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["drug_use"] = rate

most_dangerous = json.load(open(path_most_dangerous))
for el in most_dangerous:
    country = el["country"]
    rate = el["MostPeaceful2023GPI"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["rate_dangerous"] = rate

# Transporte

most_traffic = json.load(open(path_most_traffic))
for el in most_traffic:
    country = el["country"]
    rank = el["rank"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["most_traffic"] = True
    countries[country]["traffic_rank"] = rank

# Clima

import pandas as pd

global_weather = pd.read_csv(path_global_weather)

for i, row in global_weather.iterrows():
    country = row["country"]
    temperature = row["temperature_celsius"]

    if country not in countries:
        countries[country] = {}
    
    countries[country]["temperature"] = temperature





# ahora en caso algun paisos no tenga todas las propiedades
# antes descritas las completamos con null 

for country in countries:

    if "skiing" not in countries[country]:
        countries[country]["skiing"] = False
        countries[country]["skiing_resorts"] = None
    
    if "surfing" not in countries[country]:
        countries[country]["surfing"] = False
        countries[country]["best_place_to_surfing"] = None
    
    if "is_biodiverse" not in countries[country]:
        countries[country]["is_biodiverse"] = False
        countries[country]["biodiversity"] = None
    
    if "is_best_country" not in countries[country]:
        countries[country]["is_best_country"] = False
    
    if "is_worst_country" not in countries[country]:
        countries[country]["is_worst_country"] = False
        countries[country]["possible_reasons"] = None
    
    if "alcohol" not in countries[country]:
        countries[country]["alcohol"] = False
        countries[country]["alcohol_consumption"] = None
    
    if "best_food" not in countries[country]:
        countries[country]["best_food"] = False
        countries[country]["best_food_index"] = None
    
    if "traditional_dish" not in countries[country]:
        countries[country]["traditional_dish"] = None
    
    if "vegetables" not in countries[country]:
        countries[country]["vegetables"] = False
        countries[country]["vegetable_consumption"] = None
    
    if "most_car_accidents" not in countries[country]:
        countries[country]["most_car_accidents"] = False
        countries[country]["car_accidents"] = None
    
    if "crime_rate" not in countries[country]:
        countries[country]["crime_rate"] = None
    
    if "drug_use" not in countries[country]:
        countries[country]["drug_use"] = None
    
    if "rate_dangerous" not in countries[country]:
        countries[country]["rate_dangerous"] = None
    
    if "most_traffic" not in countries[country]:
        countries[country]["most_traffic"] = False
        countries[country]["traffic_rank"] = None
    
    if "temperature" not in countries[country]:
        countries[country]["temperature"] = None
    

# guardamos como un csv
import csv

with open("countries.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["country", "skiing", "skiing_resorts", "surfing", "best_place_to_surfing", "is_biodiverse", "biodiversity", "is_best_country", "is_worst_country", "possible_reasons", "alcohol", "alcohol_consumption", "best_food", "best_food_index", "traditional_dish", "vegetables", "vegetable_consumption", "most_car_accidents", "car_accidents", "crime_rate", "drug_use", "rate_dangerous", "most_traffic", "traffic_rank", "temperature"])

    for country in countries:
        writer.writerow([
            country,
            countries[country]["skiing"],
            countries[country]["skiing_resorts"],
            countries[country]["surfing"],
            countries[country]["best_place_to_surfing"],
            countries[country]["is_biodiverse"],
            countries[country]["biodiversity"],
            countries[country]["is_best_country"],
            countries[country]["is_worst_country"],
            countries[country]["possible_reasons"],
            countries[country]["alcohol"],
            countries[country]["alcohol_consumption"],
            countries[country]["best_food"],
            countries[country]["best_food_index"],
            countries[country]["traditional_dish"],
            countries[country]["vegetables"],
            countries[country]["vegetable_consumption"],
            countries[country]["most_car_accidents"],
            countries[country]["car_accidents"],
            countries[country]["crime_rate"],
            countries[country]["drug_use"],
            countries[country]["rate_dangerous"],
            countries[country]["most_traffic"],
            countries[country]["traffic_rank"],
            countries[country]["temperature"]
        ])
