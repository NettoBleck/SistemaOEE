import streamlit as st

def CarregaDashboard(links):
    # busca no dicionario o link das ocorrencias csv
    link_ocorrencias_csv = next(item for item in links if item["nome"] == "Base CSV")

    # chama a função para carregar o arquivo csv com as ocorrencias
    from LoadOcorrenciasCsv import CarregarOcorrenciasCsv
    df_ocorrencias = CarregarOcorrenciasCsv(link_ocorrencias_csv["link"])

    st.dataframe(df_ocorrencias)

    if st.button("🔄 Atualizar dados"):
        st.cache_data.clear()
        st.toast("Cache limpo com sucesso!", icon="✅")
        st.rerun()

