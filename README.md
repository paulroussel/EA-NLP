# EA-NLP

EA-NLP

Github du projet de l'EA "deep learning"

autheurs : Paul Roussel, Yannis Bekri, Augustin Espinosa

Fichiers clés :

cache.py - permet d'enregistrer tous les données dans le dossier "cache_dir" pour ne pas avoir à recalculer les méthodes couteuses.

  >> cache.save(objet,nom_objet)    - enregistre un objet
  
  >> cache.load(nom_objet)          - charge un objet
get_data.ipynb - permet de récupèrer les données et de les convertir en format utilisable.

Using_data.ipynb - création et utilisations des modèles finaux.

begin.ipynb - mise en oeuvre du preprocessing, création des features W2Vec et LSA, création du label. -uses preprocessing_data.py

preprocessing_data.py - création de toutes les fonctions de preprocessing.

Embedding feature.ipynb - Création des features de type embedding avec le librairie flair

attention_method.ipynb - Modèle d'attention:
  -Preprocessing des données aux modèles spécifique ici
  -Création du dictionnaire des mots des documents
  -Création des vecteurs de représentation des mots du dictionnaire
  -Entrainement du modèle construit dans models.py
  
  
