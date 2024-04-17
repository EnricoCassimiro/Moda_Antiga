import streamlit as st
import pandas as pd
import numpy as np



st.header('Gráfico de linhas')
st.write('Loja de roupas femininas!')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.title('st.file_uploader')

