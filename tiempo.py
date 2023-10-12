"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
def segundos_a_minutos(sec):
    min = sec / 60
    return min

def segundos_a_horas(sec):
    hr = sec / 3600
    return hr

def minutos_a_segundos(min):
    sec = min * 60
    return sec

def minutos_a_horas(min):
    hr = min / 60
    return hr

def horas_a_segundos(hr):
   sec = hr * 3600 
   return sec

def horas_a_minutos(hr):
    min = hr * 60 
    return min

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de masa:")
    print("60sec a min:", segundos_a_minutos(60))
    print("3600sec a hr:",segundos_a_horas (3600))
    print("60min a sec:", minutos_a_segundos(60))
    print("60min a hr:", minutos_a_horas(60))
    print("3600hr a sec:", horas_a_segundos(3600))
    print("60hr a min:", horas_a_minutos(60))