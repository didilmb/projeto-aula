import pandas as pd
import streamlit as st
import plotly.express as px
dataset=pd.read_csv('https://raw.githubusercontent.com/didilmb/projeto-aula/refs/heads/main/deputados_2022%20(1).csv')
# Contar o número de deputados por UF
contagem_uf = dataset['sgUF'].value_counts().reset_index()
contagem_uf.columns = ['UF', 'Número de Deputados']

# Criar o gráfico de barras com Plotly Express
fig = px.bar(
    contagem_uf,
    x='UF',
    y='Número de Deputados',
    title='Número de Deputados por Unidade da Federação (UF)',
    labels={'UF': 'Unidade da Federação', 'Número de Deputados': 'Total de Deputados'},
    color='UF'  # Opcional: para dar cores diferentes a cada barra
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)

# Opcional: Mostrar a tabela de contagem
st.subheader('Tabela de Contagem por UF')
st.dataframe(contagem_uf)
