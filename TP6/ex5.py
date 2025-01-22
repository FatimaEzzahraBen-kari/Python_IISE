def process_input(user_input):
    try:
        value = int(user_input)
        print(value)
        res = 10/value
        print(res)
        
    except ValueError:
        print("la valeur n'est pas convertible")
    except ZeroDivisionError:
        print("Erreur! Division par zero!")

process_input("10")