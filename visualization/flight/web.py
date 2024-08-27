import pandas as pd
from plotly.express import bar
from plotly.express import imshow as heapmap
from streamlit import plotly_chart as plot

df = pd.read_csv('flight_delays.csv')

plot(
  bar(
    df,
    x='Month',
    y='NK',
    title='Average Arrival Delay for Spirit Airlines Flights, by Month',
    color='Month',
    color_continuous_scale='RdBu_r',
  )
)

plot(
  heapmap(
    df,
    color_continuous_scale='Viridis',
    title='Average Arrival Delay for Each Airline by Month',
    text_auto=True,
  )
)
