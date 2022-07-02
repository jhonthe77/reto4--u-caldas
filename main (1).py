
import lista_usuarios as ls
# ---------------------------------------------------------------------------------------

lista_CDIA, lista_escalafon, lista_usuarios = ls.lista_usuarios()
for i, j in enumerate(lista_CDIA):
    print("[",lista_CDIA[i],end=" ]")
    print("[",lista_escalafon[i],end=" ]")         
    print("[", lista_usuarios[i],"]")
