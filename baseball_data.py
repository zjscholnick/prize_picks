import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

#import os
#print(os.getcwd())

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


#Testing out matplotlib, this graphs 2023 era by team :)
# era_2023 = df_2023['ERA'].tolist()
# team_name = df_2023['Team'].tolist()
# plt.plot(era_2023, 'ro')
# plt.xticks(range(len(team_name)), team_name, rotation = 'vertical')
# plt.show()



team_name_all = df_2018_2022['Team'].tolist()
color_list = plt.cm.Greens(np.linspace(0.2, 1, len(df_pitching_list[:-1])))
year_list = ["2018", "2019", "2020", "2021", "2022", "2023"]
i = 0
plt.figure()
for season in df_pitching_list[:-1]:
    temp_ERA = season['ERA'].tolist()
    plt.plot(temp_ERA, 'o', color = color_list[i], label = year_list[i])
    i += 1
plt.xticks(range(len(team_name_all)), team_name_all, rotation = 'vertical')
plt.legend(title = "Year")
plt.title("Average ERAs by Regular Season (2018-2023)")
plt.show() #Graphs ERAs 2018-2023 by Team

plt.figure()
era_2018_2022 = df_2018_2022['ERA'].tolist()
era_2023 = df_2023['ERA'].tolist()
plt.plot(era_2018_2022, 'ro',label = "2018-2022 Average")
plt.plot(era_2023, 'bo', label = "2023")
plt.xticks(range(len(team_name_all)), team_name_all, rotation = 'vertical')
plt.legend(title = "Year")
plt.title("Average ERAs by Regular Season")
plt.show()




