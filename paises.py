import pandas as pd
import streamlit as st
import ploty.express as px
dataset=pd.read_csv('https://www.irdx.com.br/media/uploads/paises.csv')
st.dataframe(dataset)
fig = px.choropleth(dataset,
                    locations=dataset['iso3'],
                    color=dataset['name'],
                    hover_name=dataset['name'])
fig.update_layout(title='Mapa Coroplético dos Países', geo_scope='world')
st.plotly_chart(fig, use_container_width=True, theme="streamlit")
