import os
from cryptography.fernet import Fernet

# Créer une liste pour stocker les fichiers
files = []

# Utiliser os.listdir() pour lister les fichiers dans le dossier actuel
for file in os.listdir():
    # Exclure les fichiers que vous ne voulez pas crypter
    if file == "problem6.py" or file == "Mykey.key" or file == "solution6.py":
        continue

    # Vérifier si le fichier est un fichier (et non un répertoire)
    if os.path.isfile(file):
        files.append(file)

print(files)

# Charger la clé secrète depuis le fichier Mykey.key
with open("Mykey.key", "rb") as Mykey:
    secretkey = Mykey.read()

# Parcourir la liste des fichiers à crypter
for file in files:
    # Ouvrir le fichier en mode lecture binaire
    with open(file, "rb") as thefile:
        # Lire le contenu du fichier
        contents = thefile.read()

    # Décrypter le contenu du fichier
    contents_decrypted = Fernet(secretkey).decrypt(contents)

    # Ouvrir le fichier en mode écriture binaire pour écrire le contenu décrypté
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
