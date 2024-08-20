import pandas as pd
import streamlit as st

valor = st.number_input('Valor', value=1000)
prestacoes = st.number_input('Prestações', value=12)
juros = st.text_input('Juros (A.M)', value='1.0%')

juros = float(juros.replace('%', '').replace(',', '.'))

prestacao = 0

with st.sidebar:
    if st.button(
        "Limpar 🧹",
        use_container_width=True,
    ):
        prestacao = 0

    if st.button(
        "Calcular 💰",
        use_container_width=True,
    ):
        juros_total = (1 + juros/100) ** prestacoes
        prestacao = valor * juros_total / prestacoes


    st.divider()

st.write(f"O valor da prestação é de R$ {prestacao:.2f}")
st.write(f"O valor total é de R$ {prestacao * prestacoes:.2f}")
