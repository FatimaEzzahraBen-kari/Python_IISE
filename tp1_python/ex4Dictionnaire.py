def compte_occurences(list):
    occ = {}
    for mot in list:
        if mot in occ:
            occ [mot] += 1
        else:
            occ [mot] = 1
    return occ
print (compte_occurences(['ali', 'kawtar','aya','ali','aya','ali']))