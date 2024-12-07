def analyse_texte(texte):
    #compter le nombre des mots 
    mots = texte.split()
    nbr_mots= len(mots)
    #compter le nombre des caractères
    nbr_c= len(texte)
    return {'Nombre_de_mots': nbr_mots, 'Nombre_de_caractères': nbr_c}
print(analyse_texte("fati fleur"))
