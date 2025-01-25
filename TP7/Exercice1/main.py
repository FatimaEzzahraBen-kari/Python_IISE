import conversion as c
if __name__ == "__main__":
    # Test de la conversion dollars -> dirhams
    dollars = 15
    dirhams = c.dollars_to_dirhams(dollars)
    print(f"{dollars}$ = {dirhams}DH")

    # Test de la conversion mètres -> kilomètres
    meters = 700
    kilometers = c.meters_to_kilometers(meters)
    print(f"{meters}m = {kilometers}Km")