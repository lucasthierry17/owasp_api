# Unsichere API (OWASP Top 10 Demo)

Diese API dient zur Demonstration von Schwachstellen gemäß der OWASP API Top 10.

**⚠️ WARNUNG**  
Diese API enthält absichtlich Sicherheitslücken und darf **niemals** in einer produktiven Umgebung oder öffentlich zugänglich eingesetzt werden. Verwenden Sie diese API nur in geschützten Testumgebungen und in eigener Verantwortung.
Wenn sie nicht ganz vertraut sind, **nicht** verwenden!

## Anforderungen

- Python 3.9+
- Pip

## Installation

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/lucasthierry17/owasp_api.git
   cd owasp_api
   ```

2. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install flask requests
   ```

## Starten der API

1. Starten Sie die API:
   ```bash
   python api_creation.py
   ```

2. Die API läuft auf `http://127.0.0.1:5000`.

## Endpunkte

1. **Unrestricted Resource Consumption**  
   - **POST /store**  
     Speichert beliebige Daten ohne Begrenzung:
     ```bash
     curl -X POST http://127.0.0.1:5000/store -d "Beliebig große Daten"
     ```

2. **Server Side Request Forgery (SSRF)**  
   - **GET /fetch?url=<url>**  
     Ruft beliebige URLs ab:
     ```bash
     curl http://127.0.0.1:5000/fetch?url=http://example.com
     ```

3. **Security Misconfiguration**  
   - **GET /debug**  
     Löst einen Fehler aus, zeigt aber Debug-Informationen an:
     ```bash
     curl http://127.0.0.1:5000/debug
     ```

4. **Unsafe Consumption of APIs**  
   - **POST /unsafe_api**  
     Übergibt unsichere Daten an eine externe API:
     ```bash
     curl -X POST http://127.0.0.1:5000/unsafe_api -H "Content-Type: application/json" -d '{"key":"value"}'
     ```

---

Nutzen Sie diese API verantwortungsvoll und nur für Testzwecke.
