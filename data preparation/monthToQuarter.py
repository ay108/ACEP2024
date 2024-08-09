# import pandas as pd

# def monthlyToQuarterly():
#     df = pd.read_excel('MonthlyData.xlsx')

#     # Ensure the 'Date' column is in datetime format
#     df['Date'] = pd.to_datetime(df['Date'])

#     # Set the 'Date' column as the index
#     df.set_index('Date', inplace=True)

#     # Group by quarter and aggregate data
#     quarterly_data = df.resample('Q').agg({
#         'FPP': 'first',           # First value of 'fpp' for the quarter
#         'Effective': 'first',     # First value of 'effective rates' for the quarter
#         'Min Temp Min': 'min',    # Minimum of 'min temp' for the quarter
#         'Min Temp Mean': 'mean',  # Mean of 'min temp' for the quarter
#         'Crude oil Prod': 'sum',  # Sum of 'crude oil prod' for the quarter
#         'Natural Gas Prices': 'mean',  # Average of 'natural gas prices' for the quarter,
#         'DFO': 'sum',
#         'RFO': 'sum',
#         'SUB': 'sum',
#         'WC': 'sum', 
#         'WND': 'sum', 
#         'WO': 'sum', 
#         'JF': 'sum',
#         'WAT': 'sum',
#         'LIG': 'sum', 
#         'Battery': 'sum', 
#         'Net Gen': 'sum'
#     }).reset_index()

#     # Adjust the dates to the specific quarterly start dates
#     def adjust_quarterly_dates(dates):
#         adjusted_dates = []
#         for date in dates:
#             if date.month == 3: # Adjust for March
#                 adjusted_dates.append(pd.Timestamp(year=date.year, month=3, day=1))
#             elif date.month == 6: # Adjust for June
#                 adjusted_dates.append(pd.Timestamp(year=date.year, month=6, day=1))
#             elif date.month == 9: # Adjust for September
#                 adjusted_dates.append(pd.Timestamp(year=date.year, month=9, day=1))
#             elif date.month == 12: # Adjust for December
#                 adjusted_dates.append(pd.Timestamp(year=date.year, month=12, day=1))
#         return adjusted_dates

import pandas as pd

def monthlyToQuarterly():
    df = pd.read_excel('MonthlyData.xlsx')

    # Ensure the 'Date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)

    # Group by quarter and aggregate data
    quarterly_data = df.resample('Q').agg({
        
        'Crude Prices': 'mean',  # Average of 'natural gas prices' for the quarter,

    }).reset_index()

    # Adjust the dates to the specific quarterly start dates
    def adjust_quarterly_dates(dates):
        adjusted_dates = []
        for date in dates:
            if date.month == 3: # Adjust for March
                adjusted_dates.append(pd.Timestamp(year=date.year, month=3, day=1))
            elif date.month == 6: # Adjust for June
                adjusted_dates.append(pd.Timestamp(year=date.year, month=6, day=1))
            elif date.month == 9: # Adjust for September
                adjusted_dates.append(pd.Timestamp(year=date.year, month=9, day=1))
            elif date.month == 12: # Adjust for December
                adjusted_dates.append(pd.Timestamp(year=date.year, month=12, day=1))
        return adjusted_dates



    # Apply the adjustment
    quarterly_data['Date'] = adjust_quarterly_dates(quarterly_data['Date'])

    # Save to Excel as quarterly data
    quarterly_data.to_excel('newshitz.xlsx', header = False)

monthlyToQuarterly()

