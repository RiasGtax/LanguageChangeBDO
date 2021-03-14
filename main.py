import os
import sys
import requests
import urllib.request
import shutil

# -----------------------------------------------
# NOTA: CAMBIAR ESTA RUTA DE DESTINO
# NOTA 2: LA RUTA NO DEBE ACABAR EN /
# EJEMPLO: /Users/ejemplo/Desktop
rutaArchivo = "RUTA"

# Check se ha cambiado la ruta
if rutaArchivo == "RUTA":
    sys.exit("ERROR: Se tiene que cambiar la variable 'rutaArchivo' con el destino!")
# -----------------------------------------------

# Obtener version actual del launcher
versionList = requests.get(
    "http://dn.sea.playblackdesert.com/UploadData/ads_files").text.split()
version = versionList[versionList.index('languagedata_en.loc') + 1]
print("Version: " + version)

# Añadir version a URL
url = "http://dn.sea.playblackdesert.com/UploadData/ads/languagedata_en/{0}/languagedata_en.loc".format(
    version)
print("Url: " + url)

# Descargar archivo
urllib.request.urlretrieve(url, 'languagedata_en.loc')

# Cambiar nombre archivo
os.rename("languagedata_en.loc", "languagedata_es.loc")

# Comprobar si el archivo existe y borrar si existe en el target
if os.path.isfile('{0}/languagedata_es.loc'.format(rutaArchivo)):
    os.remove('{0}/languagedata_es.loc'.format(rutaArchivo))

# Mover archivo
shutil.move("languagedata_es.loc", rutaArchivo)

print("Good job, all worked as expected ofc")
