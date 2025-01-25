import requests
import pandas as pd 
from db import engine
import random


def extract():
  url = "https://restcountries.com/v3.1/all?fields=name,independent,unMember,startOfWeek,currencies,idd,capital,region,subregion,languages,area,population,continents"

  respond = requests.get(url)

  if respond.status_code == 200:
    raw_data = respond.json()
  else:
     print(f"failed to fetch  the data")  
    
  return raw_data


def transform(extracted_data):
  countries = []

  for country in extracted_data:
    countries.append([
      random.randint(1000,1000000),
      country.get('name').get('common'),
      country.get('independent'),
      country.get('unMember'),
      country.get('startOfWeek'),
      country.get('name').get('official'),
      [val.get('common') for val in country.get('name', {}).get('nativeName', {}).values()],
      [country.get('currencies').keys()],
      [val.get('name') for val in country.get('currencies', {}).values()],   
      [val.get('symbol') for val in country.get('currencies', {}).values()],                                    
      country.get('capital'),  
      country.get('region'),
      country.get('subregion'),
      country.get('area'),
      country.get('population'),
      country.get('continents'),
      list[country.get('languages').values()],
       country.get('idd').get('root'),
      country.get('idd').get('suffixes')
      ])


    df = pd.DataFrame(countries)
    df.columns =['id','Country_name','Independence','United_Nation_members','startOfWeek','Official_country_name','Common_native_name',
                 'Currency_code','Currency_name','Currency_symbol','Capital','Region','Sub_region','Area',
                 'Population','Continents','Languages','idd_root','idd_suffixes']
    df['id'] = range(1,len(df) + 1)
    df['Currency_code'] = df['Currency_code'].apply(list)
    df['Languages'] = df['Languages'].apply(list)
    df['United_Nation_members'] = df['United_Nation_members'].astype(str)
    df['Independence'] = df['Independence'].astype(str)
  return df


  

def load(cleaned_data ):
   
   con_engine = engine

   cleaned_data.to_sql(
   name = "rest_countries",
   con = con_engine,
   if_exists = "replace",
   index = False,
   
    )
   return print(f'The data been successfully load into the database')
