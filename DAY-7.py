import pandas as pd

# Load the data
sales_data = pd.read_csv("D:\AD files\Day_7_sales_data.csv")

# Display the first 5 rows of the dataset
print(sales_data.head())

# Print basic statistics of the numerical columns
print(sales_data.describe())


# Assuming there's a 'Region' and 'Sales' column in your dataset
total_sales_by_region = sales_data.groupby('Region')['Sales'].sum()
print(total_sales_by_region)


# Assuming there's a 'Product' and 'Quantity' column in your dataset
most_sold_product = sales_data.groupby('Product')['Quantity'].sum().idxmax()
print(f"The most sold product is: {most_sold_product}")


# Assuming there's a 'Product', 'Profit', and 'Sales' column in your dataset
sales_data['Profit_Margin'] = (sales_data['Profit'] / sales_data['Sales']) * 100
average_profit_margin_by_product = sales_data.groupby('Product')['Profit_Margin'].mean()
print(average_profit_margin_by_product)
