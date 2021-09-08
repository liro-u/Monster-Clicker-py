def open_txt(source):
    """
    cette focntion permet d'ouvrir un document texte
    il faut y entrer:
            source
    """
    with open(source, "r") as record_fichier:
        return record_fichier.readlines()
