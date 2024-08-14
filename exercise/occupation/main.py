import numpy as np
import pandas as pd

df = pd.read_csv('occupation.txt')
# the mean age per occupation
occupation = df[['occupation', 'age']].groupby('occupation').mean().round(2)

# For each occupation, calculate the minimum and maximum ages
analysis = df.groupby('occupation').agg({'age': ['min', 'max', 'count', 'sum', 'mean']})


# The Male ratio per occupation and sort it from the most to the least
gender_separated = pd.crosstab(df.occupation, df.gender)

male_ratio = (gender_separated['M'] / gender_separated.sum(axis=1) * 100).sort_values(
  ascending=False
)

# each occupation, age, gender, mean
age_mean = df.groupby(['occupation', 'gender']).age.mean()

# each occupation, the percentage of woman and men
gender_separated['total'] = gender_separated['F'] + gender_separated['M']
gender_separated['male percentage'] = gender_separated['M'] / gender_separated['total'] * 100
gender_separated['female percentage'] = 100 - gender_separated['male percentage']

# create a new column "potential"
potential = np.zeros(943).reshape(943, 1)
df['potential'] = potential

# del df['potential']
df['gender'].value_counts()

# the first occurrence of each occupation
df.occupation.idxmax()
