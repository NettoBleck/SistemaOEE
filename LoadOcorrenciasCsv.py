import streamlit as st
import pandas as pd
import requests
from io import BytesIO

@st.cache_data(ttl=3600)
def CarregarOcorrenciasCsv(link):
    resposta = requests.get(
        link,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    resposta.raise_for_status()
    return pd.read_csv(BytesIO(resposta.content), sep=",", encoding="utf-8-sig")

"""
url_teste = "https://camilalimentos-my.sharepoint.com/:x:/g/personal/antonio_cneto_camil_com_br/IQCt9d3LMjEhSIC9fPzF-RmpAVaJczDLWfmjQuDI9oXgZgA?e=e14xra&download=1"

dados_teste = CarregarOcorrenciasCsv(url_teste)
st.dataframe(dados_teste)
"""