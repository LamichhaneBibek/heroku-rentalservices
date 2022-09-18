from urllib import response
import pandas as pd
import requests
import json

df = pd.read_csv("/home/ubu/Desktop/House_Dataset.csv")


# for i, row in df.iterrows():
    # apiAddress = str(df.at[i,'Area Locality']) + ',' + str(df.at[i,'City'])

parameters = {
    'key' : 'OQ5LG1er5VP4TnW3s9MK8pn3xxrAUI3D',
    'location' : 'Thasikhel, Lalitpur'
            }

response = requests.get('http://www.mapquestapi.com/geocoding/v1/address', params= parameters)
data = json.loads(response.text)['results']
lat = data[0]['locations'][0]['latLang']['lat']
lng = data[0]['locations'][0]['latLang']['lng']

print(lat, lng)
#     df.at[i,'lat'] = lat
#     df.at[i,'lng'] = lng

# df.to.csv('/home/ubu/Desktop/House_Dataset.csv')