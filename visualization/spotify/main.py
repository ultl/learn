from re import sub

import pandas as pd
from plotly.express import line
from streamlit import plotly_chart, set_page_config

df = pd.read_csv('spotify.csv')

set_page_config(layout='wide')


def to_snakecase(s):
  return (
    '_'.join(
      sub('([A-Z][a-z]+)', r' \1', sub('([A-Z]+)', r' \1', s.replace('-', ' '))).split(),
    )
    .lower()
    .replace('.', '')
  )


df.columns = [to_snakecase(col) for col in df.columns]

# Create the chart with plotly_express
plotly_chart(
  line(
    df,
    x='date',
    y=['shape_of_you', 'despacito', 'something_just_like_this', 'humble'],
    title='Spotify Streams',
    labels={'value': 'Streams', 'date': 'Date'},
    line_shape='spline',
  )
)
# Plot a subset of data
