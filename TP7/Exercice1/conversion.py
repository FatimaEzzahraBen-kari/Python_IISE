# conversion.py

def dollars_to_dirhams(dollars):
    """
    Convertit des dollars en dirhams.
    
    Parameters:
    - dollars (float) : Montant en dollars à convertir.
    
    Returns:
    - float : Montant en dirhams.
    """
    taux_de_change = 10 # Taux de change approximatif
    return dollars * taux_de_change


def meters_to_kilometers(meters):
    """
    Convertit des mètres en kilomètres.
    
    Parameters:
    - meters (float) : Distance en mètres à convertir.
    
    Returns:
    - float : Distance en kilomètres.
    """
    return meters / 1000
