import pandas as pd
from plotly.express import bar, line, scatter
from streamlit import plotly_chart as plot

df = pd.read_csv('clean_time.csv')

top_100 = df.iloc[:100, :]
plot(
  line(
    top_100,
    x='world_rank',
    y='citations',
    title='Citation and Teaching vs World Rank of Top 100 Universities',
  )
)

plot(
  bar(
    df[df.year == 2016].iloc[:10, :],
    x='citations',
    y='university_name',
  ),
  title='Citations for Universities in 2016',
)
plot(
  bar(
    df[df.year == 2016].iloc[:10, :],
    x='income',
    y='university_name',
  ),
  title='Income for Universities in 2016',
)
plot(
  scatter(
    df[df.year == 2016],
    x='research',
    y='international',
    color='university_name',
    title='Research vs International vs Total Score for Universities in 2016',
  )
)
