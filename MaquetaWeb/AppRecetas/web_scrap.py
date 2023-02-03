from bs4 import BeautifulSoup

path_documento = r"C:\Users\54115\Desktop\python\Maqueta\MaquetaWeb\AppRecetas\templates\AppRecetas\prueba.html"
with open(path_documento, "r") as archivo:
    documento = BeautifulSoup(archivo, "html.parser")



def encontrar_etiquetas(documento, etiqueta):
    contenidos_de_etiquetas = []
    for etiqueta in documento.find_all(f"{etiqueta}"):
        contenidos_de_etiquetas.append(etiqueta.string)
    return contenidos_de_etiquetas

print(encontrar_etiquetas(documento, "h1"))