from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from capsule import Capsule


app = FastAPI()
client = MongoClient("mongodb://localhost:27017")

# capsules_db est le nom de la base de données (comme en SQL)
db = client.capsules_db

# capsules est le nom de la collection (équivalent de la table en SQL)
capsules_collection = db.capsules

# Pour rappel, il existe plusieurs méthodes (verbes) HTTP:
# GET: Récupérer des données (par exemple, les capsules)
# POST: Créer des données (par exemple, une nouvelle capsule)
# PUT: Mettre à jour des données (par exemple, modifier une capsule déjà existante)
# DELETE: Supprimer des données (par exemple, supprimer une capsule)
# PATCH: Mettre à jour partiellement des données (par exemple, modifier uniquement la couleur d'une capsule)

# Il en existe d'autres mais il est peu probable que vous les utilisiez
# Si dans l'énoncé il est écrit faire la route "/capsules" en PATCH, vous devez comprendre
# que vous devez créer une route qui permet de modifier partiellement une capsule.


@app.get("/")
def healthcheck():
    return "It works! :)"


@app.get("/capsules")
def get_capsules():
    return list(capsules_collection.find())


# Ici, fastapi va automatiquement valider le paramètre capsule en fonction de la classe Capsule
# Si le paramètre n'est pas valide, fastapi renverra une erreur 500
@app.post("/capsule")
def create_capsule(capsule: Capsule):
    capsules_collection.insert_one(capsule)
    return "La capsule a bien été créée !"
