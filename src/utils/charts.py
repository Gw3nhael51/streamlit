import altair as alt

def create_line_chart(df_melt, title=""):
    """
    Crée un graphique en ligne Altair (standard pour Nvidia).
    """
    chart = (
        alt.Chart(df_melt)
        .mark_line()
        .encode(
            x="Date:T",
            y="value:Q",
            color=alt.Color(
                "variable:N",
                scale=alt.Scale(
                    domain=["Open", "Close"],
                    range=["#F0340A", "#1E90FF"]
                )
            ),
            tooltip=["Date:T", "variable:N", "value:Q"]
        )
        .properties(width="container", height=600, title=title)
        .interactive()
    )
    return chart

def create_bar_chart(df_melt, title=""):
    """
    Crée un graphique en barres Altair (standard pour Apple).
    """
    chart = (
        alt.Chart(df_melt)
        .mark_bar(opacity=0.8)
        .encode(
            x=alt.X("Date:T", title="Date"),
            xOffset="variable:N",
            y="value:Q",
            color=alt.Color(
                "variable:N",
                scale=alt.Scale(
                    domain=["Open", "Close"],
                    range=["#F0340A", "#1E90FF"]
                )
            ),
            tooltip=["Date:T", "variable:N", "value:Q"]
        )
        .properties(width="container", height=600, title=title)
        .interactive()
    )
    return chart
