# Utiliser une image de base officielle Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de configuration de l'application
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
