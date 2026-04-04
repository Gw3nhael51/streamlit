import streamlit as st
import pandas as pd
import altair as alt

# activer le mode wide
st.set_page_config(layout="wide")

# charger le csv de données
df = pd.read_csv("archive/price_data/AAPL.csv")

# convertir la date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.set_index("Date")

# limiter à 1200 dernières lignes
df_small = df.tail(1200).iloc[::2]

st.title("AAPL")

# préparer les données pour Altair
df_melt = df_small[
    [
        "Open", 
        "Close"
    ]
].reset_index().melt("Date")

# nettoyer les données
df_melt = df_melt.dropna()

# graphique Altair
chart = (
    alt.Chart(df_melt)
    .mark_line()
    .encode(
        # def les coord
        x = "Date:T",
        y = "value:Q",

        # def les couleurs
        color = alt.Color(
            "variable:N",
            scale = alt.Scale(
                domain = ["Open", "Close"],
                range = ["#F0340A", "#1E90FF"] 
            )
        ),

        tooltip = [
            "Date:T", 
            "variable:N", 
            "value:Q"
        ]
    )
    .properties(
        width = "container",
        height = 700
    )
)

st.altair_chart(chart, use_container_width=True)

#
st.title("Slider:")
x = st.slider("x")
st.write(f"{x}² = {x * x}", unsafe_allow_html=True)