#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %pip install requests_cache


# In[ ]:


import requests
import requests_cache
import json
import folium


# In[ ]:


requests_cache.install_cache(cache_name='apitest_cache', backend='sqlite', expire_after=720)


# In[ ]:


# https://developer.yr.no/doc/locationforecast/HowTO/
# https://api.vinmonopolet.no/api-details#api=stores&operation=GET_DETAILS

yr_headers = {
    'User-agent': 'replaceme',
    'From': 'replaceme'
}
yr_api_url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

vin_headers = {
    'Ocp-Apim-Subscription-Key': 'replaceme'
}

vin_api_url = "https://apis.vinmonopolet.no/stores/v0/details"

def vin_get_stores(vin_city):
    result_array = []
    response = requests.get(vin_api_url, headers=vin_headers)
    json_response = response.json()

    for store in json_response:
        address = dict(store['address'])
        #print(address['gpsCoord'])
        if(address['city'] == vin_city):
            result_array.append(address['gpsCoord'])
    return result_array

def yr_get_temperature(yr_lat, yr_lon):
    response = requests.get(yr_api_url, headers=yr_headers, params={"lat":yr_lat, "lon":yr_lon})

    # https://developer.yr.no/doc/ForecastJSON/
    json_response = response.json()
    data = json_response['properties']['timeseries']

    new_dict = dict(dict(data[0])['data'])
    return (new_dict['instant']['details']['air_temperature'])

def plot_folium(markers_list, desc_list):
    map = folium.Map(location=[60.39, 5.32], zoom_start=4, control_scale=True)

    i = 0
    for marker in markers_list:
        icon_lat, icon_lon = marker.split(';')
        if desc_list[i] > 8:
            folium.Marker(
                location=[icon_lat, icon_lon],
                popup=f"{desc_list[i]} \N{DEGREE CELSIUS}",
                icon=folium.Icon(color="red", icon="ok-sign"),
            ).add_to(map)
        elif desc_list[i] > 7:
            folium.Marker(
                location=[icon_lat, icon_lon],
                popup=f"{desc_list[i]} \N{DEGREE CELSIUS}",
                icon=folium.Icon(color="green", icon="ok-sign"),
            ).add_to(map)
        elif desc_list[i] > 6.5:
            folium.Marker(
                location=[icon_lat, icon_lon],
                popup=f"{desc_list[i]} \N{DEGREE CELSIUS}",
                icon=folium.Icon(color="blue", icon="ok-sign"),
            ).add_to(map)
        else:
            folium.Marker(
                location=[icon_lat, icon_lon],
                popup=f"{desc_list[i]} \N{DEGREE CELSIUS}",
                icon=folium.Icon(color="black", icon="ok-sign"),
            ).add_to(map)
        i += 1
    return map

stores_list = vin_get_stores("Oslo")
temperature_list = []

if len(stores_list) > 0:
    for store in stores_list:
        lat, lon = store.split(';')
        temperature = yr_get_temperature(lat, lon)
        temperature_list.append(temperature)

    map = plot_folium(stores_list, temperature_list)


# In[ ]:


map


# In[ ]:




