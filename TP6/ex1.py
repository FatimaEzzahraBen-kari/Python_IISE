def safe_division(a,b):

    try:
          res = a/b 
          return ConnectionRefusedError
    except ZeroDivisionError:
        print("Erreur! division par zero")

print(safe_division(8,2))