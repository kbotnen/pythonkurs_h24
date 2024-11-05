#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)

an_array = response.json()

for an_item in an_array:
    print(type(an_item))
    print(an_item["id"])


# In[ ]:


import requests
api_url = "https://jsonplaceholder.typicode.com/todos/2"
response = requests.get(api_url)
response.json()


# In[ ]:


import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()

response.status_code


# In[ ]:


import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()

response.status_code


# In[ ]:


import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
response.json()

response.status_code


# In[ ]:


import requests
response = requests.get("https://visualisere.no")

print(f"The URL you requested is {response.url}")
print(f"The response status is {response.status_code}")
print(f"This requests took {response.elapsed.microseconds} microseconds.")
if response.is_redirect:
    print("Redirect") 
else:
    print("Not redirect")


# In[ ]:


import requests
# We can add parameters to the URL. Useful when searching on webpage to name one example.
api_url = "https://api.github.com/search/repositories"
params = {"q": "python+pandas"}
response = requests.get(api_url, params=params)

print(f"The response status is {response.status_code}")


# In[ ]:


import requests
# Basic authentication When we need to access exclusive content. Allow.
api_url = "https://postman-echo.com/basic-auth"
# Authentication credentials:
username = "postman"
password = "password"
# The GET request:
response = requests.get(url=api_url, auth=(username, password))
print(f"The response status is {response.status_code}")


# In[ ]:


import requests
# Authorization Header: When we dont have username+password, and want to use an access token instead.
api_url = "https://postman-echo.com/basic-auth"
headers = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
response = requests.get(url=api_url, headers=headers)

print(f"The response status is {response.status_code}\n")
try:
    print(f'Response JSON:\n{response.json()}')
except:
    print('Response is not JSON')


# ## Del 1 - API Kall
# I denne notebooken skal vi se på hvordan vi kan kalle et API og gjøre noe fornuftig med de dataene vi får tilbake. Når vi skal bruke et API kan vi kalle det på flere forskjellige måter:
# 
#     - GET: Gir oss mulighet til å hente data. Svaret kommer ofte i form av en JSON datastruktur.
#     - POST: Gir oss mulighet til å sende inn data.
#     - DELETE: Gir oss mulighet til å slette data.
#     - PUT: Gir oss mulighet til å oppdatere data.
#     
# Et API kan støtte en eller flere av disse forskjellige metodene. Det er også ganske vanlig at et API krever en form for autentisering, og at hvilken metoder som er tilgjengelig varierer ut fra hvilken tilganger du har fått tildelt.
# 
# Her er et eksempel på hvordan vi kan kalle et API:
# 
#     (base) adrock2nd@pandacourse % curl 'https://data.brreg.no/enhetsregisteret/api/enheter/991323201' -i -X GET
#     HTTP/1.1 200
#     vary: Origin
#     vary: Access-Control-Request-Method
#     vary: Access-Control-Request-Headers
#     content-type: application/json
#     transfer-encoding: chunked
#     date: Tue, 20 Sep 2022 08:34:49 GMT
#     set-cookie: 0a6517082ccf6d7c45f7bf355f56b22c=a3a914b3d45db36b495bf6a27f0d84ad; path=/; HttpOnly; Secure; SameSite=None
#     cache-control: private
#     Set-Cookie: BRjEE1=!50oxZvwQswduWrZLGXDs3x8fCpKDZd0WtzE8qoS7iqVtHEZ7kMCABnx0MpBNIIpLD6VkKlyE3DOkmg==; path=/; Httponly; Secure
#     Strict-Transport-Security: max-age=31536000; includeSubDomains
# 
#     {"organisasjonsnummer":"991323201","navn":"BOTNEN 3D","organisasjonsform":{"kode":"ENK","beskrivelse":"Enkeltpersonforetak","_links":{"self":{"href":"https://data.brreg.no/enhetsregisteret/api/organisasjonsformer/ENK"}}},"hjemmeside":"www.botnen.org","registreringsdatoEnhetsregisteret":"2007-06-04","registrertIMvaregisteret":false,"naeringskode1":{"beskrivelse":"Programmeringstjenester","kode":"62.010"},"antallAnsatte":0,"forretningsadresse":{"land":"Norge","landkode":"NO","postnummer":"5160","poststed":"LAKSEVÅG","adresse":["Damsgårdsveien 162"],"kommune":"BERGEN","kommunenummer":"4601"},"institusjonellSektorkode":{"kode":"8200","beskrivelse":"Personlig næringsdrivende"},"registrertIForetaksregisteret":false,"registrertIStiftelsesregisteret":false,"registrertIFrivillighetsregisteret":false,"konkurs":false,"underAvvikling":false,"underTvangsavviklingEllerTvangsopplosning":false,"maalform":"Nynorsk","_links":{"self":{"href":"https://data.brreg.no/enhetsregisteret/api/enheter/991323201"}}}
# 
# Et velfungerende API vil gi deg en HTTP-statuskode sammen med eventuelt data. Her er noen vanlige statuskoder:
# 
#     200 : OK.
#     401 : Authentication failed!
#     403 : Access is forbidden by the API service.
#     404 : The requested API service is not found on the server/web.
#     500 : Internal Server Error has occurred.
#     
# Du kan se flere statuskoder her: [https://en.wikipedia.org/wiki/List_of_HTTP_status_codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
# 
# Som vi kan se i eksempelet over så fikk vi en 200: OK, sammen med data i JSON format.

# In[ ]:


import requests

import json
import pprint

url = 'https://data.brreg.no/enhetsregisteret/api/enheter/931882724'

response = requests.get(url)
json_data = response.json()


# In[ ]:


print("Type:", type(json_data)) # Let see what we received from the API-call.


# In[ ]:


print (json_data) # Examine current state.


# In[ ]:


pprint.pprint(json_data) # Let us use the pprint built-in library for show.


# In[ ]:


print(json_data['forretningsadresse']['postnummer'])


# ## Del 2

# In[ ]:


import pandas as pd
df = pd.read_excel("Pythonkurs - Del 2 - A short REST API - Introduction - Source.xlsx")
df.info() # Get information about the dataframe.
df # List out the dataframe.


# In[ ]:


# Create a function that read a selected organization from the API
def read_from_api(orgnumber):
    url = 'https://data.brreg.no/enhetsregisteret/api/enheter/%s' %orgnumber
    response = requests.get(url)
    json_data = response.json()
    return json_data


# In[ ]:


read_from_api(931882724) # Test the function read_from_api


# In[ ]:


# Create a function that extract postalcode from API response
def extract_postalcode(json_data):
    postaladdress = json_data['forretningsadresse']['postnummer']
    return postaladdress


# In[ ]:


print(extract_postalcode(read_from_api(931882724))) # Test the function extract_postalcode


# In[ ]:


# Lookup all the postalcodes for our orgnumbers.
resultdict = {}
for orgnumber in df['Orgnummer']:
    resultdict[orgnumber] = extract_postalcode(read_from_api(orgnumber))
    


# In[ ]:


print(resultdict)

df['Postnummer'] = df['Orgnummer'].map(resultdict) # Create a new column in our DataFrame containing our postalcodes.


# In[ ]:


df.to_excel("Pythonkurs - Del 2 - A short REST API - Introduction - Postnummer_resultater.xlsx", header=True) # Write our result to a new excelfile.


# In[ ]:




