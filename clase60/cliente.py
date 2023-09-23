import requests

url = 'https://miniature-goggles-v6vqw6wg75g53wprg-8000.app.github.dev/encolar'

# ejemplo request en GET
# r = requests.get(url)
# print(r.text)

# ejemplo request en POST
r = requests.post(url, json={'nombre': 'Santiago', 'productos': ['Pan', 'Arroz']})
r = requests.post(url, json={'nombre': 'Cristian', 'productos': ['Leche', 'Huevos']})
r = requests.post(url, json={'nombre': 'Emanuel', 'productos': ['Mantequilla', 'Cafe']})
print(r.text)