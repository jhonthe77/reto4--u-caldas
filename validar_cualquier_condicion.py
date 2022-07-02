def validar_condicion(lista_O_cadena, lista_condiciones, condiciones=0):
    if type(lista_O_cadena) == str:
        lista_O_cadena = list(lista_O_cadena)
    if type(lista_O_cadena) == list and len(lista_O_cadena) > 0 and not list in lista_O_cadena and str(condiciones).isdigit():
        condiciones = int(condiciones)
        contadorv = 0
        contadorf = 0
        for i, j in enumerate(lista_O_cadena):
            if type(lista_O_cadena[i]) == str and type(lista_condiciones) == list:
                for k, l in enumerate(lista_condiciones):
                    if lista_condiciones[k] and type(lista_condiciones[k]) == bool:
                        contadorv += 1
                        if i == len(lista_O_cadena)-1 and contadorf == 0 and condiciones==0:
                            return True
                        if contadorv >= condiciones and condiciones > 0:
                            return contadorv
                    elif not lista_condiciones[k] or contadorf > 0:
                        contadorf += 1
                        if i == len(lista_O_cadena)-1:
                            return False
                    else:
                        return print("El contenido de tu lista no es typo boolean ")

            else:
                return print("El contenido de tu lista no es typo boolean ")

    else:
        return print("Lista bacia o tus datos no son corretos ")