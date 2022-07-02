import validar_caracteres as vd
import validar_eda_Y_estracto as vl_e_e
import asignar_escala as sc
import menu_indicaciones as menu


def lista_usuarios():
    menu.menu_indicaciones()
    usuarios = 0
    lista_CDIA = []
    lista_escalafon=[]
    lista_usuarios=[]
    while usuarios < 10:
        usuario = input("Ingresa tu nombre de usuario por favor: ").upper()
        usuarios += 1
        lista_usuarios.append(usuario)
        validacion, edad, estracto = vl_e_e.validar_eda_Y_estracto()
        lista_CDIA.append(vd.validar_caracteres(validacion))
        sc.asignar_escala(edad, estracto)
        lista_escalafon.append(sc.asignar_escala(edad, estracto))
    return lista_CDIA,lista_escalafon,lista_usuarios

        

