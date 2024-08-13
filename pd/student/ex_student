import pandas as pd

df = pd.read_csv('student.csv')
df.shape[0]
df.shape[1]
df.columns.to_list()  # ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']
# for the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
dt = df.loc[:, 'school':'guardian']  # df.iloc[:, 0:12]


# create function that will capitalize strings
def capitalizer(x):
  return x.str.capitalize()


dt['Mjob'] = capitalizer(dt.Mjob)
dt['Fjob'] = capitalizer(dt.Fjob)
print(dt)


#  Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(x):
  if x > 17:
    return True
  else:
    return False


dt['legal drinker'] = dt.age.apply(majority)
print(dt)
