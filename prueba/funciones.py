import numpy as np
import os
listas_de_rut=[]
listas_de_nombres=[]
lista_de_nombre_mascotas=[]


    

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                listas_de_rut.append
                return rut
                
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            listas_de_nombres.append
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
def validar_nombre_mascota():
    while True:
        nombre_mascota = input("Ingrese nombre de su mascota: ")
        if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha():
            lista_de_nombre_mascotas.append
            return nombre_mascota
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
def validar_cantidad_dias():
    while True: 
        try:    
            dias=int(input("ingrese cantidad de dias entre 1 y 15: "))
            if dias >=1 and dias <=15:
                break
            else:
                print("ERROR! ingrese cantiadad de dias entre 1 y 15 correcta")
        except:
            print("INGRESE UN NUMERO ENTERO")
def validar_num_habitacion():
    while True: 
        try:    
            num_habitacion=int(input("ingrese habitacion: "))
            if num_habitacion >=1 and num_habitacion <=10:
                break
            
            else:
                print("ERROR! ingrese un numero de habitacion correcta")
                
        except:
            print("INGRESE UN NUMERO ENTERO")
def buscar_perro_con_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                listas_de_rut.append
                return rut
                
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        listas_de_rut[i]