def ohce(palabra):
    palabra = palabra.lower().replace(" ", "") #2
    reversa = palabra[::-1] #1
    if palabra == reversa:
        return reversa + "\n" + "¡Bonita palabra!" #2
    return reversa




