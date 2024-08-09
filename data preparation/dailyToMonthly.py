import pandas as pd

def convertToMonthly():
    # Read Excel file
    data = pd.read_excel("LSTMdata.xlsx", sheet_name=0)
    #only have rows from date 2009-09-01 to 2024-06-01
    data = data[(data['date'] >= '2009-09-01') & (data['date'] <= '2024-06-01')]
    print(data.head())    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Convert 'date' column to datetime type if it's not already
    df['date'] = pd.to_datetime(df['date'])
    
    # Group by month and aggregate data
    monthly_data = df.resample('M', on='date').agg({
        'date': 'first',  # First day of the month
        'fpp': 'first',   # First value of 'fpp' for the month
        'effective rates': 'first',  # First value of 'effective rates' for the month
        'min temp': ['min', 'mean'],  # Minimum and mean of 'min temp' for the month
        'crude oil prod (thousands of barrels)': 'sum',  # Sum of 'crude oil prod' for the month
        'natural gas prices (commercial), mmBT': 'mean'  # Average of 'natural gas prices' for the month
    }).reset_index(drop=True)
    
    # Flatten MultiIndex columns
    monthly_data.columns = ['Date', 'FPP', 'Effective', 'Min Temp Min', 'Min Temp Mean',
                            'Crude oil Prod', 'Natural Gas Prices']
    
    # Print the resulting DataFrame (optional)
    print(monthly_data.head())
    
    # Optionally, save the resulting DataFrame to a new Excel file
    monthly_data.to_excel('MonthlyData.xlsx', index=False)
    
convertToMonthly()
