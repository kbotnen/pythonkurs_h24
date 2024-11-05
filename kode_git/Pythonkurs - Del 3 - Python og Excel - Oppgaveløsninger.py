#!/usr/bin/env python
# coding: utf-8

# ## Oppgave
# 
# Fortsett med programmet fra tidligere. Vi skal nå opprette to nye faner i et Excel ark.
# - Den ene fanen inneholder selve datasettet vårt. Kastnummer og resultat.
# - Den andre fanen inneholder deskriptiv statistikk om datasettet vårt.
# 
# NB! Det vil være enklest om du oppretter en Pandas DataFrame basert på datasettet vårt først.

# ## Løsningsforslag oppgave

# In[ ]:


import random

import pandas as pd

def kast_terning(antall_kast):
    result_array = []
    for i in range(0, antall_kast):
        result_array.append(random.randrange(1,7))
    return result_array
        
antall_kast = 10

terning_dataframe = pd.DataFrame()
# For more interesting data, we can repeat our experiment to generate more data
antall_forsok = 5
for i in range(0, antall_forsok):
   dataset = kast_terning(antall_kast)
   terning_dataframe["Set %s" % i] = dataset

#terning_dataframe = pd.DataFrame(kast_terning(antall_kast)) # Single run only
print(type(terning_dataframe))
terning_dataframe


# In[ ]:


terning_descriptive = terning_dataframe.describe()
terning_descriptive


# In[ ]:


with pd.ExcelWriter("Pythonkurs - Del 3 - Python og excel terningkast.xlsx") as writer:
    terning_dataframe.to_excel(writer, sheet_name='Original data', index=False)
    terning_descriptive.to_excel(writer, sheet_name='Descriptive statistics')


# In[ ]:




