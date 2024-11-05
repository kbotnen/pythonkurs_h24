#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import requests_cache # pip install requests-cache, url-normalize, cattrs, plattformdirs, exceptionsgroups


# In[ ]:


#replaceme
requests_cache.install_cache(cache_name='vinmonopolet_cache', backend='sqlite', expire_after=360)

#https://api.vinmonopolet.no/api-details#api=stores&operation=GET_DETAILS
headers = {
    'Ocp-Apim-Subscription-Key': 'replaceme'
}

api_url = "https://apis.vinmonopolet.no/stores/v0/details"

response = requests.get(api_url, headers=headers)

json_response = response.json()

#print(json_response)

for store in json_response:
    #print(store['storeName'])
    #print(store['status'])
    address = dict(store['address'])
    #print(address['gpsCoord'])
    if(address['city'] == "Ulsteinvik"):
        print(store['storeName'])
        print(store['status'])
        print(address['gpsCoord'])
        lat, lon = address['gpsCoord'].split(';')
        print('--------------------')


# In[ ]:




