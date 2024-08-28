import pandas as pd
from plotly.express import box, pie
from plotly.express import histogram as hist
from streamlit import set_page_config

set_page_config(layout='wide')

raw = pd.read_csv('insurance.csv')
clean = pd.read_csv('insurance_clean.csv')

'# raw'
raw
(
    box(raw, x='sex', y='charges', color = 'sex'),
    hist(raw, x='charges',color = 'region', facet_col = 'sex'),
    pie(raw, names='age', values='charges')
)

