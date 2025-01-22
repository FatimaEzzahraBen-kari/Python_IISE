def convert_to_int(value):
    try:
        print(int(value))
    except ValueError:
        print("La valeur n est pas convertible")
        
convert_to_int("abc")
