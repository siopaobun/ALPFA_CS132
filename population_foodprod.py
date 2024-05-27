import pandas as pd
import csv
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from scipy.stats import pearsonr

population_data_url = 'https://drive.google.com/file/d/1akYu6fo1ymK-Rp3CRRzFsaOR-LF_kaLQ/view?usp=share_link'
population_data_url = 'https://drive.google.com/uc?id=' + population_data_url.split('/')[-2]
population_data = pd.read_csv(population_data_url,sep=",",usecols=['Year','Cumulative Growth'])

food_data_url = 'https://drive.google.com/file/d/1tYA63x-5SLxvTh2BT7OIe8YYBYxEdKAY/view?usp=share_link'
food_data_url = 'https://drive.google.com/uc?id=' + food_data_url.split('/')[-2]
Food_data = pd.read_csv(food_data_url,sep=",",usecols=['Date','Cumulative Growth'])



population_data['Cumulative Growth'] = pd.to_numeric(population_data['Cumulative Growth'].str.replace('%', ''))
population_data.set_index('Year', inplace=True)

Food_data['Cumulative Growth'] = pd.to_numeric(Food_data['Cumulative Growth'].str.replace('%', ''))
Food_data['Date'] = pd.to_datetime(Food_data['Date'])
Food_data.set_index('Date', inplace=True)
Food_data.index = pd.to_datetime(Food_data.index)
Food_yearly = Food_data.resample('YE').mean()
Food_yearly.index = Food_yearly.index.year

print("Population Data")
print(population_data.head(-10))
print("Food Data")
print(Food_yearly.head(-10))

df_pop_food = pd.DataFrame({
    'Year': Food_yearly.index,
    'Population Growth Rate (%)': population_data['Cumulative Growth'],
    'Food Production Growth Rate (%)': Food_yearly['Cumulative Growth']
})

#Hypothesis testing: Population growth rate vs Food production growth rate
# print(df_pop_food.corr(method='pearson'))

# #P values of the correlation
# print(df_pop_food.corr(method=lambda x, y: pearsonr(x, y)[1])['Population Growth Rate (%)']['Food Production Growth Rate (%)'])

#Hypothesis Testing #2 using scipy.stats
f, ax = plt.subplots(figsize=(8, 6))

print(pearsonr(df_pop_food['Population Growth Rate (%)'], df_pop_food['Food Production Growth Rate (%)']))

sns.lineplot(data=df_pop_food, x=df_pop_food['Year'], y=df_pop_food['Population Growth Rate (%)'], 
             ax=ax, label='Population Growth Rate', color='#A03232' )
sns.regplot(x=df_pop_food['Year'], y=df_pop_food['Food Production Growth Rate (%)'], scatter=False, 
            label='Food Production Growth Rate', color='#29AF67', line_kws={'lw': 1, 'alpha': 0.5})
sns.lineplot(data=Food_yearly,x=Food_yearly.index,y='Cumulative Growth',color='#29AF67')

# sns.set_theme(rc={'figure.figsize':(16,9)})
sns.set_theme(style="darkgrid")
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Cumulative Growth Rate (%)", fontsize=14)

Popu = sns.lineplot(data=population_data,x=population_data.index,y='Cumulative Growth', color='#A03232')

plt.title("Population Growth Rate vs Food Production Growth Rate", fontsize=16, pad=20)
plt.show()

