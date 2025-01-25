# main.py
from src.math_operations import additionner, soustraire, multiplier, diviser
from src.string_operations import concatener, uppercase

if __name__ == "__main__":
    # Exemple d'opérations mathématiques
    print("Addition: 5 + 3 =", additionner(5, 3))
    print("Multiplication: 4 * 7 =", multiplier(4, 7))

    # Exemple d'opérations sur les chaînes
    print("Concaténation: 'Hello' + ' World' =", concatener("Hello", " World"))
    print("Majuscules: 'bonjour' ->", uppercase("bonjour"))

