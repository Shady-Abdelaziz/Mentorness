import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cricket_data = pd.read_csv("T-20 World cup 2022.csv")
print(cricket_data.columns)

cricket_data=cricket_data.drop(columns = ['comment_id', 'home_team', 'away_team'])

print(cricket_data.info())
cricket_data.head()


cricket_data.duplicated()
cricket_data.drop_duplicates(inplace= True)

# Check the dimensions (shape) of the DataFrame
dimensions = cricket_data.shape

# Display the dimensions
print("Dimensions of the DataFrame:", dimensions)




# Check for missing values
missing_values = cricket_data.isnull().sum()

# Display missing values
print("Missing Values:\n", missing_values)



cricket_data.isnull().sum()

# participated Teams

cricket_data.rename(columns={'current_innings':'batting_team'}, inplace= True)
cricket_data['batting_team'].value_counts()




top10= ['INDIA','ENG','PAK','NZ','BAN','SA','SL','AUS','WI','AFG']

country = cricket_data['batting_team'].unique()
print(country)


# Split 'match_name' into two new columns: 'team1' and 'team2'
cricket_data[['team1', 'team2']] = cricket_data['match_name'].str.split(' v ', expand=True)

# Add a new column 'bowling_team' with the team not present in 'current_inning'
cricket_data['bowling_team'] = cricket_data.apply(lambda row: row['team2'] if row['batting_team'] == row['team1'] else row['team1'], axis=1)

cricket_data.drop(columns= ['team1', 'team2'], inplace= True )
cricket_data['bowling_team'].unique()


def filtered_df(cricket_data, columns, top_teams):
    condition = cricket_data['batting_team'].isin(top_teams) & cricket_data['bowling_team'].isin(top_teams)
    return cricket_data.loc[condition, columns]



#World Top10 highest scorer batsman

batting_df1= ['batting_team','batsman1_name','batsman1_runs']
for i in country:
    filtered1 = filtered_df(cricket_data,batting_df1,top10)
filtered1.rename(columns={'batsman1_name':'batsman_name'}, inplace=True)
filtered1=filtered1.groupby('batsman_name').max().sort_values(by='batsman1_runs',ascending=False)[:10]
filtered1


batting_df2= ['batting_team','batsman2_name','batsman2_runs']
for i in country:
        filtered2 = filtered_df(cricket_data,batting_df2,top10)
filtered2.rename(columns={'batsman2_name':'batsman_name'}, inplace=True)
filtered2=filtered2.groupby('batsman_name').max().sort_values(by='batsman2_runs',ascending=False)[:10]
filtered2





# Merge the dataframes on the 'batsman1_name' and 'batsman2_name' columns

merged_df = pd.merge(filtered1, filtered2, on=('batsman_name','batting_team'))
merged_df


top_runs = cricket_data[['batsman1_name','runs']].loc[cricket_data['batting_team']=='INDIA'].groupby('batsman1_name').sum().sort_values(by='runs',ascending=False)[0:5]
top_run_getters = top_runs.index
top_run_getters


#Highest Score of Every Indian Batsman

cricket_data.loc[cricket_data['batting_team'] =='INDIA',['batting_team','batsman1_name','batsman1_runs']].groupby('batsman1_name').max().sort_values(by='batsman1_runs',ascending=False)[:5]



top5_ind = cricket_data[['match_name','batsman1_name','batsman1_runs']].loc[(cricket_data['batting_team']=='INDIA') & (cricket_data['batsman1_name'].isin(top_run_getters))].groupby(['match_name','batsman1_name']).max().sort_index().unstack()
top5_ind = top5_ind.cumsum()
top5_ind


plt.figure(figsize=(10,6))
plt.plot(top5_ind[('batsman1_runs','Virat Kohli')], label='Virat Kohli', color='Green', linewidth=2)
plt.plot(top5_ind[('batsman1_runs','Suryakumar Yadav')], label='Suryakumar Yadav', color='#242F9B', linewidth=2)
plt.plot(top5_ind[('batsman1_runs','Hardik Pandya')], label='Hardik Pandya', color='#242F9B', linewidth=2, linestyle=':')
plt.plot(top5_ind[('batsman1_runs','KL Rahul')], label='KL Rahul', color='#242F9B', linewidth=2, linestyle='--')
plt.plot(top5_ind[('batsman1_runs','Rohit Sharma')], label='Rohit Sharma', color='#FBCB0A', linewidth=2)

plt.title(" India's top 5 run getters ")
plt.xticks(rotation=90)
plt.xlabel('Versus')
plt.ylabel('Total Runs')
plt.legend()
plt.grid()
plt.savefig('India top scorers', bbox_inches='tight')
plt.show()


plt.figure(figsize=(10,6))
plt.plot(top5_ind[('batsman1_runs','Virat Kohli')], label='Virat Kohli', color='Green', linewidth=2)
plt.plot(top5_ind[('batsman1_runs','Suryakumar Yadav')], label='Suryakumar Yadav', color='#242F9B', linewidth=2)
plt.plot(top5_ind[('batsman1_runs','Hardik Pandya')], label='Hardik Pandya', color='#242F9B', linewidth=2, linestyle=':')
plt.plot(top5_ind[('batsman1_runs','KL Rahul')], label='KL Rahul', color='#242F9B', linewidth=2, linestyle='--')
plt.plot(top5_ind[('batsman1_runs','Rohit Sharma')], label='Rohit Sharma', color='#FBCB0A', linewidth=2)

plt.title(" India's top 5 run getters ")
plt.xticks(rotation=90)
plt.xlabel('Versus')
plt.ylabel('Total Runs')
plt.legend()
plt.grid()
plt.savefig('India top scorers', bbox_inches='tight')
plt.show()

