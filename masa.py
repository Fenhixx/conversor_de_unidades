"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
def kilogramos_a_gramos(kg):
    g = kg * 1000
    return g

def kilogramos_a_toneladas(kg):
    t = kg /1000
    return t

def gramos_a_kilogramos(g):
    kg = g / 1000
    return kg

def gramos_a_toneladas(g):
    t = g / 1000000
    return t

def toneladas_a_kilogramos(t):
    kg = t * 1000
    return kg

def toneladas_a_gramos(t):
    g = t * 1000000
    return g

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de masa:")
    print(" kg * 1000 a g:", kilogramos_a_gramos(1000))
    print(" kg / 1000 a t:",kilogramos_a_toneladas (98.6))
    print("g / 1000 a kg:", gramos_a_kilogramos(0))
    print("g / 1000000 a t:", gramos_a_toneladas(273.15))
    print(" t * 1000 a kg:", toneladas_a_kilogramos(-40))
    print("t * 1000000 a g:", toneladas_a_gramos(100))