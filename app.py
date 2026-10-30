import streamlit as st
import json

def CarregaDashboard():

    # abre o arquivo json para buscar o link
    with open("links.json", "r", encoding="utf-8") as f:
        links = json.load(f)

    link_ocorrencias_csv = next(
        item["link"] for item in links
        if item["nome"] == "Base CSV"
    )

    # chama a função para carregar o arquivo csv com as ocorrencias
    from LoadOcorrenciasCsv import CarregarOcorrenciasCsv
    df_ocorrencias = CarregarOcorrenciasCsv(link_ocorrencias_csv)

    st.dataframe(df_ocorrencias)

    if st.button("🔄 Atualizar dados"):
        st.cache_data.clear()
        st.toast("Cache limpo com sucesso!", icon="✅")
        st.rerun()
