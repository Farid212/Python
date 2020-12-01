import pandas as pd
import metaplotib.pyplot as plt

confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recovered = pd.read_csv('covid19_recovered.csv')

print(confirmed.head())