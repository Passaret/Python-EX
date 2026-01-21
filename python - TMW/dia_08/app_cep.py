import streamlit as st
import requests
import pandas as pd

st.title("Busca CEP")

cep = st.text_input("Busque seu cep")

URL = "https://viacep.com.br/ws/{cep}/json"


if cep != "":
    try:
        resp = requests.get(URL.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data)
    except Exception as err:
        st.error("Entre com um cep válido!")