import pandas as pd

def load_stock_data(ticker, tail=2500, skip=2):
    """
    Charge les données boursières depuis un fichier CSV et effectue un pré-traitement de base.
    """
    file_path = f"archive/price_data/{ticker}.csv"
    try:
        # On lit le CSV
        df = pd.read_csv(file_path)
        
        # On convertit et indexe la date
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.set_index("Date")
        
        # Échantillonnage simple
        return df.tail(tail).iloc[::skip]
    except FileNotFoundError:
        return None

def prepare_melted_data(df, columns=None):
    """
    Prépare les données pour Altair (format long / melt).
    """
    if columns is None:
        columns = ["Open", "Close"]
    df_melt = df[columns].reset_index().melt("Date")
    return df_melt.dropna()
