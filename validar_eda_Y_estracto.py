
def validar_eda_Y_estracto():
    
    edad = input("Ingrese su edad por favor: ")
    estracto = input(
        "Por favor ingrese su estracto rango permitido (1 A 4): ")
    while True:
        if estracto.isdigit() and edad.isdigit() and  bool(edad) and bool(estracto):
            estracto = int(estracto)
            edad = int(edad)

            if edad > 0 and edad <= 150 and estracto > 0 and estracto < 5:
                print(
                    "-------------------------------------------------------------------------------------")
                return True, edad, estracto
                break
            else:

                print(
                    "-------------------------------------------------------------------------------------")
                print(
                    "La edad ingresada o el estracto ingresado no son corretos intentalo de nuevo")
                print(
                    "-------------------------------------------------------------------------------------")
                validar_eda_Y_estracto()

        else:
            print(
                "-------------------------------------------------------------------------------------")
            print(
                "La edad ingresada o el estracto ingresado no son corretos intentalo de nuevo")
            print(
                "-------------------------------------------------------------------------------------")
            validar_eda_Y_estracto()
