# 📂 Awesome FTP Explorer (ExoFTP)

Un script Python incroyable pour explorer les fichiers et dossiers sur un serveur FTP avec facilité ! 🚀

Ce script vous permet de :

- 📂 Explorer récursivement les fichiers et dossiers sur un serveur FTP.
- ⚡️ Facile à utiliser et à configurer.

## 🛠️ Configuration

1. Clonez ce dépôt ou téléchargez le fichier `ftp_script.py`.
2. Ouvrez le fichier `ExoFTP.py` dans votre éditeur de code préféré.

## ⚙️ Utilisation

1. Configurez les valeurs appropriées pour `ftp_host`, `ftp_username`, `ftp_password` et `remote_path`.
2. Exécutez le script en utilisant Python : `python ExoFTP.py`.

## 📝 Exemple

```python
from ftplib import FTP

# Configurez les informations d'authentification et de chemin distant
ftp = FTP("ftp.example.com")
ftp.login("votre_nom_utilisateur", "votre_mot_de_passe")
remote_path = "/chemin/vers/le/répertoire/distant"

# Liste récursive des fichiers et dossiers
files, folders = list_files_and_folders_recursive(ftp, remote_path)
print("Files:", files)
print("Folders:", folders)

ftp.quit()
