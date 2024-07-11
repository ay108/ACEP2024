import pandas as pd
import matplotlib.pyplot as plt
data = [
    ['9/1/2009', 0.08142, 0.08352, 0.16494],
    ['12/1/2009', 0.08142, 0.09886, 0.18028],
    ['1/1/2010', 0.08337, 0.09886, 0.18223],
    ['3/1/2010', 0.08337, 0.0989, 0.18227],
    ['6/1/2010', 0.08337, 0.09401, 0.17738],
    ['9/1/2010', 0.08337, 0.09137, 0.17474],
    ['12/1/2010', 0.08337, 0.08929, 0.17266],
    ['3/1/2011', 0.08337, 0.10051, 0.18388],
    ['6/1/2011', 0.08791, 0.10051, 0.18842],
    ['9/16/2011', 0.08791, 0.10943, 0.19734],
    ['9/17/2011', 0.08791, 0.10924, 0.19715],
    ['12/1/2011', 0.08790, 0.12737, 0.20647],
    ['1/1/2012', 0.09004, 0.12737, 0.21741],
    ['3/1/2012', 0.09004, 0.12527, 0.21531],
    ['6/1/2012', 0.09004, 0.12379, 0.21383],
    ['9/1/2012', 0.09004, 0.13768, 0.22772],
    ['12/1/2012', 0.09004, 0.10802, 0.19806],
    ['1/1/2013', 0.09597, 0.10802, 0.20399],
    ['3/1/2013', 0.09597, 0.11078, 0.20675],
    ['6/1/2013', 0.09724, 0.08774, 0.18498],
    ['9/1/2013', 0.09724, 0.10576, 0.203],
    ['12/1/2013', 0.09724, 0.09631, 0.19355],
    ['1/1/2014', 0.10001, 0.09631, 0.19632],
    ['3/1/2014', 0.10001, 0.09496, 0.19497],
    ['6/1/2014', 0.10341, 0.10593, 0.20934],
    ['9/2/2014', 0.10341, 0.10378, 0.20719],
    ['12/1/2014', 0.10341, 0.09947, 0.20288],
    ['1/1/2015', 0.10771, 0.07111, 0.17882],
    ['6/1/2015', 0.10771, 0.07297, 0.18068],
    ['7/1/2015', 0.10800, 0.07297, 0.18097],
    ['9/1/2015', 0.10800, 0.07202, 0.18002],
    ['12/1/2015', 0.10800, 0.07484, 0.18284],
    ['1/1/2016', 0.11508, 0.07484, 0.18992],
    ['3/1/2016', 0.11508, 0.06099, 0.17607],
    ['6/1/2016', 0.11631, 0.09207, 0.20838],
    ['9/1/2016', 0.11631, 0.08365, 0.19996],
    ['12/1/2016', 0.11631, 0.08257, 0.19888],
    ['3/1/2017', 0.11631, 0.10857, 0.22488],
    ['6/1/2017', 0.11631, 0.10454, 0.22085],
    ['9/1/2017', 0.11631, 0.09385, 0.21016],
    ['12/1/2017', 0.11631, 0.09467, 0.21098],
    ['3/1/2018', 0.11631, 0.11227, 0.22858],
    ['6/1/2018', 0.11631, 0.11071, 0.22702],
    ['9/1/2018', 0.11631, 0.10502, 0.22133],
    ['11/1/2018', 0.11404, 0.10502, 0.21906],
    ['12/1/2018', 0.11404, 0.08648, 0.20052],
    ['1/1/2019', 0.12158, 0.08648, 0.20806],
    ['3/1/2019', 0.12158, 0.10129, 0.22287],
    ['6/1/2019', 0.12327, 0.09639, 0.21966],
    ['9/1/2019', 0.12327, 0.09177, 0.21504],
    ['12/1/2019', 0.12327, 0.10998, 0.23325],
    ['1/1/2020', 0.12697, 0.10998, 0.23695],
    ['3/1/2020', 0.12697, 0.10965, 0.23662],
    ['6/1/2020', 0.12697, 0.07095, 0.19792],
    ['9/1/2020', 0.12697, 0.09614, 0.22311],
    ['12/1/2020', 0.12697, 0.08172, 0.20869],
    ['3/1/2021', 0.12697, 0.09655, 0.22352],
    ['6/1/2021', 0.12697, 0.09978, 0.22675],
    ['9/1/2021', 0.12697, 0.1071, 0.23407],
    ['12/1/2021', 0.12697, 0.10450, 0.23147],
    ['3/1/2022', 0.12697, 0.12969, 0.25666],
    ['6/1/2022', 0.12697, 0.14036, 0.26733],
    ['9/1/2022', 0.12697, 0.12726, 0.25423],
    ['12/1/2022', 0.12697, 0.09164, 0.21861],
    ['1/1/2023', 0.12973, 0.09164, 0.22137],
    ['3/1/2023', 0.12973, 0.12106, 0.25079],
    ['6/1/2023', 0.13109, 0.12889, 0.25998],
    ['9/1/2023', 0.13109, 0.12057, 0.25166],
    ['12/1/2023', 0.13109, 0.11763, 0.24872],
    ['1/1/2024', 0.13378, 0.11763, 0.25141],
    ['3/1/2024', 0.13378, 0.16629, 0.30007],
    ['6/1/2024', 0.14047, 0.13731, 0.27778]
]

df = pd.DataFrame(data, columns = ["date", "fpp", "utility", "effective_rate"])
df["date"] = pd.to_datetime(df["date"], format = "%m/%d/%Y")

start_date = df["date"].min()
end_date = df["date"].max()
daily_dates = pd.date_range(start = start_date, end = end_date, freq = "D")
daily_df = pd.DataFrame(daily_dates, columns = ["date"])
merged_df = pd.merge(daily_df, df, on = "date", how = "left")

merged_df.fillna(method = "ffill", inplace = True)

#drop columns fpp and utility
merged_df.drop(columns = ["fpp", "utility"], inplace = True)

print(merged_df.head(20))

merged_df.to_csv("effectiveRate.csv", index = False)

# #plot both effective rate and the fpp with date, corresponding to each quarter (3 months)
# df.plot(x = "date", y = ["effective_rate", "fpp"], kind = "line")

# #show plot
# plt.show()

# start_date = df['date'].min()
# end_date = df['date'].max()
# daily_dates = pd.data_range(start = start_date, end = end_date, freq = "D")
# daily_df = pd.DataFrame(daily_dates, columns = ['date'])

# merged_df = pd.merge(daily_df, df, on = "date", how = "left")
# merged_df.fillna(method = "ffill", inplace = True)

# # Create a DataFrame
# df = pd.DataFrame(data, columns=['date', 'utility_charge', 'fpp', 'effective_rate'])


# # Convert the 'date' column to datetime format
# df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# # Create a DataFrame with daily dates
# start_date = df['date'].min()
# end_date = df['date'].max()
# daily_dates = pd.date_range(start=start_date, end=end_date, freq='D')
# daily_df = pd.DataFrame(daily_dates, columns=['date'])

# # Merge the daily dates DataFrame with the quarterly data DataFrame
# merged_df = pd.merge(daily_df, df, on='date', how='left')

# # Forward fill the NaN values to propagate the quarterly data to daily
# merged_df.fillna(method='ffill', inplace=True)

# # Display the first few rows of the merged DataFrame
# print(merged_df.head(20))
# ##save df to a csv file, replacing it if it exists
# df.to_csv('features.csv', index=False)


# dataNew = [["12/1/2005", 0.06758],
#            ["3/1/2006", 0.06758], 
#            ["6/1/2006", 0.06477], 
#            ["9/1/2006",  0.07576], 
#            ["12/1/2006", 0.06625], 
#            ["3/1/2007",  0.06791], 
#            ["6/1/2007", 0.06845], 
#            ["9/1/2007", 0.07337],
#            ["12/1/2007", 0.09254], 
#            ["3/1/2008", 0.10030],
#            ["6/1/2008", 0.13004], 
#            ["9/1/2008", 0.12240],
#            ["12/1/2008", 0.07979],
#            ["3/1/2009", 0.05215], 
#            ["6/1/2009", 0.06536], 
#            ["9/1/2009", 0.08352],]
# dfNew = pd.DataFrame(dataNew, columns=['date', 'fpp'])
# dfNew['date'] = pd.to_datetime(dfNew['date'], format='%m/%d/%Y')
# start_dateN = dfNew['date'].min()
# end_dateN = dfNew['date'].max()
# daily_datesN = pd.date_range(start=start_dateN, end=end_dateN, freq='D')
# daily_dfN = pd.DataFrame(daily_datesN, columns=['date'])
# # Merge the daily dates DataFrame with the quarterly data DataFrame
# merged_dfNew = pd.merge(daily_dfN, dfNew, on='date', how='left')

# merged_dfNew.fillna(method='ffill', inplace=True)


# print(merged_dfNew.head(20))

# merged_dfNew.to_csv("featuresNew.csv" , index = False)

# dataUtility = [
#     ["9/1/2009", 0.08142, 0.08352, 0.16494],
#     ["12/1/2009", 0.08142, 0.09886, 0.18028],
#     ["1/1/2010", 0.08337, 0.09886, 0.18223],
#     ["3/1/2010", 0.08337, 0.09890, 0.18227],
#     ["6/1/2010", 0.08337, 0.09401, 0.17738],
#     ["9/1/2010", 0.08337, 0.09137, 0.17474],
#     ["12/1/2010", 0.08337, 0.08929, 0.17266],
#     ["3/1/2011", 0.08337, 0.10051, 0.18388],
#     ["6/1/2011", 0.08791, 0.10051, 0.18842],
#     ["9/16/2011", 0.08791, 0.10943, 0.19734],
#     ["9/17/2011", 0.08791, 0.10924, 0.19715],
#     ["12/1/2011", 0.08790, 0.12737, 1.00647],
#     ["1/1/2012", 0.09004, 0.12737, 0.21741],
#     ["3/1/2012", 0.09004, 0.12527, 0.21531],
#     ["6/1/2012", 0.09004, 0.12379, 0.21383],
#     ["9/1/2012", 0.09004, 0.13768, 0.22772],
#     ["12/1/2012", 0.09004, 0.10802, 0.19806],
#     ["1/1/2013", 0.09597, 0.10802, 0.20399],
#     ["3/1/2013", 0.09597, 0.11078, 0.20675],
#     ["6/1/2013", 0.09724, 0.08774, 0.18498],
#     ["9/1/2013", 0.09724, 0.10576, 0.203],
#     ["12/1/2013", 0.09724, 0.09631, 0.19355],
#     ["1/1/2014", 0.10001, 0.09631, 0.19632],
#     ["3/1/2014", 0.10001, 0.09496, 0.19497],
#     ["6/1/2014", 0.10341, 0.10593, 0.20934],
#     ["9/2/2014", 0.10341, 0.10378, 0.20719],
#     ["12/1/2014", 0.10341, 0.09947, 0.20288]
# ]
# ##discard the last two elements in every tuple
# print(len(dataUtility))
# #for i in range(len(dataUtility)):


# dfUtility = pd.DataFrame(dataUtility, columns=['date', 'utility_charge'])
# dfUtility['date']= pd.to_datetime(dfUtility['date'], format='%m/%d/%Y')
# start_dateU = dfUtility['date'].min()
# end_dateU = dfUtility['date'].max()
# daily_datesU = pd.date_range(start=start_dateU, end=end_dateU, freq='D')
# daily_dfU = pd.DataFrame(daily_datesU, columns=['date'])
# # Merge the daily dates DataFrame with the quarterly data DataFrame
# merged_dfUtility = pd.merge(daily_dfU, dfUtility, on='date', how='left')

# merged_dfUtility.fillna(method='ffill', inplace=True)

# print(merged_dfUtility.head(20))