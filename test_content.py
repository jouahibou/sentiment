import requests
import json

# Adresse IP et port de l'API
api_address = "127.0.0.1"
api_port = 8000

# Informations d'authentification de l'utilisateur
auth = ("alice", "wonderland")

# Phrases à tester
phrases = [
    "life is beautiful",
    "that sucks"
]

# Versions du modèle à tester
versions = ["v1", "v2"]

# Boucle sur les phrases
for phrase in phrases:
    print("Phrase: ", phrase)
    
    # Boucle sur les versions du modèle
    for version in versions:
        print("Version: ", version)
        
        # Construction de l'URL complète
        url = "http://{address}:{port}/{version}/sentiment".format(address=api_address, port=api_port, version=version)
        
        # Données de la requête POST
        data = {"sentence": phrase}
        
        # Envoi de la requête POST avec les informations d'authentification
        response = requests.post(url, data=json.dumps(data), auth=auth, headers={"Content-Type": "application/json"})
        
        # Récupération du score retourné
        score = response.json()["score"]
        
        # Vérification de la positivité ou négativité du score
        if score >= 0.5:
            print("Score: Positive")
        else:
            print("Score: Negative")