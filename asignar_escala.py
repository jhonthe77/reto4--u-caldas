
def asignar_escala(edad, estracto):
    estractos = [estracto <= 2, estracto <= 4]
    edades = [edad > 12 and edad < 20, edad >= 20 and edad <= 40, edad > 40]
    if estractos[0]:
        for i, k in enumerate(edades):
            if edades[i]:
                return i+1
                
    elif estractos[1]:
        for i in range(3, 6):
            if edades[i-3]:
                return i+1
                