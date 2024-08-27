import pandas as pd

df = pd.read_csv('insurance.csv')

# code nay sai te le roi nha


def outliers_removal(df):
  q1 = df.quantile(0.25)
  q3 = df.quantile(0.75)
  iqr = q3 - q1
  lower_bound = q1 - 1.5 * iqr
  upper_bound = q3 + 1.5 * iqr
  return df[(df > upper_bound) | (df < lower_bound)]


df['charges'] = outliers_removal(df['charges'])
df['bmi'] = outliers_removal(df['bmi'])
df['age'] = outliers_removal(df['age'])


# def remove_outliers(df, column):
#   df_mean = df[column].mean()
#   df_std = df[column].std()
#   lower, upper = df_mean - 3 * df_std, df_mean + 3 * df_std
#   return df[(df[column] > lower) & (df[column] < upper)]


# df['bmi'] = remove_outliers(df, 'bmi')
# df['charges'] = remove_outliers(df, 'charges')
# df['age'] = remove_outliers(df, 'age')

# df.to_csv('insurance_cleaned.csv', index=False)
