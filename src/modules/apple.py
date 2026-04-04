import streamlit as st
from src.utils.data_loader import load_stock_data, prepare_melted_data
from src.utils.charts import create_bar_chart

def show_apple():
    """
    Dashboard dédié à Apple (AAPL).
    """
    df = load_stock_data("AAPL")
    if df is not None:
        st.title("Apple (AAPL)")
        df_melt = prepare_melted_data(df)
        chart = create_bar_chart(df_melt, title="Evolution des prix Open/Close")
        st.altair_chart(chart, use_container_width=True)
    else:
        st.error("Données Apple non trouvées.")