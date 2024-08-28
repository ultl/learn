import pandas as pd

raw = pd.read_csv('raw_food.tsv', sep='\t')

'Data before cleaning', raw.describe()


def to_string(df, column):
  df[column] = df[column].astype(str).str.zfill(3)
  return df


'Convert order_id values to string', to_string(raw, 'order_id')

raw = raw.dropna()
'Drop null', raw.dropna()


def to_float(df, column):
  df[column] = df[column].str.replace('$', '').astype(float).round(2)
  return df


'Convert price values to float', to_float(raw, 'item_price')

'Data after cleaning', raw.describe()
