# Utilise une image Python officielle
FROM python:3.13-slim

# Variables d’environnement pour production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Créer un répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port (utile pour Gunicorn)
EXPOSE 8000

# Commande de lancement avec Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=4"]
