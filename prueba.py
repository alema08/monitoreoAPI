import requests

dato = {"lugar":"Medellín", "autor": "alejandro", "temperatura": 34.9, "humedad": 87.5}

res = requests.post("https://diplomadofisica-alejandromira.b4a.run/monitoreo", json=dato)

print(res.text)