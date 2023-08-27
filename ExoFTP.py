from ftplib import FTP

def list_files_and_folders_recursive(ftp, path):
    def recursive_list(ftp, current_path):
        contents = ftp.nlst(current_path)
        files = []
        folders = []

        for item in contents:
            try:
                # Tentative de changer de répertoire, si cela échoue, c'est un fichier
                ftp.cwd(item)
                ftp.cwd("..")  # Revenir au répertoire précédent
                folders.append(item)
            except:
                files.append(item)

        return files, folders

    ## Recursive explore upgrade with CHAT-GPT4
    def recursive_explore(ftp, current_path):
        files, folders = recursive_list(ftp, current_path)
        all_files = files

        for folder in folders:
            folder_path = f"{current_path}/{folder}"
            subfiles, subfolders = recursive_explore(ftp, folder_path)
            all_files.extend(subfiles)

        return all_files, folders

    return recursive_explore(ftp, path)


# Exemple d'utilisation
from ftplib import FTP

ftp = FTP("ftp.dlptest.com")
ftp.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")

path = "/"
files, folders = list_files_and_folders_recursive(ftp, path)
print("Files:", files)
print("Folders:", folders)



ftp.quit()
