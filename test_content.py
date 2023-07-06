import requests
import json
import urllib.parse

# Adresse IP et port de l'API
api_address = "127.0.0.1"
api_port = 8000

# Informations d'authentification de l'utilisateur
username = "alice"
password = "wonderland"

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
        url = "http://{address}:{port}/{version}/sentiment?username={username}&password={password}&sentence={sentence}".format(
        address=api_address,
        port=api_port,
        version=version,
        username=urllib.parse.quote(username),
        password=urllib.parse.quote(password),
        sentence=urllib.parse.quote(phrase)
    )
        
        # Données de la requête POST
        data = {"sentence": phrase}
        
        # Envoi de la requête POST avec les informations d'authentification
        response = requests.get(url)
        
        # Récupération du score retourné
        score = response.json()['score']
        
         # Vérification de la positivité ou négativité du score
        if score >= 0.5:
            print("Score: Positive")
        else:
            print("Score: Negative")
        
        