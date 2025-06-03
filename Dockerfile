# Exemple basique d'un Dockerfile Django

FROM python:3.13-slim

# Variables d'environnement (optionnel, mais conseillé)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copier requirements.txt et installer les dépendances
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier tout le code source
COPY . /app/

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port (selon ton application)
EXPOSE 8000

# Commande pour lancer l'application
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
