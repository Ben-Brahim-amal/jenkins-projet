import requests
import json

# Ta clé Gemini personnelle
API_KEY = "AIzaSyBQv8D4vQMijV5e4LClGSkAbQW_Xq23zSE"
# URL avec f-string pour injecter la clé
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Lire les logs Jenkins depuis le fichier (encodage latin1 pour éviter erreurs)
with open("logs.txt", "r", encoding="latin1") as f:
    logs = f.read()

# Préparer le prompt pour Gemini
prompt = f"""Aide à comprendre l'erreur si elle existe dans les logs suivants.
Si il n'y a pas d'erreur, mentionne que tout va bien.
Dans les 2 cas fais un résumé des logs.
Très important : Propose une solution aux erreurs rencontrées.

Voici les logs :
{logs}
"""

headers = {
    "Content-Type": "application/json"
}

body = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

summary = None  # Résumé par défaut

try:
    # Appel API Gemini
    response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(body))
    response.raise_for_status()  # Lève une erreur si status != 200

    # Gérer la réponse
    data = response.json()
    summary = data["candidates"][0]["content"]["parts"][0]["text"]

except requests.exceptions.HTTPError as e:
    if response.status_code == 429:
        summary = "⚠️ Erreur 429: Trop de requêtes envoyées à Gemini. Réessaie plus tard."
    else:
        summary = f"❌ Erreur API Gemini : {e}"
except Exception as e:
    summary = f"❌ Erreur inattendue : {e}"

# Afficher dans Jenkins console
print("\n===== Résumé des logs par Gemini =====\n")
print(summary)
print("\n======================================\n")

# Sauvegarder dans un fichier
with open("resume_logs.txt", "w", encoding="cp1252", errors="replace") as out:
    out.write(summary)
