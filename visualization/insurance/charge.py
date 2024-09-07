import pandas as pd
import statsmodels.api as sm
from plotly.express import box, pie, scatter
from plotly.express import histogram as hist
from plotly.express import imshow as heat
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from streamlit import set_page_config

set_page_config(layout='wide')

raw = pd.read_csv('insurance.csv')
trial = pd.read_csv('insurance.csv')
'# Raw Data'
'## raw', raw.describe()
raw
(
  box(raw, x='sex', y='charges', color='sex'),
  hist(raw, x='charges', color='region', facet_col='sex'),
)

'# Transform'


def to_equal_chunk(series, chunk):
  # Calculate the bin edges
  bins = list(range(0, series.max() + chunk + 1, chunk))

  # Adjust labels to match the new bins
  labels = [f'{bins[i]}-{bins[i+1]}' for i in range(len(bins) - 1)]
  # len(bins) - 1 because the number of labels is one less than the number of bins
  return pd.cut(series, bins=bins, labels=labels, right=False)


trial['age'] = to_equal_chunk(raw['age'], 10)
'Age groups', trial

(
  '',
  pie(
    trial,
    values='charges',
    names='age',
    title='Charges by age',
    width=1000,
  ),
)

'', hist(raw, x='bmi', color='region', facet_col='sex')


def to_number(series):
  midpoints = []
  for i in series:
    i = i.split('-')
    i = int(i[0]) + (int(i[1]) - int(i[0])) / 2
    midpoints.append(i)
  return pd.Series(midpoints)


trial['age'] = to_number(trial['age'])
(
  '',
  heat(
    trial[['age', 'bmi', 'children', 'charges']].corr(),
    title='Correlation Heatmap',
    color_continuous_scale='Viridis',
  ),
)

'# Analysis: one-way ANOVA'
trial['age'], trial['charges'] = trial['age'].astype(int), trial['charges'].astype(int)
(
  'anova one way: charges by age',
  f_oneway(trial['charges'], trial['age']),
)

'# Analysis: two-way ANOVA'
(
  'two-way anova: charges by age and bmi',
  sm.stats.anova_lm(ols('charges ~ age + bmi', data=trial).fit()),
)


def bmi_categories(bmi):
  if bmi < 18.5:
    return 'Underweight'
  elif 18.5 <= bmi < 25:
    return 'Normal'
  elif 25 <= bmi < 30:
    return 'Overweight'
  else:
    return 'Obese'


raw['bmi'] = raw['bmi'].apply(bmi_categories)

'# Weight Status vs Charges'
(
  scatter(
    raw,
    x='age',
    y='charges',
    color='bmi',
    title='Weight Status vs Charges',
    height=800,
    width=1000,
  ),
)
