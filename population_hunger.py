import csv
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, kendalltau

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x * 1e-6)

formatter = FuncFormatter(millions)

f, ax = plt.subplots(figsize=(8, 6))

ax.yaxis.set_major_formatter(formatter)

url_ipi_hunger = 'https://drive.google.com/file/d/1W_NW8Gk4m9TcH4R4THdeW7fTTz4Rfdyw/view?usp=sharing'
url_ipi_hunger = 'https://drive.google.com/uc?id=' + url_ipi_hunger.split('/')[-2]
ipi_hunger = pd.read_csv(url_ipi_hunger,sep=',') # type: ignore

#print(ipi_hunger["Population"].describe().apply(lambda x: format(x, 'f')))

years = ipi_hunger['Year']

hungry_people = ipi_hunger['# of Hungry People']
population = ipi_hunger['Population']

'''
g = sns.barplot(data=ipi_hunger, x='Year', y="Population", ax=ax)
g = sns.barplot(data=ipi_hunger, x='Year', y="# of Hungry People", ax=ax)
ax.tick_params(axis='x', rotation=45)
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())

print(ipi_hunger)
'''

#Hypothesis testing:

print(pearsonr(hungry_people, population))


plt.bar(years, population, label = "Population", color='#29AF67')
plt.bar(years, hungry_people, label = "Hungry People", color = '#A03232')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.yticks(np.arange(1000000, 115000000, 5000000))
plt.xlabel("Year", fontsize=14)
plt.xticks(rotation=45)
plt.ylabel("Population Count", fontsize=14)
plt.legend()
plt.title("People Experiencing Hunger in Overall Population", fontsize=16, pad=20)


plt.show()
