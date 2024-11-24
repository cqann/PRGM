import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Load the first account's CSV file into a pandas DataFrame
file_path1 = 'kort_konto.csv'  # Replace with the path to the first CSV file
file_path2 = 'spar_konto.csv'  # Replace with the path to the second CSV file
json_file_path = 'avanza_port.json'  # Replace with the path to your JSON file

# Read the CSV files
df1 = pd.read_csv(file_path1, sep=';', encoding='utf-8')
df2 = pd.read_csv(file_path2, sep=';', encoding='utf-8')

# Convert 'Bokföringsdatum' to datetime
df1['Bokföringsdatum'] = pd.to_datetime(df1['Bokföringsdatum'], format='%Y-%m-%d')
df2['Bokföringsdatum'] = pd.to_datetime(df2['Bokföringsdatum'], format='%Y-%m-%d')

# Ensure 'Saldo' and 'Belopp' are numeric
df1['Saldo'] = pd.to_numeric(df1['Saldo'])
df1['Belopp'] = pd.to_numeric(df1['Belopp'])
df2['Saldo'] = pd.to_numeric(df2['Saldo'])

# --- Identify Internal Transfers to AVANZA ---

# Filter transactions where 'Text' contains 'AVANZA'
df_avanza_transfers = df1[df1['Text'].str.contains('AVANZA', case=False, na=False)]

# Create a 'NetCashFlowToAvanza' column (negative of 'Belopp')
df_avanza_transfers['NetCashFlowToAvanza'] = -df_avanza_transfers['Belopp']

# Group by date and sum 'NetCashFlowToAvanza'
daily_net_cashflow = df_avanza_transfers.groupby('Bokföringsdatum')['NetCashFlowToAvanza'].sum()

# Compute cumulative net cash flow over time
cumulative_net_cashflow_to_avanza = daily_net_cashflow.cumsum()

# Reindex to match the date range of 'eod_saldo1'
all_dates_accounts = pd.date_range(start=min(df1['Bokföringsdatum'].min(), df2['Bokföringsdatum'].min()),
                                   end=max(df1['Bokföringsdatum'].max(), df2['Bokföringsdatum'].max()))
cumulative_net_cashflow_to_avanza = cumulative_net_cashflow_to_avanza.reindex(
    all_dates_accounts).fillna(method='ffill').fillna(0)

# --- Compute EOD Saldo for 'kort_konto' ---

# Group by 'Bokföringsdatum' and get the last saldo for each day
eod_saldo1 = df1.groupby('Bokföringsdatum')['Saldo'].last()

# Reindex to include all dates and fill missing values
eod_saldo1 = eod_saldo1.reindex(all_dates_accounts).fillna(method='ffill').fillna(0)

# Adjust 'eod_saldo1' by adding back the cumulative net cash flow to AVANZA
adjusted_eod_saldo1 = eod_saldo1 + cumulative_net_cashflow_to_avanza

# --- Compute EOD Saldo for 'spar_konto' ---

# Group by 'Bokföringsdatum' and get the last saldo for each day
eod_saldo2 = df2.groupby('Bokföringsdatum')['Saldo'].last()

# Reindex to include all dates and fill missing values
eod_saldo2 = eod_saldo2.reindex(all_dates_accounts).fillna(method='ffill').fillna(0)

# --- Combine the Adjusted Bank Account Balances ---

combined_saldo_accounts = adjusted_eod_saldo1 + eod_saldo2

# --- Read and Process the Portfolio Data from JSON ---

# Read and parse the JSON file
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract the 'absoluteSeries' data
portfolio_series = data['absoluteSeries']

# Create lists for timestamps and values
timestamps = []
values = []

for entry in portfolio_series:
    # Extract timestamp and convert to datetime
    timestamp = entry['timestamp'] / 1000  # Convert milliseconds to seconds
    date = datetime.utcfromtimestamp(timestamp).date()
    # Extract value
    value = 0  # entry['performance']['value']
    # Append to lists
    timestamps.append(date)
    values.append(value)

# Create a DataFrame from the lists
df_portfolio = pd.DataFrame({'Date': timestamps, 'PortfolioValue': values})

# Convert 'Date' to datetime
df_portfolio['Date'] = pd.to_datetime(df_portfolio['Date'])

# Set 'Date' as index
df_portfolio.set_index('Date', inplace=True)

# Remove duplicates by keeping the last value for each date (if any)
df_portfolio = df_portfolio[~df_portfolio.index.duplicated(keep='last')]

# Create a date range spanning all dates in the portfolio data
all_dates_portfolio = pd.date_range(start=df_portfolio.index.min(),
                                    end=df_portfolio.index.max())

# Reindex the portfolio data to include all dates, filling missing values with the previous value
portfolio_values = df_portfolio['PortfolioValue'].reindex(all_dates_portfolio).fillna(method='ffill').fillna(0)

# --- Combine All Data ---

# Combine the date ranges from accounts and portfolio
combined_dates = pd.date_range(start=min(combined_saldo_accounts.index.min(), portfolio_values.index.min()),
                               end=max(combined_saldo_accounts.index.max(), portfolio_values.index.max()))

# Reindex the accounts and portfolio data to the combined date range
combined_saldo_accounts = combined_saldo_accounts.reindex(combined_dates).fillna(method='ffill').fillna(0)
portfolio_values = portfolio_values.reindex(combined_dates).fillna(method='ffill').fillna(0)

# --- Compute Total Wealth ---

# Sum the adjusted bank account balances with the portfolio values
total_wealth = combined_saldo_accounts + portfolio_values


# Truncate 'total_wealth' to start from 2020-09-01
start_date = '2020-09-01'
total_wealth = total_wealth[total_wealth.index >= start_date]
# --- Plotting the Total Wealth ---

plt.figure(figsize=(12, 6))
plt.plot(total_wealth.index, total_wealth.values, label='Total Wealth', linestyle="-")
plt.title('Total Wealth Over Time (Adjusted Bank Accounts + Stock Portfolio)')
plt.xlabel('Date')
plt.ylabel('Value (SEK)')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
