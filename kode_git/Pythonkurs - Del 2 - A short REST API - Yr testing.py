#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json


# In[ ]:


# https://developer.yr.no/doc/locationforecast/HowTO/
headers = {
    'User-agent': 'replaceme',
    'From': 'replaceme'
}

api_url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
latitude = "60.392" # http://www.geonames.org/
longitude = "5.324" # http://www.geonames.org/

response = requests.get(api_url, headers=headers, params={"lat":latitude, "lon":longitude})

# https://developer.yr.no/doc/ForecastJSON/
json_response = response.json()

#print(json_response)


data = json_response['properties']['timeseries']

new_dict = dict(dict(data[0])['data'])
print(new_dict['instant']['details']['air_temperature'])


# In[ ]:




