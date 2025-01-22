import logging
class NegativeAgeError(Exception):
    def _init_(self, message="L'âge ne peut pas être négatif."):
        super()._init_(message)

def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("La division par zéro n'est pas permise.")
    else:
        print("La division a été effectuée avec succès.")
        return result
    finally:
        print("La fonction de division est terminée.")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("La conversion a échoué : la valeur n'est pas un entier valide.")

def read_file(filename):
    
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        log_error(f"Le fichier '{filename}' est introuvable.")
        raise
    finally:
        print("Tentative de lecture terminée.")

def log_error(message):
    import logging
    logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(message)s')
    logging.error(message)

def set_age(age):
    if age < 0:
        raise NegativeAgeError
    return age

def process_input(user_input):
    try:
        value = int(user_input)
        result = value / 10
        return result
    except ValueError:
        raise ValueError("La valeur fournie n'est pas un entier.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Division par zéro.")