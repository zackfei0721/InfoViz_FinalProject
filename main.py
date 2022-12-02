import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly
# plotly.offline.init_notebook_mode(connected=True)


datafile = 'BigMacPrice.csv'
df = pd.read_csv(datafile)
# print(df)
# print(df.info())

for year in range(2000, 2021):
    df_new = df[df['year'] == year]
    print(df_new)
    fig = px.choropleth(df_new,
                        title="Big Mac Price Over the World",
                        locations="iso_a3",
                        color="dollar_price",
                        scope="world",
                        hover_name="name",
                        animation_frame="year")
    fig.show()

year = 2000
df_2000 = df[df['year'] == 2000]
print(df_2000)

fig = px.choropleth(df_2000,
                    locations="iso_a3",
                    color="dollar_price",
                    scope="world",
                    hover_name="name",
                    animation_frame="year")
fig.show()
# scl = [[0.0, '#ffffff'], [0.2, '#ff9999'], [0.4, '#ff4d4d'],
#       [0.6, '#ff1a1a'], [0.8, '#cc0000'], [1.0, '#4d0000']]
"""
#The slider seems to have some issues when
 running the code outside a ipython notebook so I removed it
 and made it print out all iteration figures instead
slider for each year
data_slider = []
for year in range(2000, 2021):
    df_year = df[df['year'] == year]

    for col in df.columns:
        df[col] = df[col].astype(str)
    data_one_year = dict(
        type='choropleth',
        locations=df['iso_a3'],
        locationmode='ISO-3',
        colorscale=scl,
        text="name",
    )
    data_slider.append(data_one_year)


steps = []

for i in range(len(data_slider)):
    step = dict(method='restyle',
                args=['visible', [False]*len(data_slider)],
                label='Year {}'.format(i+2000))
    step['args'][1][1] = True
    steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

layout = dict(geo=dict(scope='world', sliders=sliders))

# I create the figure object:

fig = dict(data=data_slider, layout=layout)


plotly.offline.iplot(fig)
"""
