import requests

URL = "https://integrationsmonitoringXX.niedersachsen.de/"

try:
    response = requests.get(URL, timeout=20)

    if response.status_code != 200:
        print(f"Fehler: HTTP {response.status_code}")
        exit(1)

    print("Seite ist erreichbar.")

except Exception as e:
    print(f"Exception: {e}")
    exit(1)
