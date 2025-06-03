FROM python:3.13-slim

WORKDIR /app

# Copier uniquement requirements pour cache Docker efficace
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Définir la variable d'environnement pour Django
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Créer le dossier pour staticfiles si besoin et permissions
RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles

# Collecter les fichiers statiques pendant la construction
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
