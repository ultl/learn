import pandas as pd

df = pd.read_csv('student.csv')
print(df.shape[0])
print(df.shape[1])
print(df.columns)

df = df.rename(
  columns={
    'famsize': 'family_size',
    'Pstatus': 'parent_status',
    'Medu': 'male_education',
    'Fedu': 'female_education',
    'Mjob': 'male_job',
    'Fjob': 'female_job',
    'schoolsub': 'school_support',
    'famsup': 'family_support',
    'higher': 'higher_education',
    'internet': 'internet_access',
    'famrel': 'family_relationship',
    'freetime': 'free_time',
    'goout': 'go_out',
    'Dalc': 'daily_alcohol',
    'Walc': 'weekend_alcohol',
    'health': 'health_status',
    'G1': 'grade_1',
    'G2': 'grade_2',
    'G3': 'grade_3',
  }
)
df.to_csv('cleaned_student.csv', index=False)
df.to_parquet('food.parquet')
