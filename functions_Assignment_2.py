import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

    # Check for missing values
class Data_Collection:
    def check_missing(df): # From Assignment 1
        df_check = df.isna()
        count1 = 0 # To count the number of missing and non missing values
        count2 = 0
        for col in df_check.columns:
            for row in df_check[col]:
                if row == True: # Returns a missing value
                    count1 += 1
                    # print(row, col) # Shows where the None values are. NOTE They are in the 'parental_education_level'
                else:
                    count2 += 1# Returns a non missing value
        print('Number of missing values', count1)
        print('Total number of values in the table', count1 + count2)

        missing_percentage = 100.0 * count1 / (count1 + count2)
        print(f'Proportion of missing data to the total: {round(missing_percentage, 2)}% of data is missing.') # percentage is well below 1%, Unlikely to have a major impact on overall findings
        # print(df.isna()) # Returns missing values as true

    # (Function) Remove rows with critical missing data, critical data column specified
    def remove_rows(df, column): 
        for i, row in df.iterrows():
            if pd.isna(row[column]): # How to equate to None/NaN in pandas. Pandas has no None, it's NaN in pandas
                # print(1)
                df.drop(index= i, inplace= True) #NOTE Inplace = True changes the DF
        return df

    # (Function) Remove duplicates
    def dropDuplicates(df):
        df_noDuplicates = df.drop_duplicates() # Removes any row that is a duplicate of any other, leaving only the first occurance
        return df_noDuplicates

class Data_Preperation:
    # (Funtion) Creating a new 'Relesed_Decade' column from the 'Released_Year' column
    def newColumn_ReleasedDecade(df):
        # Convert 'Released_Year' from string to int
        df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors= 'coerce') # 'coerce' to make errors encountered NaN
        df['Released_Year'] = df['Released_Year'].fillna(0)
        df['Released_Year'] = df['Released_Year'].astype(int)
        # Extract Decade from Released_Year
        list1 = []
        for row in df['Released_Year']:
            if row == 0:
                list1.append('0')
            elif row >= 1920 and row < 1930:
                list1.append('1920s')
            elif row >= 1930 and row < 1940:
                list1.append('1930s')
            elif row >= 1940 and row < 1950:
                list1.append('1940s')
            elif row >= 1950 and row < 1960:
                list1.append('1950s')
            elif row >= 1960 and row < 1970:
                list1.append('1960s')
            elif row >= 1970 and row < 1980:
                list1.append('1970s')
            elif row >= 1980 and row < 1990:
                list1.append('1980s')
            elif row >= 1990 and row < 2000:
                list1.append('1990s')
            elif row >= 2000 and row < 2010:
                list1.append('2000s')
            elif row >= 2010 and row < 2020:
                list1.append('2010s')
            elif row >= 2020 and row < 2030:
                list1.append('2020s')
        df_col = pd.DataFrame({'Released_Decade': list1})
        df_res = pd.concat([df, df_col], axis= 1) # Concat the decade column to the main DF
        return df_res
                    
class Data_Visualisation:
    # (Function) Create a histogram of column_1 vs column_2 of a dataframe
    def histogram(df, column1, column2, num_of_bins): # specify these characteristics of your histogram
        df_col1 = df[column1]
        df_col2 = df[column2]
        title1 = 'Histogram of ' + column1
        title2 = 'Histogram of ' + column2
        
        fig, axes = plt.subplots(1, 2, figsize=(10, 4)) # 1 row, 2 columns of subplots

        axes[0].hist(df_col1, bins= num_of_bins, color= 'skyblue', edgecolor= 'black')
        axes[0].set_title(title1)
        axes[0].set_xlabel('Adjusted ' + column1)
        axes[0].set_ylabel('Frequency')
        
        axes[1].hist(df_col2, bins= num_of_bins, color= 'red', edgecolor= 'black')
        axes[1].set_title(title2)
        axes[1].set_xlabel(column2)
        axes[1].set_ylabel('Frequency')

        plt.grid(True)
        plt.show()
    
    # (Function) Creating a box plot using DF and column name
    def bar_plot(df, x_column, y_column):
        plt.bar(df[x_column], df[y_column], color= 'orange')
        # ax = sns.countplot(x="Column", data=ds)

        # ax.set_xticklabels(ax.get_xticklabels(), fontsize=7)  
        
        plt.xlabel(x_column, fontsize= 5)
        plt.ylabel('Frequency')
        plt.title('Box plot of ' + x_column + 'frequency')
        
        plt.tight_layout()
        plt.show()