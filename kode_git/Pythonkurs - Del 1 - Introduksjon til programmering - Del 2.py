#!/usr/bin/env python
# coding: utf-8

# # Python for ingeniøren - Introduksjon til python - Del 2
# Hva er python og hva kan det brukes til?
# 
# NITO pythonkurs november 2024, Kristian Botnen

# ## Litt kode for å vise funksjoner på string og list

# In[ ]:


# Remember that we can check the type of a variable.
string_var = "Hello World"
print(type(string_var))


# In[ ]:


# We can uppercase / lowercase a string.
string_var = "Hello World"
print(string_var.lower())
print(string_var.upper())
print(string_var)


# In[ ]:


# String is actually a list of characters.
string_var = "Hello World"
print(string_var[0])


# In[ ]:


# We can loop over a string (which is a type of list) by using the index.
string_var = "Hello World"
for bokstav in string_var:
    print(bokstav)


# In[ ]:


# We can define a list like this.
fruit_list = ["apple", "banana", "cherry"]

# And then we can loop over the list.
for fruit in fruit_list:
    print(fruit)


# In[ ]:


# We can sort a list in reverse.
fruit_list = ["apple", "banana", "cherry"]
print(fruit_list)
fruit_list.sort(reverse=True)
print(fruit_list)


# In[ ]:


# We can define a dictionary like this.
personal_info = {"firstName": "Kristian",
          "lastName": "Botnen",
          "age": 42,
          "hairColour": "brown",
          "height": 176}

# And then print information from the dict.
print("My hairColour is ", personal_info['hairColour'])
# And change information in the dict.
personal_info['hairColour'] = "green"
# Check that our change is... changed?
print("My hairColour is ", personal_info['hairColour'])
# We can add a new key:value pair in our dictionary.
personal_info['language'] = "python"
# And print the new key:value pair.
print("My language is ", personal_info['language'])


# In[ ]:


# We can define multiple lists.
trondheimWeatherStation = { "stationName": "Trondheim",
                        "windSpeed": 10,
                        "windDirection": 189,
                        "temperature": 4.3}

osloWeatherStation = { "stationName": "Oslo",
                        "windSpeed": 4,
                        "windDirection": 76,
                        "temperature": 9.8}

# And create a list that contain our dictionaries.
weatherstations = [trondheimWeatherStation, osloWeatherStation]

# And inspect the list of dictionaries using a for loop.
for station in weatherstations:
    for key in station.keys():
        print(key, ":", station[key])
              


# # Oppsummering og oppgaver

# ## Oppgaver - Del 1
# 
# 0. Opprett et nytt tomt kodeprosjekt / dokument.
# 1. Lag en variabel som inneholder en valgfri tekst (string).
# 2. Lag en funksjon som tar inn variabelen og reverserer stringen.

# ## Oppgaver - Del 2
# 
# 0. Opprett et nytt tomt kodeprosjekt / dokument.
# 1. Lag et program som simulerer en terning. Du kan kanskje gjenbruke deler av koden fra tidligere oppgave?
# 2. Bruk programmet til å utføre 10, 100 eller 1000 kast.
# 3. Vi vet hva sansynligheten for å få en sekser er 1/6, men hvordan stemmer dette overens med resultatene fra pkt2?.
