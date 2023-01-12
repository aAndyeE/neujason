import json
# Öffne die Datei
with open('tsjsonneu/accounts.json', 'r') as f:
    # Lade die JSON-Daten aus der Datei
    data = json.load(f)
    #print(json.dumps(data, indent=4))

eingabe = input('Was möchtest du tun?\n1 gib ;alter; ein für personen über 25 Jahre ')


if eingabe == 'alter':

    alter = x['age'] > 25

    for x in data:
        print(alter)
        
        