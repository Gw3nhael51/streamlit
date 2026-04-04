import streamlit as st
import pandas as pd
import altair as alt
from PIL.ImageOps import scale

# activer le mode wide
st.set_page_config(layout="wide")

def app():

    # charger le csv de données
    df = pd.read_csv("archive/price_data/NVDA.csv")

    # convertir la date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.set_index("Date")

    # limiter à 1200 dernières lignes
    df_small = df.tail(2500).iloc[::2]

    st.title("Nvidia")

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
            x="Date:T",
            y="value:Q",

            # def les couleurs
            color=alt.Color(
                "variable:N",
                scale=alt.Scale(
                    domain=["Open", "Close"],
                    range=["#F0340A", "#1E90FF"]
                )
            ),

            tooltip=[
                "Date:T",
                "variable:N",
                "value:Q"
            ]
        )
        .properties(
            width="container",
            height=700
        )

        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    #
    st.title("Slider:")

    #
    x = st.slider("x", key="slider_nvda")
    st.write(f"{x}² = {x * x}", unsafe_allow_html=True)

def app2():

    # charger le csv de données
    df = pd.read_csv("archive/price_data/AAPL.csv")

    # convertir la date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.set_index("Date")

    # limiter à 1200 dernières lignes
    df_small = df.tail(2500).iloc[::2]

    st.title("Apple")

    # préparer les données pour Altair
    df_melt = df_small[
        [
            "Open",
            "Close"
        ]
    ].reset_index().melt("Date")

    # nettoyer les données
    df_melt = df_melt.dropna()

    # graphique Altair (bar chart propre)
    chart = (
        alt.Chart(df_melt)
        .mark_bar(opacity=0.8)
        .encode(
            # def les coord
            x=alt.X("Date:T", title="Date"),
            xOffset="variable:N",   # ← indispensable pour séparer Open / Close
            y="value:Q",

            # def les couleurs
            color=alt.Color(
                "variable:N",
                scale=alt.Scale(
                    domain=["Open", "Close"],
                    range=["#F0340A", "#1E90FF"]
                )
            ),

            tooltip=[
                "Date:T",
                "variable:N",
                "value:Q"
            ]
        )
        .properties(
            width="container",
            height=700
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

if __name__ == '__main__':
    app()
    app2()