import streamlit as st
from src.modules.nvidia import show_nvidia
from src.modules.apple import show_apple

# Activer le mode wide dès le chargement
st.set_page_config(
    page_title="Dashboard Boursier",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """
    Point d'entrée principal de l'application.
    """
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à", ["Nvidia", "Apple"])

    if page == "Nvidia":
        show_nvidia()
    else:
        show_apple()

if __name__ == '__main__':
    main()
