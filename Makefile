# Variables
PYTHON = .venv/bin/python
STREAMLIT = .venv/bin/streamlit

# Création de l'environnement sur Windows
env-w:
	python -m venv .venv
	@echo "Pour activer l'environnement : .venv\Scripts\activate"

# Création de l'environnement sur Linux/macOS
env-l:
	python3 -m venv .venv
	@echo "Pour activer l'environnement : source .venv/bin/activate"

# Lancer l'application
run:
	$(STREAMLIT) run main.py

# Installer les dépendances
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# Nettoyage
clean:
	rm -rf __pycache__
	rm -rf .streamlit/cache