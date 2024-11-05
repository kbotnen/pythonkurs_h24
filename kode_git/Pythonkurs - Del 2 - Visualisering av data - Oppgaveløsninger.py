#!/usr/bin/env python
# coding: utf-8

# ## Oppgave
# 0: Opprett et nytt tomt kodeprosjekt / dokument.
# 
# 1: Bruk terningprogrammet fra forrige oppgave.
# 
# 2: Plott resultatene fra 1000 eller 10.000 terningkast i valgfritt plot.

# ## Løsningsforslag oppgave

# In[ ]:


import random

def kast_terning(antall_kast):
    result_array = []
    for i in range(0,antall_kast):
        result_array.append(random.randrange(1,7))
    #print("Antall prosent som er 6:", (result_array.count(6) / antall_kast) * 100)
    return result_array
        
antall_kast = 100
dataset = kast_terning(antall_kast)
#print(dataset)
print("Antall prosent som er 1:", (dataset.count(1) / antall_kast) * 100)
print("Antall kast som er 1:", (dataset.count(1)))
print("----------------------------------")
print("Antall prosent som er 2:", (dataset.count(2) / antall_kast) * 100)
print("Antall kast som er 2:", (dataset.count(2)))
print("----------------------------------")
print("Antall prosent som er 3:", (dataset.count(3) / antall_kast) * 100)
print("Antall kast som er 3:", (dataset.count(3)))
print("----------------------------------")
print("Antall prosent som er 4:", (dataset.count(4) / antall_kast) * 100)
print("Antall kast som er 4:", (dataset.count(4)))
print("----------------------------------")
print("Antall prosent som er 5:", (dataset.count(5) / antall_kast) * 100)
print("Antall kast som er 5:", (dataset.count(5)))
print("----------------------------------")
print("Antall prosent som er 6:", (dataset.count(6) / antall_kast) * 100)
print("Antall kast som er 6:", (dataset.count(6)))


# In[ ]:


print(type(dataset))


# In[ ]:


# We need to create a new label:number of occurences DataFrame.
import pandas as pd

df = pd.DataFrame({'labels': ['1', '2', '3', '4', '5', '6'],
                    'occurences': [dataset.count(1), dataset.count(2), dataset.count(3), dataset.count(4), dataset.count(5), dataset.count(6)] 
                    })

print(df)


# In[ ]:


import plotly.express as px

# https://plotly.com/python-api-reference/generated/plotly.express.pie.html
fig = px.pie(
    df,
    values='occurences', # Values from this column or array_like are used as labels for sectors.
    names='labels'        # Array-like and dict are transformed internally to a pandas DataFrame.
)
fig.show()


# In[ ]:


# https://plotly.com/python-api-reference/generated/plotly.express.bar.html
new_dataset = {1:dataset.count(1),2:dataset.count(2),3:dataset.count(3),4:dataset.count(4),5:dataset.count(5),6:dataset.count(6)}
print (new_dataset)
fig = px.bar(
    x=[1,2,3,4,5,6], # Values from this column or array_like are used to position marks along the x axis.
    y=new_dataset,   # Values from this column or array_like are used to position marks along the y axis
    labels={"x":"Result", "y":"Frequency"} # Values should correspond to the desired label to be displayed.
)
fig.show()

