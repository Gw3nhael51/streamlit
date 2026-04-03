# Streamlit Data Lab

Un espace d’expérimentation pour apprendre Streamlit à travers des projets d’analyse de données.  

Objectif : manipuler des DataFrames, créer des dashboards interactifs, explorer des datasets réels et développer des workflows d’analyse propres et reproductibles.

---

## Objectifs du projet
- Découvrir Streamlit de manière pratique  
- Construire des interfaces interactives 100 % Python  
- Manipuler des datasets volumineux (ex : S&P 500)  
- Tester des visualisations, filtres, exports et analyses  
- Structurer un mini‑projet data propre et réutilisable  

---

## Structure du projet

```
streamlit/
│
├── app.py               # Application principale Streamlit
├── archive/             # Datasets locaux (non versionnés)
│   ├── 01_company_info.csv
│   ├── ...
│   └── price_data/
│       ├── AAPL.csv
│       └── ...
└── .gitignore           # Exclusion des environnements et archives
```

---

## Installation

```bash
git clone https://github.com/Gw3nhael51/streamlit.git
cd streamlit
python3 -m venv .venv
# si linux:
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Lancer l’application

```bash
streamlit run app.py
```

---

## Fonctionnalités explorées
- Affichage interactif de DataFrames  
- Téléchargement automatique des tableaux  
- Visualisations (line charts, bar charts, Plotly…)  
- Filtres dynamiques (tickers, dates, colonnes)  
- Manipulation de données financières  
- Tests d’exports CSV / Excel  

---

## Dataset utilisé
Dataset S&P 500 (finances, prix, news, bilans) disponible sur Kaggle :  
https://www.kaggle.com/datasets/sadiqguru/s-and-p-500-stock-data-along-with-financials-and-news

Déposer les fichiers dans :  
```
streamlit/archive/
```

---

## Exemple minimal

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("archive/price_data/AAPL.csv")

st.title("Test DataFrame S&P 500")
st.dataframe(df)
```

## Exemple rendus

![alt text](assets/image-1.png)
![alt text](assets/image-2.png)


---

## Technologies
- Python 3  
- Streamlit  
- Pandas  
- Plotly (optionnel)  

---

## Notes
Ce projet sert de laboratoire personnel pour tester Streamlit, structurer des dashboards et manipuler des données réelles dans un environnement simple et reproductible.