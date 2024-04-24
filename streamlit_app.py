import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
###################################################

###################################################
st.header('LOJA MODA ANTIGA')
st.write('Loja de roupas femininas!')
st.warning('Atenção: O site está em manutenção. Algumas funcionalidades podem ficar temporariamente indisponíveis.', icon="⚠️")
st.title('Bem-vindo à fase de teste!')
st.write('Este site está atualmente em fase de teste. Agradecemos sua paciência enquanto trabalhamos para melhorá-lo.')
###################################################
with st.container():
    st.write("---")
###################################################
data = pd.read_csv('Trabalho - Estoque - Blusa.csv')

# Gráfico de estoque por nome de roupa
def plot_stock_chart(data):
    plt.figure(figsize=(15, 8))
    plt.bar(data['Nome'], data['Estoque'], color='skyblue')
    plt.title('Estoque de Roupas por Nome')
    plt.xlabel('Nome da Roupa')
    plt.ylabel('Estoque')
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    st.pyplot()

# Interface do Streamlit
st.title('Análise de Estoque de Roupas')

# Mostrar o gráfico de estoque por nome de roupa
plot_stock_chart(data)
###################################################

###################################################
#COLOCAR UM GRFICO AQUI
###################################################

###################################################
with st.container():
    st.write("---")
###################################################
#COLOCAR UM GRAFICO AQUI
###################################################
with st.container():
    st.write("---")
###################################################
st.sidebar.warning ('Atenção: O site está em manutenção. Algumas funcionalidades podem estar temporariamente indisponíveis.')
###################################################

###################################################
# Carregar os dados do CSV
@st.cache
def load_data():
    df = pd.read_csv('Trabalho - Estoque - Blusa.csv')
    return df

df = load_data()

# Criar o gráfico interativo
st.title('Gráfico Interativo a partir de um CSV')
chart_type = st.selectbox('Selecione o tipo de gráfico:', ['Gráfico de Linhas', 'Gráfico de Barras'])

if chart_type == 'Gráfico de Linhas':
    chart = alt.Chart(df).mark_line().encode(
        x='DESCRIÇÃO',
        y='ESTOQUE'
    ).interactive()
else:
    chart = alt.Chart(df).mark_bar().encode(
        x='DESCRIÇÃO',
        y='ESTOQUE'
    ).interactive()

st.altair_chart(chart, use_container_width=True)
###################################################

###################################################
with st.container():
    st.write("---")
###################################################

###################################################
#COLOCAR ALGUMA COISA AQUI
###################################################
