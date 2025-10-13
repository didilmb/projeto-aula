import pandas as pd
dataset=pd.read_csv('https://www.irdx.com.br/media/uploads/paises.csv')
dataset
import plotly.express as px
fig = px.choropleth(dataset,
                    locations=dataset['iso3'],
                    color=dataset['name'],
                    hover_name=dataset['name'])
fig.update_layout(title='Mapa Coroplético dos Países',
                  geo_scope='world')
fig.show()
import plotly.express as px
fig = px.scatter_geo(dataset,
                     lat=dataset['latitute'],
                     lon=dataset['longitude'],
                     hover_name=dataset['nome'])
fig.update_layout(title='Coordenadas dos Países no Mapa',
                  geo_scope='world')
fig.show()
st.dataframe(dataset)
