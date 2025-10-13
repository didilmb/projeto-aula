import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página Streamlit (Opcional, mas recomendado)
st.set_page_config(layout="wide")
st.title("Análise de Deputados por UF")

# Carregamento dos dados
# Certifique-se de que a URL está acessível e correta
dataset = pd.read_csv('https://raw.githubusercontent.com/didilmb/projeto-aula/refs/heads/main/deputados_2022%20(1).csv')

# --- Lógica de Contagem e Geração do Gráfico ---

# 1. Contar o número de deputados por UF
# Usando 'uf' como o nome da coluna, conforme você corrigiu.
contagem_uf = dataset['uf'].value_counts().reset_index()
contagem_uf.columns = ['UF', 'Número de Deputados'] # Renomeando para títulos melhores

# 2. Criar o gráfico de barras com Plotly Express
fig = px.bar(
    contagem_uf,
    x='UF',
    y='Número de Deputados',
    title='Número de Deputados por Unidade da Federação (UF)',
    labels={'UF': 'Unidade da Federação', 'Número de Deputados': 'Total de Deputados'},
    color='UF',  # Cores diferentes para cada barra
    template='plotly_white' # Estilo visual mais limpo (opcional)
)

# 3. Exibir o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)

# Opcional: Mostrar a tabela de contagem
st.subheader('Tabela de Contagem')
st.dataframe(contagem_uf, use_container_width=True
