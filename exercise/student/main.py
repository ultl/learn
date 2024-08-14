import pandas as pd

df = pd.read_csv('cleaned_student.csv')
df.shape[0]
df.shape[1]
df.columns.to_list()

# for the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
dt = df.loc[:, 'school':'guardian']  # df.iloc[:, 0:12]


# create function that will capitalize strings
def capitalizer(x):
  return x.str.capitalize()


#  Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def maturity(x):
  return True if x > 17 else False


dt['legal_drinker'] = dt.age.apply(maturity)
print(dt)
