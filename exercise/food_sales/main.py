import pandas as pd

df = pd.read_csv('clean_food_sales.csv')

'rows', df.shape[0]
'columns', df.shape[1]
'column names', df.columns.to_list()
'describe',df.describe()

# the most ordered item in the chipotle dataset based on item name:
most_ordered = df.groupby('item_name').sum().sort_values(['quantity'], ascending=False).head(1)

# the most ordered item based on choice description:
highest_choice = (
  df.groupby('choice_description').sum().sort_values(['quantity'], ascending=False).head(1)
)

# the number of items in total:
items = df.quantity.sum()

# change the type of item price using lambda function:
df['item_price'] = df.item_price.apply(lambda x: float(x[1:]))

# the revenue for the period in the dataset:
# chipotle['item_price'] = chipotle['item price']
revenue = (df['quantity'] * df['item_price']).sum()

# the average revenue amount per order:
df.insert(5, 'revenue', df['quantity'] * df['item_price'], True)

# products cost more than $10.00
required_products = df[df['item_price'] > 10.00]

# the price of each item
new_df = (
  df[['item_name', 'item_price']].drop_duplicates().sort_values('item_price', ascending=False)
)
# Sort by the name of the item
sorted_df = df.sort_values('item_name').drop_duplicates()

# the quantity of the most expensive item ordered
expensive_items = df.quantity[df.item_price.sort_values(ascending=False).head(1).index]

# How many times was a Veggie Salad Bowl ordered?
veggie = df.item_name[df.item_name.str.contains('Veggie Salad Bowl')].count()

# How many times did someone order more than one Canned Soda?
soda = df[df.item_name == 'Canned Soda']
over_one_soda = soda[soda.quantity > 1].count()

# Data cleaning and transformation
"order_id => nominal"
"price => float"