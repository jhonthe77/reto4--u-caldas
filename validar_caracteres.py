import validar_cualquier_condicion as vc
import validar_eda_Y_estracto as vd


def validar_caracteres(validacion):
    CDIA = input("7-Ingresa tu CDIA por favor: ").upper()
   

    print("-------------------------------------------------------------------------------------")
    if not CDIA.isalnum() and bool(CDIA):
        condiciones = [len(CDIA) == 10, '?' in CDIA or '=' in CDIA,
                       '-' in CDIA, CDIA.find('@') == 5, CDIA.count('k') <= 3,
                        CDIA.index(CDIA[0]) != CDIA.index(CDIA[1-len(CDIA)])]

        entrar = vc.validar_condicion(CDIA, condiciones)
        if entrar and validacion:
            print("Tu CDIA es valido :)")
            print(
                "Tu CDIA No Esta en Nuestra base de Datos registro exitoso..")
            
            return CDIA

    else:
        print(
            "--------------------CDIA invalido------------------------------------------ ")
        print("")
        validacion = vd.validar_eda_Y_estracto()
        validar_caracteres(validacion)
