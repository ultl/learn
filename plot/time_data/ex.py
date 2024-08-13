import pandas as pd
from plotly.graph_objects import (
  Bar,
  Box,
  Figure,
  Layout,
  Pie,
  Scatter,
  Scatter3d,
  Splom,
)
from streamlit import plotly_chart

df = pd.read_csv('time_data_analyzed.csv')
top_100 = df.iloc[:100, :]

citation_scatter = Scatter(
  x=top_100['world_rank'],
  y=top_100['citations'],
  name='citations',
  text='university_name ',
  line=dict(color='firebrick', width=2),
)
teaching_scatter = Scatter(
  x=top_100['world_rank'],
  y=top_100['teaching'],
  name='teaching',
  text=top_100.university_name,
  line=dict(color='gold', width=4),
)
plotly_chart(
  figure_or_data=dict(
    data=[citation_scatter, teaching_scatter],
    layout=dict(
      title='Citation and Teaching vs World Rank of Top 100 Universities',
      xaxis=dict(
        title='World Rank',
      ),
    ),
  )
)
# Horizontal bar chart: Citations vs Income for Universities
citation_bar = Bar(
  x=df[df.year == 2016].iloc[:10, :].citations,
  y=df[df.year == 2016].iloc[:10, :].university_name,
  name='Citations',
  marker=dict(color='rgba(171, 50, 96, 0.6)', line=dict(color='rgba(171, 50, 96, 1.0)', width=1)),
  orientation='h',
)
income_bar = Bar(
  x=df[df.year == 2016].iloc[:10, :].income,
  y=df[df.year == 2016].iloc[:10, :].university_name,
  name='Income',
  marker=dict(color='rgba(0.6, 50, 96, 1716)', line=dict(color='rgba(171, 50, 96, 1.0)', width=1)),
  orientation='h',
)


plotly_chart(
  figure_or_data=dict(
    data=[citation_bar, income_bar],
    layout=Layout(
      title='Citations vs Income for Universities in 2016',
      yaxis=dict(title='Universities'),
      bargap=0.15,
      legend=dict(x=1, y=1, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
    ),
  )
)

# Pie chart: Students rated top 10 universities in 2016
university_top10 = df[df.year == 2016].iloc[:10, :].university_name.tolist()
students_top10 = df[df.year == 2016].iloc[:10, :].num_students.tolist()
students_top10 = [int(i.replace(',', '')) for i in students_top10]
plotly_chart(figure_or_data=dict(data=[Pie(labels=university_top10, values=students_top10)]))

# Box plot: total score vs research in 2016
trace_total_score = Box(
  y=df[df.year == 2016].total_score,
  name='The total score of universities in 2016',
)
trace_research = Box(
  y=df[df.year == 2016].research,
  name='Research of universities in 2016',
)
plotly_chart(figure_or_data=dict(data=[trace_total_score, trace_research]))


# Scatter plot matrix: research, international, and total score in 2015
def mixed_scatter(time_data):
  fig = Figure(
    data=Splom(
      dimensions=[
        dict(label='research', values=time_data['research'].to_list()),
        dict(label='international', values=time_data['international'].to_list()),
        dict(label='total_score', values=time_data['total_score'].to_list()),
      ],
    )
  )
  return fig


plotly_chart(mixed_scatter(df[df.year == 2015]))

# 3D scatter plot:
scatter_3d = Scatter3d(
  x=df[df.year == 2016].research,
  y=df[df.year == 2016].international,
  z=df[df.year == 2016].total_score,
  mode='markers',
  marker=dict(
    size=10,
    color='rgb(255,0,0)',
  ),
)
plotly_chart(figure_or_data=dict(data=[scatter_3d]))
