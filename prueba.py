from os import system
try:
    from bs4 import BeautifulSoup
    import requests
except ModuleNotFoundError:
    os.system('pip install BeautifulSoup')
    os.system('pip install request')
    os.system('pip install lxml')
finally:
    print("Iniciando ejecución")
# El código se arriba es solo para evitar errores

# import lxml

r = input("Página a buscar (URL de la página, hasta ahora solo steam): ") # Intermediario para buscar la página deseada 
s = requests.get(r) # Request va a almacenar el HTML de la página
interaction = BeautifulSoup(s.content, "lxml") # Interacción con los elementoa del html

n = soup.find('div', id="appHubAppName").txt # Nombre del juego de steam 

i = soup.find("El precio de",n,"es: ","div", class_="game_purchase_price price").txt # Precio de steam en texto

print(i.strip())


