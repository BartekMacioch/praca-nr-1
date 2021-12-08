#zdn4
def print_dict(slownik):
    napis = ""
    for klucz in slownik:
        napis = napis + '"%s" %d ' % (klucz, slownik[klucz])
    print(napis)
print_dict({"a":1, "b":2})