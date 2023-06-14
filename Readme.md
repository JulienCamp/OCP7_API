# API Flask de prédiction par un modèle de scoring

## Projet 7 du parcours Data Scientist OpenClassrooms

API flaks déployée à l'adresse suivante : 
https://ocp7flaskapi.herokuapp.com/

API pouvant être interrogée via requête JSON et renvoyant la prédiction sous format JSON.
Format JSON pour la requête post :
    'client_id': numéro d'identification du client  
    'model_type': type de modèle à utiliser ("default" or "calibrated")  
    'credit_amount': montant du crédit demandé  

Format JSON de la réponse :
    'prediction' : classe prédite (0 ou 1)  
    'confidence' : taux de confiance de la prediction (entre 0 et 1)
