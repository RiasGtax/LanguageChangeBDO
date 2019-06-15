import os
import sys
import requests
import urllib.request
import zipfile
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
version = str(requests.get(
    "http://akamai-gamecdn.blackdesertonline.com/live001/game/config/config.language.version").json())
print("Version: " + version)

# Añadir version a URL
url = "http://akamai-gamecdn.blackdesertonline.com/live001/game/language/BDOLanguage_{0}.zip".format(
    version)
print("Url: " + url)

# Nombre archivo
nombreConExtension = "{0}.zip".format(version)

# Comprobar que el archivo no esta ya descargado
if os.path.isfile(nombreConExtension):
    sys.exit("ERROR: Ya tienes esta version descargada, borra el zip con el nombre: {0}".format(nombreConExtension))

# Descargar archivo
urllib.request.urlretrieve(url, nombreConExtension)

# Extraer archivo
with zipfile.ZipFile(nombreConExtension, "r") as zip_ref:
    zip_ref.extractall(version)

# Cambiar nombre archivo
os.rename("{0}/languagedata_en.loc".format(version), "{0}/languagedata_es.loc".format(version))

# Comprobar si el archivo existe y borrar si existe en el target
if os.path.isfile('{0}/languagedata_es.loc'.format(rutaArchivo)):
    os.remove('{0}/languagedata_es.loc'.format(rutaArchivo))

# Mover archivo
shutil.move("{0}/languagedata_es.loc".format(version), rutaArchivo)

# Borrar carpeta descomprimida
shutil.rmtree(version)

print("Good job, all worked as expected ofc")