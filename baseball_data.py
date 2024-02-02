import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


df_2018_2022 = pd.read_csv('pitch_data_2018-2022_aggregate.csv') # aggregate pitching stats

df_2018 = pd.read_csv('pitch_data_2018_regular_season.csv')
df_2019 = pd.read_csv('pitch_data_2019_regular_season.csv')
df_2020 = pd.read_csv('pitch_data_2020_regular_season.csv')
df_2021 = pd.read_csv('pitch_data_2021_regular_season.csv')
df_2022 = pd.read_csv('pitch_data_2022_regular_season.csv')
df_2023 = pd.read_csv('pitch_data_2023_regular_season.csv') # yearly pitching stats

## data frames currently have the same columns in the same locations, but teams row index varies
## across year, the code below corrects that

df_pitching_list = [df_2018, df_2019, df_2020, df_2021, df_2022, df_2023, df_2018_2022]

for item in df_pitching_list:
    item.sort_values(by=['Team'], ascending=True, inplace=True)
    print(item.head(30))


#Testing out matplotlib, this graphs 2023 era by team
era_2023 = df_2023['ERA'].tolist()
team_name = df_2023['Team'].tolist()
plt.plot(era_2023, 'ro')
plt.xticks(range(len(team_name)), team_name, rotation = 'vertical')
plt.show()
