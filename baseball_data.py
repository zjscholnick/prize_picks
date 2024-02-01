import pandas as pd
import numpy as np



df_2018_2022 = pd.read_csv('pitch_data_2018-2022_aggregate.csv') # aggregate pitching stats

df_2018 = pd.read_csv('pitch_data_2018_regular_season.csv')
df_2019 = pd.read_csv('pitch_data_2019_regular_season.csv')
df_2020 = pd.read_csv('pitch_data_2020_regular_season.csv')
df_2021 = pd.read_csv('pitch_data_2021_regular_season.csv')
df_2022 = pd.read_csv('pitch_data_2022_regular_season.csv')
df_2023 = pd.read_csv('pitch_data_2023_regular_season.csv') # yearly pitching stats

## data frames currently have the same columns in the same locations, but teams row index varies
## across year
