
def calcular_area_del_rectangulo(ancho, largo):
    result = ancho * largo
    return result

def calcular_area_del_triangulo(base, altura):
    respuesta = 0.5 * base * altura
    return respuesta

# Función principal
def Principal():
    ancho = 4
    largo = 6
    print("Área del rectángulo: ()", calcular_area_del_rectangulo(ancho, largo))

    base = 5
    altura = 8
    print("Área del triángulo:", calcular_area_del_triangulo(base, altura))

Principal()
