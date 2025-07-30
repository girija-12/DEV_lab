import plotly.express as px
import pandas as pd
import numpy as np
import webbrowser
import os

countries = ['IND', 'CHN', 'JPN', 'RUS', 'SAU', 'IRN', 'IDN', 'PAK', 'KAZ', 'TUR']
data = {
    'country': countries,
    'pop_growth_%': np.random.uniform(0, 5, len(countries)),
    'gdp': np.random.randint(1000, 1000000, len(countries)),
    'population': np.random.randint(10_000_000, 1_400_000_000, len(countries))
}
df = pd.DataFrame(data)

fig = px.choropleth(
    df,
    locations='country',
    color='pop_growth_%',
    hover_name='country',
    hover_data={
        'pop_growth_%': ':.2f',
        'gdp': True,
        'population': True
    },
    locationmode='ISO-3',
    color_continuous_scale='Plasma',
    title='Population Growth % by Country (Sample Data)'
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    hoverlabel=dict(bgcolor="white", font_size=12)
)

html_file = "population_growth_map.html"
fig.write_html(html_file)
print(f"Map saved to {html_file}")

webbrowser.open('file://' + os.path.realpath(html_file))