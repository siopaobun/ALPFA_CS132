# @title Libraries
import os

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

import seaborn as sns

import datetime

# @title Datasets

url_ipi_hunger = 'https://drive.google.com/file/d/1W_NW8Gk4m9TcH4R4THdeW7fTTz4Rfdyw/view?usp=sharing'
url_ipi_hunger = 'https://drive.google.com/uc?id=' + url_ipi_hunger.split('/')[-2]
ipi_hunger = pd.read_csv(url_ipi_hunger,sep=',') # type: ignore

# @title Design Elements

# COLORS
colors = ["#648FFF", "#785EF0", "#DC267F", "#FE6100", "#FFB000", "#000000", "#FFFFFF"]
colors_grad = sns.color_palette('flare_r',  12)
colors_heat1 = sns.color_palette('flare_r', as_cmap=True)
colors_heat2 = sns.diverging_palette(315, 261, s=74, l=50, center='dark', as_cmap=True)

color_bg = "#1B181C"
color_text = "#FFFFFF"

# @title Plot settings
mpl.rcParams['figure.dpi'] = 50
mpl.rcParams["figure.figsize"] = 16,16

# Text
mpl.rcParams['font.family'] = 'Roboto'

# Title
mpl.rcParams['figure.titlesize'] = 32
mpl.rcParams['axes.titlesize'] = 32
mpl.rcParams['axes.titleweight'] = 'bold'

# Labels
mpl.rcParams['axes.labelsize'] = 22
mpl.rcParams['xtick.labelsize'] = 22
mpl.rcParams['ytick.labelsize'] = 22

# Spacing
mpl.rcParams['axes.titlepad'] = 72
mpl.rcParams['axes.labelpad'] = 10
mpl.rcParams['xtick.major.pad'] = 10
mpl.rcParams['ytick.major.pad'] = 10
mpl.rcParams['xtick.major.width'] = 0
mpl.rcParams['xtick.minor.width'] = 0
mpl.rcParams['ytick.major.width'] = 0
mpl.rcParams['ytick.minor.width'] = 0

# Spines and grids
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.grid'] = False

# Legends
mpl.rcParams['legend.title_fontsize'] = 18
mpl.rcParams['legend.fontsize'] = 18
mpl.rcParams['legend.frameon'] = False

# Bars
plt.rcParams['patch.linewidth'] = 0
plt.rcParams['patch.edgecolor'] = 'none'

# Colors
mpl.rcParams["figure.facecolor"] = color_bg
mpl.rcParams["axes.facecolor"] = color_bg
mpl.rcParams["savefig.facecolor"] = color_bg

# Text colors
mpl.rcParams['text.color'] = color_text
mpl.rcParams['axes.labelcolor'] = color_text
mpl.rcParams['xtick.color'] = color_text
mpl.rcParams['ytick.color'] = color_text

# Line colors
mpl.rcParams['axes.edgecolor'] = color_text

# @title Visualizations

years = ipi_hunger['Year']
df_ipi_hunger = pd.DataFrame({
    'Year': years,
    'Cumulative IPI Growth (%)': ipi_hunger['Cumulative IPI Growth (%)'],
    'Cumulative Hunger Growth (%)': ipi_hunger['Cumulative Hunger Growth (%)']})

f, ax = plt.subplots(figsize=(16, 8))

sns.lineplot(x='Year', y='value', hue='variable', ax=ax, palette=colors[1:3], data=pd.melt(df_ipi_hunger, ['Year']))
g = sns.regplot(x=ipi_hunger['Year'], y=ipi_hunger['Cumulative IPI Growth (%)'], scatter=False, line_kws={'lw':1, 'color':colors[1], 'alpha':0.5})
g = sns.regplot(x=ipi_hunger['Year'], y=ipi_hunger['Cumulative Hunger Growth (%)'], scatter=False, line_kws={'lw':1, 'color':colors[2], 'alpha':0.5})


g.xaxis.set_major_locator(ticker.MultipleLocator(2))
g.xaxis.set_major_formatter(ticker.ScalarFormatter())

ax.set(xlabel="Year", ylabel="Cumulative Growth (%)")
ax.set_title('Food Production Growth and Hunger Growth Per Year (2001-2021)')

if 'output.png' == True:    
    os.remove('output.png') 

plt.savefig('output.png', dpi=100, bbox_inches='tight')
print(pearsonr(df_ipi_hunger['Cumulative IPI Growth (%)'], df_ipi_hunger['Cumulative Hunger Growth (%)']))

os.remove('C:/Users/Alec/.matplotlib/fontlist-v330.json') 
