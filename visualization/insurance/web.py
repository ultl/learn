import pandas as pd
from plotly.express import box, scatter, violin
from streamlit import header, set_page_config
from streamlit import plotly_chart as plot

set_page_config(layout='wide')

df = pd.read_csv('insurance.csv')
cleaned_df = pd.read_csv('insurance_clean.csv')

header('raw')

plot(
  scatter(
    df,
    x='bmi',
    y='charges',
    color='region',
    marginal_x='histogram',
    marginal_y='box',
    trendline='ols',
    height=800,
  )
)
plot(
  scatter(
    df,
    x='bmi',
    y='charges',
    color='smoker',
    trendline='ols',
  )
)
plot(
  violin(
    df,
    x='region',
    y='charges',
    color='region',
  )
)
plot(
  box(
    df,
    x='region',
    y='charges',
    color='region',
  )
)

header('cleaned')
plot(
  box(
    cleaned_df,
    x='region',
    y='charges',
    color='region',
  )
)
