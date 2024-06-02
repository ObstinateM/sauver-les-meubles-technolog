# On choisit l'image de base pour notre conteneur (alpine est une version "light", 
# avec le moins de chose installées possible)
FROM python:alpine

# On copie le fichier main.py depuis notre machine vers le conteneur sous le nom de main.py
COPY main.py main.py
COPY capsule.py capsule.py

# On installe les dépendances de notre application
RUN pip install fastapi uvicorn pymongo pydantic

# On donne la commande à exécuter pour lancer notre application (au démarrage du conteneur)
# Le --host 0.0.0.0 évite des problèmes avec docker
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
