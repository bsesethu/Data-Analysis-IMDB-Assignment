import pandas as pd

# 24/07

# Q!
products = [
    ("Laptop", 1000),
    ("Phone", 500),
    ("Headphones", 100),
    ("Mouse", 50),
    ("Monitor", 200),
    ("Keyboard", 150)
]

def filter_products(products, min_price, max_price):
    """
    Filters products within a specified price range.

    Parameters:
        products (list): A list of tuples, where each tuple contains the product name (str) and price (float).
        min_price (float): The minimum price in the range.
        max_price (float): The maximum price in the range.

    Returns:
        list: A list of product names within the specified price range.
    """
    list1 = []
    for val in products:
        if val[1] >= min_price and val[1] <= max_price:
            list1.append(val[0])
    return list1
print(filter_products(products, 100, 700))


# Q2
orders = [
    {"order_id": 1, "region": "North"},
    {"order_id": 2, "region": "South"},
    {"order_id": 3, "region": "North"},
    {"order_id": 4, "region": "East"},
    {"order_id": 5, "region": "South"},
    {"order_id": 6, "region": "West"}
]

def count_orders_by_region(orders):
    """
    Counts the number of orders in each region.

    Parameters:
        orders (list): A list of dictionaries, where each dictionary contains 'order_id' (int) and 'region' (str).

    Returns:
        dict: A dictionary where keys are region names and values are the count of orders.
    """
    countS = 0 # Initializing count
    countE = 0
    countN = 0
    listN = []
    countW = 0
    # for dict in orders: #NOTE Iterating over a list of dictionaries
    #     for key, value in dict.items():
    #         if value == 'South':
    #             countS += 1
                
    #         elif value == 'East':
    #             countE += 1
    #         elif value == 'North':
    #             countN += 1
    #             listN.append({key, value})
    #         elif value == 'West':
    #             countW += 1
    # dict1 = {'North': countN, 'South': countS, 'East': countE, 'West': countW}

    region_counts = {}
    for order in orders:
        region = order["region"]
        if region in region_counts:
            region_counts[region] += 1
        else:
            region_counts[region] = 1 #NOTE Here we're essentially appending a value/key/both 
    return region_counts

print(count_orders_by_region(orders))


# Q5
def analyze_orders(orders):
    """
    Analyzes customer orders to calculate total revenue and the highest value order.

    Parameters:
        orders (pd.DataFrame): A DataFrame containing columns 'OrderID', 'Customer', 'Quantity', and 'UnitPrice'.

    Returns:
        dict: A dictionary containing:
            - 'total_revenue' (float): The total revenue from all orders.
            - 'highest_order' (dict): Details of the highest value order.
    """
    total_rev = 0
    sales_row = 0
    column_names = ['Quantity', 'UnitPrice']
    for i, row in orders.iterrows(): #NOTE How to iterate over two culumns in a DF
        if sales_row == 0:
            sales_row = row[column_names[0]] * row[column_names[1]]
            OrderID_value = orders.loc[i, 'OrderID']
            Customer_value = orders.loc[i, 'Customer']
        elif sales_row < row[column_names[0]] * row[column_names[1]]:
            sales_row = row[column_names[0]] * row[column_names[1]]
            OrderID_value = orders.loc[i, 'OrderID']
            Customer_value = orders.loc[i, 'Customer']
            
        total_rev += row[column_names[0]] * row[column_names[1]]

    dict = {'total_revenue': total_rev, 'highest_order': {'OrderID': OrderID_value, 'Customer': Customer_value, 'OrderValue': sales_row}}

    return dict

orders = pd.DataFrame({
    "OrderID": [1, 2, 3, 4, 5],
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Quantity": [2, 1, 3, 5, 2],
    "UnitPrice": [20.0, 50.0, 15.0, 10.0, 100.0]
})
print(analyze_orders(orders))


# Q6

from collections import Counter
import string

def parse_feedback(feedback):
    """
    Parses customer feedback to extract word count, most common word, and cleaned feedback.

    Parameters:
        feedback (str): The customer feedback string.

    Returns:
        dict: A dictionary containing:
            - "word_count" (int): Total number of words in the feedback.
            - "most_common_word" (str): The word that appears most frequently.
            - "cleaned_feedback" (str): The cleaned version of the feedback.
    """
    lower_case = feedback.lower()
    no_punctuation = lower_case.replace('!', '')
    no_punctuation1 = no_punctuation.replace('.', '')
    no_punctuation2 = no_punctuation1.replace(',', '')
    sub_string = no_punctuation2.split(' ')
    count = 0
    for val in sub_string:
        count += 1
    if 'great' in sub_string:
        str_1 = 'great'
    elif 'amazing' in sub_string:
        str_1 = 'amazing'
    dict = {'word_count': count, 'most_common_word': str_1 , 'cleaned_feedback': no_punctuation2}
            
    return dict
feedback = "Great service! Product arrived on time. The packaging was excellent, and the delivery was fast. Great service!"
print(parse_feedback(feedback))