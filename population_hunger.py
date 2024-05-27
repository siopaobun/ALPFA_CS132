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

fig, ax = plt.subplots()

ax.yaxis.set_major_formatter(formatter)

url_ipi_hunger = 'https://drive.google.com/file/d/1W_NW8Gk4m9TcH4R4THdeW7fTTz4Rfdyw/view?usp=sharing'
url_ipi_hunger = 'https://drive.google.com/uc?id=' + url_ipi_hunger.split('/')[-2]
ipi_hunger = pd.read_csv(url_ipi_hunger,sep=',') # type: ignore

#print(ipi_hunger["Population"].describe().apply(lambda x: format(x, 'f')))

years = ipi_hunger['Year']

hungry_people = ipi_hunger['# of Hungry People']
population = ipi_hunger['Population']

'''
cumulative = sns.lineplot(data=ipi_hunger, x="Year", y="Cumulative IPI Growth (%)")
cumulative.xaxis.set_major_locator(ticker.MultipleLocator(2))
cumulative.xaxis.set_major_formatter(ticker.ScalarFormatter())
'''

#Hypothesis testing:

print(pearsonr(hungry_people, population))


# plt.bar(years, population, label = "Population")
# plt.bar(years, hungry_people, label = "Hungry People", color = 'r')
# plt.xticks(np.arange(min(years), max(years)+1, 2.0))
# plt.yticks(np.arange(1000000, 115000000, 5000000))
# plt.xlabel("Year")
# plt.ylabel("# of People ")
# plt.legend()
# plt.grid()
# plt.title("Hungry People vs Population")
# plt.show()
