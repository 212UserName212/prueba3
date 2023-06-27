import numpy as np
import os
os.system("cls")
import funciones as fn

while True:
    
    
    
    print(""""
                    La guardería Mascota Segura
          1.-grabar datos
          2.-buscar
          3.-retirarse
          4.-salir
          """)
    while True: 
        try:    
            
            opcion=int(input("ingrese una opcion 1,2,3,4: "))
            if opcion >=1 and opcion <=4:
                break
            else:
                print("ERROR! ingrese una opcion correcta")
        except:
            print("INGRESE UN NUMERO ENTERO")
    if opcion==1:
        fn.validar_rut()
        fn.validar_nombre()
        fn.validar_nombre_mascota()
        fn.validar_cantidad_dias()
        fn.validar_num_habitacion()

    elif opcion==2:
        fn.buscar_perro_con_rut()
    elif opcion==3:
        pass
    else:
        print("Adios")
        break 
        
        