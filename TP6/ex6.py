def safe_division(a,b):

    try:
          res = a/b 
    except ZeroDivisionError:
        print("Erreur! division par zero")
    else:
        print(f"Le resultat est {res}")
    finally:
         print("Fin du traitement")
         
print(safe_division(8,2))