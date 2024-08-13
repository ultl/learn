import pandas as pd
from streamlit import dataframe, title

title('')
df = pd.read_csv('population.csv')
dataframe(df)
