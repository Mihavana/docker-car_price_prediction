# Utilise une image de base Python 3.12 légère
FROM python:3.12.3

# Met à jour les paquets pour corriger les vulnérabilités du système d'exploitation
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier de dépendances et les installe
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code de l'application dans le conteneur
COPY . /app/

# Expose le port par défaut de Django (8000)
EXPOSE 8000

# Définit la commande par défaut pour lancer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]