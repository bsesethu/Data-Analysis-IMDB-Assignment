import kagglehub
import pandas as pd
import numpy as np
from functions_Assignment_2 import Data_Collection as DaC 
from functions_Assignment_2 import Data_Preperation as DaP
from functions_Assignment_2 import Data_Visualisation as DaV
import matplotlib.pyplot as plt

# Downloading file from kagglehub
# path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
# print( "Path to dataset files:" , path)
    # File downloaded
    
df = pd.read_csv('imdb_top_1000.csv') # Doesn't want to read imdb file in the .cache folder
print(df.head())
print('\nDataFrame core info:')
print(df.info())

# Check for mising values and document their percantage
    # Using functions written into functions_Assignment_2.py file
missing = DaC.check_missing(df) 

# Remove rows with missing critical data, from the following columns
df_new = DaC.remove_rows(df, 'Meta_score')
df_new = DaC.remove_rows(df_new, 'Gross')
print('\nAfter removal of null values')
missing_df_new = DaC.check_missing(df_new)
print('\nNew DF with removed null values:')
print(df_new.info())

# Phase 2 Data preperation
# Drop duplicates
df_noDuplicates = DaC.dropDuplicates(df_new)
print('\nAfter dropped duplicates:')
print(df_noDuplicates.info()) # There are no duplicates. Function would've kept the first occurance

# Testing the 'dropDuplicates' function
# df_G = pd.DataFrame({'Name': ['Cash', 'Money', 'Money', 'Ross'],
#                      'Sex': ['Yes', 'No', 'No', 'Yes'],
#                      'Number': [1, 5, 5, 8]
#                      })
# df_noDup = DaC.dropDuplicates(df_G)
# print(df_noDup) # The function works

# Convert runtime to numerical
newRuntime = []
cnt = 0
# for i, row in df_noDuplicates.iterrows():
for row in df_noDuplicates['Runtime']:
    newRuntime.append(float(row.split(' ')[0])) # New list of numerical values only
    
# Reset indices so there are noe skipped values
df_reset = df_noDuplicates
df_reset.reset_index(inplace= True) #NOTE Index values are now reset for all affilliated DFs being used from now on

df_noDuplicates['Runtime'] = pd.DataFrame({'Runtime': newRuntime}) # Make newRuntime list a DF column by overriding the original
# print(df_noDuplicates['Runtime'].tail(50))
print(df_noDuplicates.info())

# For some reason I can't explain it's returning NaN values for the last 200 or so values of the 'Runtime' column, Let's fix this.
# Sorted: Reason for the issue is the index values of the df_duplicates DF, there are 750 values but indices go up to 997
# This program is therefore not neccessary
# for i, row in df_noDuplicates.iterrows():
#     if pd.isna(row['Runtime']): #NOTE row['Column_name'] for a specific column
        # print(i)
        # df_noDuplicates.loc[i, 'Runtime'] = newRuntime[i] # Replace NaN values

# Extract Decade from Released_Year
df_res = DaP.newColumn_ReleasedDecade(df_noDuplicates)
print(df_res.info())
print(df_res[['Released_Year', 'Released_Decade']].head()) # It checks out


# Create a Lead_Actors column combining Star1, Star2, Star3, Star4.
df_res['Lead_Actors'] = df_res[['Star1', 'Star2', 'Star3', 'Star4']].agg(', '.join, axis= 1) # New column, all 4 cell values in one, using aggregate funtion where all values are joined along the columns axis
print(df_res)


# Phase 3: Data Visualisation
# Histogram
# Convert 'IMDB_Rating' to a comparative rating with 'Meta_score', rating out of 100 not 10
df_res['IMDB_Rating'] = df_res['IMDB_Rating'] * 10
# hist = DaV.histogram(df_res, 'IMDB_Rating', 'Meta_score', 24)

# Bar plot of Genre frequency
    # First need to find the top 10 genre frequency of occurance
cntDr = 0; cntCr = 0; cntAc = 0; cntAd = 0; cntSc = 0; cntBi = 0; cntHi = 0; cntWe = 0; cntTh = 0
cntCo = 0; cntRo = 0; cntAn = 0; cntFam = 0; cntWa = 0; cntMu = 0; cntFan = 0; cntMy = 0; cntHo = 0

for row in df_res['Genre']:
    if 'Drama' in row: cntDr += 1
    if 'Crime' in row: cntCr += 1 # Not elif because a film may be of more than one genre
    if 'Action' in row: cntAc += 1
    if 'Adventure' in row: cntAd += 1
    if 'Sci-Fi' in row: cntSc += 1
    if 'Biography' in row: cntBi += 1
    if 'History' in row: cntHi += 1
    if 'Western' in row: cntWe += 1
    if 'Thriller' in row: cntTh += 1
    if 'Comedy' in row: cntCo += 1
    if 'Romance' in row: cntRo += 1
    if 'Animation' in row: cntAn += 1
    if 'Family' in row: cntFam += 1
    if 'War' in row: cntWa += 1
    if 'Music' in row: cntMu += 1
    if 'Fantasy' in row: cntFan += 1
    if 'Mystery' in row: cntMy += 1
    if 'Horror' in row: cntHo += 1
list_freq = pd.array([cntDr, cntCr, cntAc, cntAd, cntSc, cntBi, cntHi, cntWe, cntTh, cntCo, cntRo, cntAn, cntFam, cntWa, cntMu, cntFan, cntMy, cntHo])        
list_Genre = pd.array(['Drama','Crime','Action','Adventure','Sci-Fi','Biography','History','Western','Thriller',
                       'Comedy','Romance','Animation','Family','War','Music','Fantasy','Mystery','Horror'])
df_Genre = pd.DataFrame({'Film_Genre': list_Genre, 'Frequency': list_freq})

# Show only the top 10 by Frequency
df_Genre.sort_values('Frequency', ascending = False, inplace = True)
df_Genre_top10 = df_Genre[df_Genre['Frequency'] >= 64] # 64 being the 10th highest value, hence everything below is not important
print(df_Genre_top10)

# Generating the bar plot
box = DaV.bar_plot(df_Genre_top10, 'Film_Genre', 'Frequency')