class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age < 0:
        raise NegativeAgeError("l'age ne peut pas etre negatif")
    
try:
    set_age(-9)
except NegativeAgeError as e:
    print(e)