import pandas as pd
from time import strptime

# #read in a csv file
# df = pd.read_csv('naturalgasprices.csv')

# #make a list like x= [["Dec-2005",836], ...
# data = df.values.tolist()
# #get rid of first two rows and last row
# data = data[2:-1]
# print(data)

# # #make it so that the second value in the tuple is an integer
# for i in range(len(data)):
#     #cast the second value in the tuple to an integer
#     data[i][1] = data[i][1].replace(",","")
#     data[i][1] = float(data[i][1])

# print(data)

# for i in range(len(data)):
#      date = (data[i][0].split("-"))
#      month = date[0]
#      year = date[1]
#      month = str(strptime(month,'%b').tm_mon)
#      if(len(month)!=2):
#           month = "0"+month
#      data[i][0]= (str(year)+ "-"+ month+ "-01")
# print(data)

# df = pd.DataFrame(data, columns = ["date", "natural gas prices"])
# df['date']= pd.to_datetime(df['date'], format='%Y-%m-%d')

# start_date = '2006-01-01'
# end_date = df['date'].max()
# daily_dates = pd.date_range(start=start_date, end=end_date, freq='D')
# daily_df = pd.DataFrame(daily_dates, columns=['date'])
# # # # # # Merge the daily dates DataFrame with the quarterly data DataFrame
# merged_df = pd.merge(daily_df, df, on='date', how='left')
# merged_df.fillna(method='ffill', inplace=True)

# merged_df.to_csv("naturalgasprices.csv" , index = True)

df = pd.read_csv('naturalgasprices.csv')

#make the start date 2006-01-01
start_date = '2006-01-01'
#cut off all values/rows before this
df = df[df['date'] >= start_date]

print(df.head())

#save to file
df.to_csv("naturalgasprices.csv", index = False)