#!/usr/bin/env python
# coding: utf-8

# # Python for ingeniøren - Introduksjon til python - Del 1
# Hva er python og hva kan det brukes til?
# 
# NITO pythonkurs november 2024, Kristian Botnen

# ## Kalkulator

# In[ ]:


# Vi har 100 pirater, og 20 store tønner. Hvor mange pirater får vi gjemt i hver tønne?
print(100 / 20)


# In[ ]:


# Vi har en myntdupliseringsmaskin som kan lage ti nye mynter pr.dag. Hvor mange mynter har vi iløpet av et år?
print(365 * 10)


# In[ ]:


# Vi har funnet 101 nye mynter, hvor mye mynt har vi nå iløpet av året?
print(365 * 10 + 101)


# Vi har mange forskjellige operatorer i python, blant annet:
# 
#     + , addisjon
#     - , subraksjon
#     * , multiplikasjon
#     / , dividering
# 
# *Når vi programmerer i Python så går ganging og deling før pluss og minus, så sant du ikke bruker parenteser for å endre rekkefølgen.*

# ## Hva er en variabel?
# En variabel i programmering beskriver en plass hvor vi kan lagre informasjon som tall, tekst, lister med mer. Vi kan også se på en variabel som en merkelapp til stedet hvor informasjonen er lagret.

# In[ ]:


# Vi kan lage en variabel på denne måten:
pirat = "Langemann"
print(pirat)


# In[ ]:


# Vi kan endre innholdet i en variabel ved å tildele en ny verdi på samme måte som vi gjorde opprinnelig:
pirat = "Kaptein Sabeltann"
print(pirat)


# In[ ]:


# Vi kan ha flere merkelapper som peker til den samme informasjonen:
kaptein = pirat
print(kaptein)


# In[ ]:


# Det kan være lurt å navngi variablene våre slik at vi skjønner hva de skal brukes til:
antall_mynter = 200
print(antall_mynter)


# In[ ]:


# Vi kan se hvilken type verdi en variabel peker til ved å bruke nøkkelordet type():
print(type(kaptein))
print(type(antall_mynter))


# ## Bruke variabler
# La oss bruke det vi har lært til nå.

# In[ ]:


antall_dager = 365
antall_produserte_mynter_dag = 10
antall_ekstra_mynter = 101

print(antall_dager * antall_produserte_mynter_dag + antall_ekstra_mynter)


# Ved å bruke variabler kan vi enkelt endre verdier et sted, og så blir de nye verdiene tilgjengelig alle steder hvor variablene er brukt. Dette vil spare oss for mye manuell inntasting, som igjen sparer oss tid OG reduserer risikoen for å taste feil.

# ## Løkker
# Maskinen er flink til å repetere ting. Vi skal her se på to forskjellige måter å repetere.

# In[ ]:


# Tilstandsløkke
i = 0
while (i < 5):
    print(i)
    i = i + 1


# In[ ]:


# Telleløkke
for i in range(0, 5):
    print(i)


# ## Inndata
# La oss se hvordan vi kan gå frem for å gi maskinen noe inndata.

# In[ ]:


inndata = ""
while (inndata != "quit"):
    inndata = input("Enter something:") # The input() function always return a string!
    print("You entered: " + inndata)
print("You told me to quit, so I did")


# ## Typecasting
# Vi ser på hvordan vi kan sjonglere mellom forskjellige typer.

# In[ ]:


string_variable_a = "1"
string_variable_b = "2"

print(string_variable_a + string_variable_b) # Vi konkatinerer to variabler av type string.


# In[ ]:


string_variable_a = "1"
string_variable_b = "2"

print(int(string_variable_a) + int(string_variable_b)) # Vi summerer to variabler av type string v.h.a typecasting.


# ## Bonus: Vi kaster terning
# Bakgrunn: Vi ønsker å kaste en terning 6 ganger. La oss se hvordan vi kan løse dette på forskjellige måter.
# 
# Vi bruker den innebygde modulen random, som tross navnet genererer pseudorandom verdier.
# 
# Vi skal også gjøre et forsøk på å bruke den offisielle dokumentasjonen: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)

# In[ ]:


import random
#random.seed(1)
print(random.randrange(1,7))
print(random.randrange(1,7))
print(random.randrange(1,7))
print(random.randrange(1,7))
print(random.randrange(1,7))
print(random.randrange(1,7))


# In[ ]:


import random

def egen_funksjon():
    print(random.randrange(1,7))
    
egen_funksjon()
egen_funksjon()
egen_funksjon()
egen_funksjon()
egen_funksjon()
egen_funksjon()


# In[ ]:


import random

def egen_funksjon(antall_kast):
    for i in range(0, antall_kast):
        print(random.randrange(1,7))
    
egen_funksjon(6)


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
