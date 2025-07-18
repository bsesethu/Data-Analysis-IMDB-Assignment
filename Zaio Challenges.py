import numpy as np
import pandas as pd

# 14/07 Assignment Challenge
arr = np.array([10, 12, 15, 10, 300])
q1 = np.quantile(arr, 0.25)
q3 = np.quantile(arr, 0.75)
IQR = q3 - q1

boo_list = []
for val in arr:
    if val < (q1 - 1.5 * IQR):
        boo = True
        boo_list.append(boo)
    elif val > (q1 + 1.5 * IQR):
        boo = True
        boo_list.append(boo)
    else:
        boo_list.append(False)
    
print(boo_list)
print(q1, q3, IQR)

# Filling missing values
s = pd.Series([1, None, 3, 4])
print('\n')

def meanStuff(s):
    mean_v = np.mean(s)

    count = 0 # Initialize count
    for i in range(len(s)):
        if pd.isna(s[i]):
            count += 1

    if count == len(s):
        return s #NOTE I'm allowed to do this
    else:
        for i in range(len(s)):
            if pd.isna(s[i]):
                s[i] = mean_v
                count += 1
        return s

s = pd.Series([None, None, None, None])
print('\n')
s_stuff = meanStuff(s)
print(s_stuff)


# 15/07
def handle_missing_values():
    data = {
    "OrderID": [1001, 1002, 1003, 1004, 1005],
    "Product": ["Laptop", None, "Office Chair", "Desk", "Microwave"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", None],
    "Customer": ["Alice Smith", "Bob Johnson", "Charlie Lee", None, "Eve Wilson"],
    "Quantity": [2, 1, 5, None, 1],
    "Price": [800, 600, 120, 200, None],
    "Discount": [10, 5, None, 0, 10],
    "Total": [1440, None, 510, 200, 135],
    "Region": ["North", "South", "East", None, "North"],
    "Date": ["2023-01-15", "2023-01-18", "2023-01-20", "2023-02-01", "2023-02-15"]
    }
    count_missing = 0
    df = pd.DataFrame(data)
    for col in df.columns:
        for row in df[col]:
            if pd.isna(row):
                count_missing += 1

    df[['Product', 'Category']] = df[['Product', 'Category']].fillna('Unknown')
    df[['Quantity', 'Price']] = df[['Quantity', 'Price']].fillna(0)
    df[['Discount']] = df[['Discount']].fillna(np.mean(df['Discount']))
    df[['Total']] = df[['Total']].fillna(np.mean(df['Total']))
    df[['Customer', 'Region']] = df[['Customer', 'Region']].fillna('Not Specified')
    
    return df,  count_missing
    

print(handle_missing_values())
# The bitch
def aggregate_and_group():
    df = pd.DataFrame({
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Appliances", "Appliances"],
    "Sales": [1200, 800, 950, 650, 400, 300],
    "Profit": [200, 150, 120, 50, 60, 40]
    })
    # Grouping using for loop
    # for i in range(df.columns):
    #     for j in range(df.shape[0]):
                    
            
    df_new = df.groupby(['Region', 'Category']).agg(TotalSales = ('Sales', 'sum'), AvgProfit = ('Profit', 'mean'))
    # if df_new['TotalSales'] == 1200:
    #     df_new['Region'] = df_new['Region'].replace('', 'North')
    df_new.iloc[2, 0] = 'North'
    # df_new.replace('North', 'Nor', inplace= True)
    return df_new
result = aggregate_and_group()
print(result)

# Q4
{
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Appliances", "Appliances", "Electronics", "Furniture"],
    "Sales": [1200, 800, 950, 650, 400, 300, 1500, 700],
    "Profit": [200, 150, 120, 50, 60, 40, 300, 100]
}
# Creates a pivot table with the following specifications:

# Rows represent the "Region".
# Columns represent the "Category".
# The values are the total "Sales".
# Missing values are filled with 0.
# Returns the resulting pivot table as a DataFrame.
def create_sales_pivot_table():
    data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Appliances", "Appliances", "Electronics", "Furniture"],
    "Sales": [1200, 800, 950, 650, 400, 300, 1500, 700],
    "Profit": [200, 150, 120, 50, 60, 40, 300, 100]
    }
    df = pd.DataFrame(data)
    df_pivot = pd.pivot_table(df, index= 'Region', # Index AKA rows
                                  columns= 'Category',
                                  values= 'Sales',
                                  aggfunc= 'sum')
    df_pivot.fillna(0, inplace= True)
    return df_pivot
res = create_sales_pivot_table()
print(res)


def add_new_column():
    data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
    }
    df = pd.DataFrame(data)
    df['Score'] = [90, 85, 80]
    return df
result = add_new_column()

def set_dataframe_values():
    data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 88]
    }
    df = pd.DataFrame(data)
    df.loc[1, 'Score'] = 95
    df.loc[2, 'Age'] = 40
    return df
result = set_dataframe_values()
print(result)

def concat_two_dataframes():
    df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Alice", "Bob"]
    })
    df2 = pd.DataFrame({
    "ID": [3, 4],
    "Name": ["Charlie", "David"]
    })
    res_row = pd.concat([df1, df2], axis= 0)
    res_col = pd.concat([df1, df2], axis= 1)
    return res_row, res_col
result_rows, result_columns = concat_two_dataframes()

def create_copies_of_dataframe():
    data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 88]
    }
    df = pd.DataFrame(data)
    shallow = df.copy(deep= False)
    deep = df.copy(deep= True)
    shallow.loc[0, 'Score'] = 95
    return (shallow, deep)
tup = create_copies_of_dataframe()
print(tup)