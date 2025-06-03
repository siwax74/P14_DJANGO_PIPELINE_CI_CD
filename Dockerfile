# Utilise une image officielle Python
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers nécessaires dans le conteneur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste de l'application
COPY . .

RUN python manage.py collectstatic --no-input

# Expose le port 8000 (par défaut pour Django)
EXPOSE 8000

# Commande pour démarrer le serveur Django
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
