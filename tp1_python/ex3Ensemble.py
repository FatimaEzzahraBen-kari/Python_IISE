# def intersectionS(ensemble1, ensemble2):
#     s = ensemble1 & ensemble2
#     return s

# print(intersectionS({1,3,7}, {3,2,5}))

def intersectionS(ensemble1, ensemble2):
    s = ensemble1.intersection(ensemble2)
    return s

print(intersectionS({1,3,7}, {3,2,5}))