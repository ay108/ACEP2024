#CPI Index with Base Year 2009
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def cpi_index_shifting():

    df = pd.read_excel('/Users/ashleyyang/Desktop/ACEP intern/final_data/quarter.xlsx')
    #find column titled CPI
    cpi = df['CPI']
    cpi_new = []
    #for each item in CPI, create a new column and fill it with the rebased CPI
    for i in range(0,len(cpi)):
        #create a new column and fill it with the rebased CPI
        cpi_new.append(cpi[i]/cpi[0]*100)

    df["CPI_new"] = cpi_new
    print(df["CPI_new"].head())
    #append this new column to the dataframe
    #appendthis to the excel file
    df["CPI_new"].to_excel('/Users/ashleyyang/Desktop/ACEP intern/final_data/CPI_new.xlsx', index=False)


    
cpi_index_shifting()