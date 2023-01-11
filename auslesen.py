import json
# Öffne die Datei
with open('tsjsonneu/accounts.json', 'r') as f:
    # Lade die JSON-Daten aus der Datei
    data = json.load(f)
    #print(json.dumps(data, indent=4))

    print(data[1])