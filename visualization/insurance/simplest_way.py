import pandas as pd
from plotly.express import box, scatter, violin
from streamlit import set_page_config

set_page_config(layout='wide')


raw = pd.read_csv('insurance.csv')
clean = pd.read_csv('insurance_clean.csv')


'# raw'
raw
(
  box(raw, x='sex', y='charges', color = 'sex'),
  scatter(raw, x='bmi', y='charges', color = 'region', trendline='ols'),
  violin(raw, x='region', y='charges'),
  box(raw, x='bmi', y='region')
)

'# clean'
clean
(
  box(clean, x='sex', y='charges'),
  scatter(clean, x='bmi', y='charges'),
  violin(clean, x='region', y='charges'),
)
