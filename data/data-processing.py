# data processing 
import pandas as pd
import numpy as np

clt = pd.read_csv('weather_data/CLT.csv')
cqt = pd.read_csv('weather_data/CQT.csv')
ind = pd.read_csv('weather_data/IND.csv')
jax = pd.read_csv('weather_data/JAX.csv')
mdw = pd.read_csv('weather_data/MDW.csv')
phl = pd.read_csv('weather_data/PHL.csv')
phx = pd.read_csv('weather_data/PHX.csv')
datasets = [clt, cqt, ind, jax, mdw, phl, phx]

def get_df_name(df):
    name =[x for x in globals() if globals()[x] is df][0]
    return name

for dataset in datasets:
    dataset['city'] = get_df_name(dataset)

data = clt.append(cqt)
data = data.append(ind)
data = data.append(jax)
data = data.append(mdw)
data = data.append(phl)
data = data.append(phx)
data
count = 0
for df in datasets : 
    count = count + len(df)
count
data['year_season'] = np.nan
for ind in data.index:
    row_year = data.iloc[ind]['date'][0:4]
    row_month = data.iloc[ind]['date'][5:7]
    if "-" in row_month :
        row_month = row_month[0]
    row_month = np.int64(row_month)
    year_season = ''
    if row_month == 1 or row_month == 2 :
        year_season = "Winter " + row_year
    elif row_month == 12 :
        row_year = np.int64(row_year) + 1
        row_year = str(row_year)
        year_season = "Winter" + row_year 
    elif row_month == 3 or row_month == 4 or row_month == 5 :
        year_season = "Spring " + row_year
    elif row_month == 6 or row_month == 7 or row_month == 8 :
        year_season = "Summer " + row_year
    elif row_month == 9 or row_month == 10 or row_month == 11 :
        year_season = "Fall " + row_year
    data.at[ind, 'year_season'] = year_season
    print(year_season)

data.to_csv("data.csv")
len(data[(data['city'] == 'mdw') & (data['year_season'] == 'Fall 2014')])
