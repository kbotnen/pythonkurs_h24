#!/usr/bin/env python
# coding: utf-8

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

# ## Løsningsforslag oppgaver - Del 1

# In[ ]:


original_string = "Hello world"

def reverse_string(text):
    reversed_string = ""
    for letter in text:
        reversed_string = letter + reversed_string
    return reversed_string
        
print(reverse_string(original_string))


# ## Løsningsforslag oppgaver - Del 2

# In[ ]:


import random

def kast_terning(antall_kast):
    # Listevariabel som holder resultatene av kastene underveis
    result_array = []
    
    # Bruk for-løkke for å gjøre antall_kast
    for i in range(0,antall_kast):
        terningkastet = random.randrange(1,7)
        result_array.append(terningkastet)
    
    prosentandelen = (result_array.count(6) / antall_kast) * 100
    print("Antall prosent som er 6:", prosentandelen)
    return result_array
        
ti_kast = kast_terning(10)
hundre_kast = kast_terning(100)
tusen_kast = kast_terning(1000)

print(ti_kast)
print(hundre_kast)
print(tusen_kast)


# In[ ]:




