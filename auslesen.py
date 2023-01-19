import json
# Öffne die Datei
with open('tsjsonneu/accounts.json', 'r') as f:
    # Lade die JSON-Daten aus der Datei
    data = json.load(f)
    #print(json.dumps(data, indent=4))

eingabe = input('Was möchtest du tun?\ngib ;alter; ein für personen über 25 Jahre\nfür den aktuellen Kontostand gib ;kontostand; ein ')


if eingabe == 'alter':

    for alter in data:
        if alter['age'] > 25:
            #print(json.dumps(alter, indent=4))
            print('Name: ', alter['name'], alter['age'])
        
elif eingabe == "kontostand":
    summe = 0
    for accounts in data:
        pruf = accounts["balance"].replace(",","")
        pruf = float(pruf)
        if summe < pruf:
                summe = pruf
    print('Den hoesten Kontostand hat: ',accounts['name'],'mit ',summe)