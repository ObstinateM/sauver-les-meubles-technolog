# Les info utiles

Pour installer les packages pythons (si vous ne les avez pas déjà) :

`pip install <nom du package>` => `pip install uvicorn`

Selon votre version de python et/ou votre installation, vous devrez peut-être plutôt utiliser : `python -m pip install <nom du package>`

Utilisez la commande `uvicorn main:app --port 8000` pour lancer le serveur (API REST)

Utilisez la commande `pytest` pour lancer vos tests

Utilisez la commande `docker run -d -p 27017:27017 --name mongo_dev_exam mongodb` pour lancer votre instance de mongodb sur votre PC (pour le développement)

Pour éteindre le conteneur `docker stop mongo_dev_exam`

Pour supprimer le conteneur `docker rm mongo_dev_exam`

Note: il faut éteindre le conteneur avant de pouvoir le lancer

Pour tester votre API vous pouvez vous rendre sur `http://127.0.0.1:8000/docs` ou `http://127.0.0.1:8000/redoc`

Je vous conseille `http://127.0.0.1:8000/docs`

Pour tester vos routes, il vous suffit de cliquer sur la route pour dérouler ses informations.

Vous pouvez ensuite cliquer sur `Try it out` puis `Execute`. (Si votre requête prend des paramètres, vous pourrez les modifier entre le bouton `Try it out` et le bouton `Execute`)

Une commande qui pourrait vous êtes utile est `docker logs <nom_du_conteneur>`. Elle vous permet de voir les logs de votre conteneur.

Une autre commande utile est `docker ps -a`. Elle vous permet de voir la liste de tout vos conteneurs et leurs status (STOP, ON, ...)

## Pour tester votre docker-compose/dockerfile :

`docker compose up -d` pour lancer votre recette docker-compose

`docker compose down` pour l'éteindre
