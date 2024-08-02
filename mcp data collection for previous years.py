# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:02:28 2024

@author: Eleni
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
"""
2020 files
"""
folder_path  = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2020_EL-DAM_PrelimResults\PrelimResults"
files = os.listdir(folder_path)

# Filter the list to include only .xlsx or .xls files
excel_files = [file for file in files if file.endswith(('.xlsx'))]

# Read each Excel file into a DataFrame and store them in a list
dfs = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path, sheet_name = 'SITE_BZ_NP_PRICES')
    dfs.append(df)

# Concatenate all DataFrames along axis 0
concatenated_df = pd.concat(dfs, axis=0, ignore_index=True)
concatenated_df.info()
concatenated_df['DELIVERY_MTU'] = pd.to_datetime(concatenated_df['DELIVERY_MTU'])
concatenated_df.drop(['BIDDING_ZONE_EIC', 'DDAY', 'DELIVERY_DURATION', 'SORT', 'PUB_TIME', 'VER'], axis = 1, inplace = True)
#find if all transactions are refering to DAM
distinct_names = concatenated_df['TARGET'].unique()
distinct_names
#indeed we only have DAM so we can drop this column
#Do the same for the bidding zone
distinct_names = concatenated_df['BIDDING_ZONE_DESCR'].unique()
distinct_names
#indeed we only have Mainland Greece so we can drop this column
concatenated_df.drop(['BIDDING_ZONE_DESCR', 'TARGET'], axis = 1, inplace = True)
concatenated_df.set_index('DELIVERY_MTU', inplace = True)
dam_2020 = concatenated_df
dam_2020.info()

#No CRIDA/LIDA data here
"""
2021 files
"""
folder_path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2021_EL-DAM-CRIDAs_PrelimResults\2021_EL-DAM_PrelimResults"
files = os.listdir(folder_path)

# Filter the list to include only .xlsx or .xls files
excel_files = [file for file in files if file.endswith(('.xlsx'))]

# Read each Excel file into a DataFrame and store them in a list
dfs = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path, sheet_name = 'SITE_BZ_NP_PRICES')
    dfs.append(df)
    
# Concatenate all DataFrames along axis 0
concatenated_df = pd.DataFrame()
concatenated_df = pd.concat(dfs, axis=0, ignore_index=True)
concatenated_df.info()
concatenated_df['DELIVERY_MTU'] = pd.to_datetime(concatenated_df['DELIVERY_MTU'])
concatenated_df.drop(['BIDDING_ZONE_EIC', 'DDAY', 'DELIVERY_DURATION', 'SORT', 'PUB_TIME', 'VER'], axis = 1, inplace = True)
#find if all transactions are refering to DAM
distinct_names = concatenated_df['TARGET'].unique()
distinct_names
#indeed we only have DAM so we can drop this column
#Do the same for the bidding zone
distinct_names = concatenated_df['BIDDING_ZONE_DESCR'].unique()
distinct_names
#indeed we only have Mainland Greece so we can drop this column
concatenated_df.drop(['BIDDING_ZONE_DESCR', 'TARGET'], axis = 1, inplace = True)
concatenated_df.set_index('DELIVERY_MTU', inplace = True)
dam_2021 = concatenated_df

"""
2022 files
"""
folder_path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2022_EL-DAM-CRIDAs_Results\2022_EL-DAM_Results"
files = os.listdir(folder_path)

# Filter the list to include only .xlsx or .xls files
excel_files = [file for file in files if file.endswith(('.xlsx'))]

# Read each Excel file into a DataFrame and store them in a list
dfs = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    dfs.append(df)
    
# Concatenate all DataFrames along axis 0
concatenated_df = pd.DataFrame()
concatenated_df = pd.concat(dfs, axis=0, ignore_index=True)
concatenated_df.info()
concatenated_df['DELIVERY_MTU'] = pd.to_datetime(concatenated_df['DELIVERY_MTU'])
concatenated_df.drop(['DDAY', 'DELIVERY_DURATION', 'SORT', 'PUB_TIME', 'VER'], axis = 1, inplace = True)
#find if all transactions are refering to DAM
distinct_names = concatenated_df['TARGET'].unique()
distinct_names
#indeed we only have DAM so we can drop this column
#Do the same for the bidding zone
distinct_names = concatenated_df['BIDDING_ZONE_DESCR'].unique()
distinct_names
#indeed we only have Mainland Greece so we can drop this column
concatenated_df.drop(['BIDDING_ZONE_DESCR', 'TARGET'], axis = 1, inplace = True)
#as we have many ASSET_DESCR, SIDE_DESCR (Buy/Sell), and CLASSIFICATION, we will group by
# the DELIVERY_MTU and sum the TOTAL_TRADES to find the total volumes going through DAM
concatenated_df.drop(['SIDE_DESCR', 'ASSET_DESCR', 'CLASSIFICATION'], axis = 1, inplace = True)
groups = concatenated_df.groupby('DELIVERY_MTU')['TOTAL_TRADES'].sum().reset_index()
concatenated_df.drop('TOTAL_TRADES', axis = 1, inplace = True)
concatenated_df = concatenated_df.drop_duplicates(subset='DELIVERY_MTU')
concatenated_df.set_index('DELIVERY_MTU', inplace = True)
groups.set_index('DELIVERY_MTU', inplace = True)
groups = pd.concat([groups, concatenated_df], axis = 1)
dam_2022 = groups   

"""
2023 files
"""
folder_path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2023 DAM"
files = os.listdir(folder_path)

# Filter the list to include only .xlsx or .xls files
excel_files = [file for file in files if file.endswith(('.xlsx'))]

# Read each Excel file into a DataFrame and store them in a list
dfs = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    dfs.append(df)
    
# Concatenate all DataFrames along axis 0
concatenated_df = pd.DataFrame()
concatenated_df = pd.concat(dfs, axis=0, ignore_index=True)
concatenated_df.info()
concatenated_df['DELIVERY_MTU'] = pd.to_datetime(concatenated_df['DELIVERY_MTU'])
concatenated_df.drop(['DDAY', 'DELIVERY_DURATION', 'SORT', 'PUB_TIME', 'VER'], axis = 1, inplace = True)
#find if all transactions are refering to DAM
distinct_names = concatenated_df['TARGET'].unique()
distinct_names
#indeed we only have DAM so we can drop this column
#Do the same for the bidding zone
distinct_names = concatenated_df['BIDDING_ZONE_DESCR'].unique()
distinct_names
#indeed we only have Mainland Greece so we can drop this column
concatenated_df.drop(['BIDDING_ZONE_DESCR', 'TARGET'], axis = 1, inplace = True)
#as we have many ASSET_DESCR, SIDE_DESCR (Buy/Sell), and CLASSIFICATION, we will group by
# the DELIVERY_MTU and sum the TOTAL_TRADES to find the total volumes going through DAM
concatenated_df.drop(['SIDE_DESCR', 'ASSET_DESCR', 'CLASSIFICATION'], axis = 1, inplace = True)
groups = concatenated_df.groupby('DELIVERY_MTU')['TOTAL_TRADES'].sum().reset_index()
concatenated_df.drop('TOTAL_TRADES', axis = 1, inplace = True)
concatenated_df = concatenated_df.drop_duplicates(subset='DELIVERY_MTU')
concatenated_df.set_index('DELIVERY_MTU', inplace = True)
groups.set_index('DELIVERY_MTU', inplace = True)
groups = pd.concat([groups, concatenated_df], axis = 1)
groups.head()
dam_2023 = groups   

"""
2024 files and you will need to add more
"""
folder_path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\2024 DAM"
files = os.listdir(folder_path)

# Filter the list to include only .xlsx or .xls files
excel_files = [file for file in files if file.endswith(('.xls'))]

# Read each Excel file into a DataFrame and store them in a list
dfs = []
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    dfs.append(df)
    
# Concatenate all DataFrames along axis 0
concatenated_df = pd.DataFrame()
concatenated_df = pd.concat(dfs, axis=0, ignore_index=True)
concatenated_df.info()
concatenated_df['DELIVERY_MTU'] = pd.to_datetime(concatenated_df['DELIVERY_MTU'])
concatenated_df.drop(['DDAY', 'DELIVERY_DURATION', 'SORT', 'PUB_TIME', 'VER'], axis = 1, inplace = True)
#find if all transactions are refering to DAM
distinct_names = concatenated_df['TARGET'].unique()
distinct_names
#indeed we only have DAM so we can drop this column
#Do the same for the bidding zone
distinct_names = concatenated_df['BIDDING_ZONE_DESCR'].unique()
distinct_names
#indeed we only have Mainland Greece so we can drop this column
concatenated_df.drop(['BIDDING_ZONE_DESCR', 'TARGET'], axis = 1, inplace = True)
#as we have many ASSET_DESCR, SIDE_DESCR (Buy/Sell), and CLASSIFICATION, we will group by
# the DELIVERY_MTU and sum the TOTAL_TRADES to find the total volumes going through DAM
concatenated_df.drop(['SIDE_DESCR', 'ASSET_DESCR', 'CLASSIFICATION'], axis = 1, inplace = True)
groups = concatenated_df.groupby('DELIVERY_MTU')['TOTAL_TRADES'].sum().reset_index()
concatenated_df.drop('TOTAL_TRADES', axis = 1, inplace = True)
concatenated_df = concatenated_df.drop_duplicates(subset='DELIVERY_MTU')
concatenated_df.set_index('DELIVERY_MTU', inplace = True)
groups.set_index('DELIVERY_MTU', inplace = True)
groups = pd.concat([groups, concatenated_df], axis = 1)
groups.tail()
dam_2024 = groups  



"""
Concat all together
"""
dam = pd.concat([dam_2020, dam_2021],axis = 0)
dam = pd.concat([dam, dam_2022], axis = 0)
dam = pd.concat([dam, dam_2023], axis = 0)
dam = pd.concat([dam, dam_2024], axis = 0)
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\DAM.xlsx"
dam.to_excel(path)
plt.plot(dam['MCP'], linestyle='-')
plt.xlabel('Date')
plt.ylabel('MCP')
plt.title('DAM MCP')
#plt.grid(True)
plt.show()

#find daily average
dam.head()
daily_avg_df = dam.resample('D').mean()
path = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\DAM daily avg.xlsx"
daily_avg_df.to_excel(path)
