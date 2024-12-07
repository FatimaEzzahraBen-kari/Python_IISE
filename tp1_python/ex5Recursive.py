def factorielle(n):
    if n< 0: 
        return "Error: Veuillez entrer un nombre positif!"
    elif n==0 or n==1:
        return 1
    else: 
        return n*factorielle(n-1)

print(factorielle(6))