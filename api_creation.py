from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 1. **Unrestricted Resource Consumption**
# Endpunkt, der beliebig viele Daten akzeptiert und speichert
@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_data(as_text=True)  # Keine Begrenzung der Eingabedaten
    with open("data.txt", "a") as f:
        f.write(data + "\n")  # Unbegrenzter Festplattenverbrauch
    return jsonify({"status": "success"}), 200


# 2. **Server Side Request Forgery**
# Endpunkt für externe URLs, ohne die Quelle zu validieren
@app.route('/fetch', methods=['GET'])
def fetch_url():
    url = request.args.get('url')  # Akzeptiert beliebige URLs
    response = requests.get(url)  # Kein Schutz gegen Server Side Request Forgery
    return response.text, response.status_code


# 3. **Security Misconfiguration**
# Debugging aktiviert, sensible Daten in Fehlermeldungen
@app.route('/debug', methods=['GET'])
def debug():
    1 / 0  # Provozierte Exception für Debugging
    return "This should never be reached"


# 4. **Unsafe Consumption of APIs**
# Unsichere Verarbeitung von Daten externer APIs
@app.route('/unsafe_api', methods=['POST'])
def unsafe_api():
    data = request.json
    # Beispiel: Unsichere Verarbeitung der Daten ohne Validierung
    api_response = requests.post("https://external-api.com/process", json=data)
    return api_response.text, api_response.status_code


if __name__ == '__main__':
    app.run(debug=True)  # Debugging aktiviert (Security Misconfiguration)
