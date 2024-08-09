import pandas as pd
def prepDF(year):
    #read in an excel file first sheet
    data = pd.read_excel("EIA_" + str(year)+ ".xlsx", sheet_name= 0)
    #Create a dataframe from that
    df = pd.DataFrame(data)
    #Print the first 5 rows of the dataframe

    #filter out the rows that dont have "Golden Valley Elec Assn Inc" as their Operator Name
    df = df[df['Operator Name'] == "Golden Valley Elec Assn Inc"]
    
    #only keep certain columns
    required_columns = [col for col in df.columns if col.startswith('Reported Fuel') or col.startswith('NETGEN')  or col.startswith('Netgen') or col.startswith("Operator Name") or col.startswith("Physical") or col.startswith("NET GENERATION")]

    #save as df
    df = df[required_columns]

    #add a column "year" to the dataframe
    df['year'] = year
    print(df.head())

    #add to csv file
    df.to_csv("2024Update.csv", header = True, mode = 'w', index = False)

prepDF(2024)



def get_net_gen(year):
    #open the excel sheet
    df = pd.read_excel('EIA_'+str(year)+'.xlsx', sheet_name=0)
    df = df.dropna(subset=['Operator Name'])

    print("Column names in the DataFrame:")
    print(df.columns)


    #filter out all except the rows that start with "Golden Valley"
    df = df[df['Operator Name'].str.contains('Golden Valley')]
    print(df.head())

    #in that df, group by the Reported Fuel Type, and sum the Net Generation (Megawatthours)
    df = df.groupby('Reported\nFuel Type Code')['Net Generation\n(Megawatthours)'].sum()
    print(df.head())
    #make the df with columns as fuel type and year as another column
    df = pd.DataFrame(df)
    df['year'] = year
    print(df.head())
    #add to a csv with the fuel type as columns and year as another column
    df.to_csv('net_gen_GVEA.csv', mode = 'a', header=True, index = False)  

get_net_gen(2024)