from data_stark import *
from funciones import *
import os

flag_seguir = True

while flag_seguir:
    os.system("cls") #se limpia la consola
    x = menu()
    print("-------------------------------------")
    y = elegir_opcion(x)
    if y == "s":
        flag_seguir = False
    elif y == 8:
        while flag_seguir:
            os.system("cls") #se limpia la consola
            x = segundo_menu()
            print("-------------------------------------")
            y = segundo_elegir_opcion(x)
            if y == 15:
                break
            elif y == 16:
                x = tercer_menu()
            elif y == "s":
                flag_seguir = False
                break
            os.system("Pause")
                
    os.system("Pause")
        
