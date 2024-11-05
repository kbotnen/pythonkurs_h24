#!/usr/bin/env python
# coding: utf-8

# # Oppsummering og oppgaver

# ## Oppsummering 1
# Vi har lært litt om hva python er og hvordan vi kan bruke det til å gjøre enkle kalkuleringsoppgaver. Vi har også sett litt på python sin syntaks, lært hva variabler er og hvordan de kan brukes.
# 
# 
# ## Oppgave 1
# 0. Opprett et nytt tomt kodeprosjekt / dokument.
# 1. Lag et program som regner ut **summen** av følgende tall: 27, 15, 6, 21, 52.
# 2. Lag et program som regner ut **differansen** mellom følgende tall: 27, 15, 6, 21, 52.
# 3. Lag et program som regner ut **produktet** av følgende tall: 27, 15, 6, 21, 52.

# ## Oppsummering 2
# Vi har sett på hvordan vi kan hente inn data v.h.a en tilstandsløkke, samt hvordan vi kan bruke variabler for å lagre verdier som vi summerer.
# 
# 
# ## Oppgave 2
# 
# 0. Opprett et nytt tomt kodeprosjekt / dokument.
# 1. Lag et program som regner ut **summen** av to tall som du skriver inn.

# ## Oppsummering 3
# Vi har sett flere eksempler på hvordan vi kan rulle en terning ved hjelp av den innebygde random() funksjonen. Vi valgte å rulle en terning 6 ganger.
# 
# 
# ## Oppgave 3
# 0. Opprett et nytt tomt kodeprosjekt / dokument.
# 1. Lag et program som ruller en terning 12 ganger.
# 2. Lag et program som ruller en 12-sidet terning 6 ganger.
# 2. Lag et program som ruller to terninger 6 ganger.

# ## Løsningsforslag oppgaver - Del 1

# In[ ]:


number_a = 27
number_b = 15
number_c = 6
number_d = 21
number_e = 52

print(number_a + number_b + number_c + number_d + number_e)
print(number_a - number_b - number_c - number_d - number_e)
print(number_a * number_b * number_c * number_d * number_e)


# ## Løsningsforslag oppgaver - Del 2

# In[ ]:


tall_a = 0
tall_b = 0
while (True):
    tall_a = input("Enter first number:")
    tall_b = input("Enter second number:")
    print(int(tall_a) + int(tall_b))


# ## Løsningsforslag oppgaver - Del 3

# In[ ]:


# Lag et program som ruller en terning 12 ganger.
import random

def egen_funksjon(antall_kast):
    for i in range(0, antall_kast):
        print(random.randrange(1,7))
    
egen_funksjon(12)


# In[ ]:


# Lag et program som ruller en 12-sidet terning 6 ganger.
import random

def egen_funksjon(antall_kast):
    for i in range(0, antall_kast):
        print(random.randrange(1,13))
    
egen_funksjon(6)


# In[ ]:


# Lag et program som ruller to terninger 6 ganger.
import random

terning_a = 0
terning_b = 0

def egen_funksjon(antall_kast):
    for i in range(0, antall_kast):
        terning_a = random.randrange(1,7)
        terning_b = random.randrange(1,7)
        print("Kast #" + str(i) + ": Terning A - " + str(terning_a))
        print("Kast #" + str(i) + ": Terning B - " + str(terning_b))
        print("Sum: " + str(terning_a + terning_b))
    
egen_funksjon(6)


# In[ ]:




