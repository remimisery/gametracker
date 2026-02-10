# Utilisation de l'image de base demandée [cite: 79]
FROM python:3.11-slim

# Installation du client MySQL pour permettre aux scripts Bash de communiquer avec la base [cite: 80]
RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt/lists/*

# Définition du dossier de travail dans le conteneur
WORKDIR /app

# Installation des dépendances Python 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout le code source et des scripts dans le conteneur [cite: 81]
COPY . .

# Donner les droits d'exécution aux scripts Bash [cite: 81]
RUN chmod +x scripts/*.sh

# Commande par défaut (sera souvent surchargée par docker-compose)
CMD ["python", "src/main.py"]


