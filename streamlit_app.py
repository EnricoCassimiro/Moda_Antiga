import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
###################################################
# Conteúdo da página de teste
def test_page():
    st.title('Bem-vindo à fase de teste!')
    st.write('Este site está atualmente em fase de teste. Agradecemos sua paciência enquanto trabalhamos para melhorá-lo.')
    st.write('Por favor, compartilhe quaisquer feedbacks ou sugestões conosco.')
###################################################
st.header('Gráfico de vendas.')
st.write('MODA ANTIGA - Loja de roupas femininas!')
###################################################
with st.container():
    st.write("---")
###################################################
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Tops', 'Calças', 'Blusas'])

st.line_chart(chart_data)
###################################################
# Crie um dataframe de exemplo estoque das roupas
data = pd.DataFrame({
  'Estoque': ['Tops', 'Calças', 'Blusas', 'Cropped', 'Shorts'],
  'Quantidade': [25, 35, 45, 55, 44]
})
 
# Crie um gráfico de barras
st.bar_chart(data)
###################################################
with st.container():
    st.write("---")
###################################################
    # Função para plotar o gráfico de barras
def plot_stock_chart(data):
    fig, ax = plt.subplots()
    ax.bar(data['Produto'], data['Estoque'], color='skyblue')
    ax.set_xlabel('Produto')
    ax.set_ylabel('Estoque')
    ax.set_title('Estoque de Roupas')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

# Página 1
def page1(data):
    st.title('Página 1')
    st.write('Este é o conteúdo da página 1:')
    st.write(data.head())  # Exemplo de exibição dos primeiros 5 registros do DataFrame

# Página 2
def page2(data):
    st.title('Página 2')
    st.write('Este é o conteúdo da página 2:')
    st.write(data.describe())  # Exemplo de exibição de estatísticas descritivas do DataFrame

# Página 3
def page3(data):
    st.title('Página 3')
    st.write('Este é o conteúdo da página 3:')
    plot_stock_chart(data)  # Exemplo de plotagem do gráfico de estoque de roupas

# Interface do Streamlit
st.sidebar.title('Menu de Navegação')
page = st.sidebar.radio('Escolha uma página:', ['Página 1', 'Página 2', 'Página 3'])

# Carregar os dados do arquivo CSV
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo CSV", type=['csv'])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = None

# Navegação entre páginas
if page == 'Página 1':
    if data is not None:
        page1(data)
    else:
        st.write('Por favor, faça o upload de um arquivo CSV.')
elif page == 'Página 2':
    if data is not None:
        page2(data)
    else:
        st.write('Por favor, faça o upload de um arquivo CSV.')
else:
    if data is not None:
        page3(data)
    else:
        st.write('Por favor, faça o upload de um arquivo CSV.')
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
        x='ESTOQUE',
        y='DESCRIÇÃO'
    ).interactive()
else:
    chart = alt.Chart(df).mark_bar().encode(
        x='ESTOQUE',
        y='DESCRIÇÃO'
    ).interactive()

st.altair_chart(chart, use_container_width=True)