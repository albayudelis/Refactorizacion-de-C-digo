def puntos_calculados(a: int, b: int, c: int):
    total = a + b + c
    return total


def sort_students():
    # Puntos de estudiantes
    Puntos_de_Harry = 20
    Puntos_de_Hermione = 25
    Puntos_de_Ron = 18
    Puntos_de_Draco = 30

    gryffindor = puntos_calculados
    (Puntos_de_Harry,
     Puntos_de_Hermione,
     Puntos_de_Ron)

    slytherin = puntos_calculados(Puntos_de_Draco, 0, 0)
    print("Puntos de Gryffindor: ", gryffindor)
    print("Puntos de Slytherin: ", slytherin)


sort_students()
