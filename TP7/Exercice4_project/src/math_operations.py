def additionner(a,b):
    """Retourne la somme de a et b."""
    return a+b
def soustraire(a,b):
    """Retourne la différence entre a et b."""
    return a-b
def multiplier(a,b):
    """Retourne le produit de a et b."""
    return a*b
def diviser(a,b):
    """Retourne le quotient de a et b. Lance une exception si b est zéro."""
    if b== 0:
        raise ValueError("Erreur! Division par zero")
    return a/b