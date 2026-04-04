import streamlit as st
from src.utils.data_loader import load_stock_data, prepare_melted_data
from src.utils.charts import create_line_chart

def show_nvidia():
    """
    Dashboard dédié à Nvidia (NVDA).
    """
    df = load_stock_data("NVDA")
    if df is not None:
        st.title("Nvidia (NVDA)")
        df_melt = prepare_melted_data(df)
        chart = create_line_chart(df_melt, title="Evolution des prix Open/Close")
        st.altair_chart(chart, use_container_width=True)

        # Widget de test interactif
        st.divider()
        st.subheader("Outils Interactifs")
        x = st.slider("Choisissez une valeur x", min_value=0, max_value=100, key="slider_nvda")
        st.write(f"Résultat : **{x}² = {x * x}**")
    else:
        st.error("Données Nvidia non trouvées.")
