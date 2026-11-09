def montecarlo(a, b, c, d, cantidad, semilla):
    # Generador de numeros pseudoaleatorios sin usar import.
    modulo = 2147483647
    multiplicador = 48271
    puntos_elipse = 0
    puntos_interseccion = 0

    # Se generan coordenadas dentro del rectangulo que contiene la elipse.
    for _ in range(cantidad):
        semilla = (multiplicador * semilla) % modulo
        x = (2 * semilla / modulo - 1) * a

        semilla = (multiplicador * semilla) % modulo
        y = (2 * semilla / modulo - 1) * b

        # Se comprueba si el punto cumple las formulas de ambas regiones.
        dentro_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1
        dentro_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

        if dentro_elipse:
            puntos_elipse += 1

            if dentro_hiperbola:
                puntos_interseccion += 1

    return puntos_elipse, puntos_interseccion


def mostrar_resultados(a, b, c, d, cantidad, semilla):
    puntos_elipse, puntos_interseccion = montecarlo(
        a, b, c, d, cantidad, semilla
    )

    area_elipse = 3.1416 * a * b

    print("----------------------------------------")
    print("Valores utilizados:")
    print("a =", a, " b =", b, " c =", c, " d =", d)
    print("Cantidad de puntos:", cantidad)
    print("Puntos dentro de la elipse:", puntos_elipse)
    print("Puntos en la interseccion:", puntos_interseccion)
    print("Area de la elipse:", round(area_elipse, 4))

    if puntos_elipse == 0:
        print("No hubo puntos dentro de la elipse.")
    else:
        proporcion = puntos_interseccion / puntos_elipse
        area_interseccion = area_elipse * proporcion

        print("Porcentaje de interseccion:", round(proporcion * 100, 2), "%")
        print("Area aproximada de interseccion:", round(area_interseccion, 4))


if __name__ == "__main__":
    pruebas = [
        [10, 5, 4, 4, 1000, 12345],
        [12, 7, 5, 4, 10000, 12345],
        [10, 5, 4, 4, 100000, 12345]
    ]

    for prueba in pruebas:
        a = prueba[0]
        b = prueba[1]
        c = prueba[2]
        d = prueba[3]
        cantidad = prueba[4]
        semilla = prueba[5]

        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            print("Los valores a, b, c y d deben ser mayores que cero.")
        elif cantidad <= 0:
            print("La cantidad de puntos debe ser mayor que cero.")
        elif semilla <= 0 or semilla >= 2147483647:
            print("La semilla debe estar entre 1 y 2147483646.")
        else:
            mostrar_resultados(a, b, c, d, cantidad, semilla)
