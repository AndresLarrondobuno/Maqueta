from bs4 import BeautifulSoup
import requests

pagina = requests.get('https://listado.mercadolibre.com.ar/corrector-postural-espalda#D[A:corrector%20postural%20espalda]')
html = pagina.text
parser = BeautifulSoup(html, "html.parser")


def encontrar_etiquetas(parser, etiqueta):
    return [ etiqueta.string for etiqueta in parser.find_all(f"{etiqueta}") ]

print(encontrar_etiquetas(parser, "form"))
