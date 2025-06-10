# syntax=docker/dockerfile:1

# Étape de base
FROM python:3.12-slim

# Arguments pour l'environnement
ARG SECRET_KEY
ARG SENTRY_DSN
ARG DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  SECRET_KEY=${SECRET_KEY} \
  SENTRY_DSN=${SENTRY_DSN} \
  DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}

# Créer le dossier d'application
WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y build-essential libpq-dev curl

# Installer pip + dépendances
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le reste du code
COPY . .

# Créer l'utilisateur django
RUN groupadd -r django && useradd --no-create-home -r -g django django

# Port exposé par l'application
EXPOSE 8000

# Préparer les fichiers statiques
RUN mkdir -p /app/staticfiles && chown -R django:django /app
RUN python manage.py collectstatic --noinput --clear


# Démarrer avec gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "127.0.0.0:8000"]
