import requests
from bs4 import BeautifulSoup

# URL de la web original
url = 'https://desbrocesenourense.es/'

# Descargar contenido
response = requests.get(url)
if response.status_code != 200:
    print(f"Error al descargar la página: {response.status_code}")
    exit()

# Procesar HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Reemplazar 'Ourense' por 'Pontevedra'
html_modificado = soup.prettify().replace("Ourense", "Pontevedra").replace("ourense", "pontevedra")

# Guardar el resultado como index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_modificado)

print("✅ Página copiada y modificada. Archivo guardado como 'index.html'")
