"""
Elaborado por:
Roger Méndez Ramírez A43333
Jonathan Barrantes Castillo B50891
Josué Herrera Martínez B63440
"""
import os.path
import random
import pickle
from ast import literal_eval

import Incluir
import Consultas

print
medico=True
paciente=True
ingreso=True

tuplamedicos=[]

tuplapacientes=[]

tuplaingresos=[]

if(os.path.exists("tuplamedicos.txt")):    
    archivo=open("tuplamedicos.txt","rb")
    linea=pickle.load(archivo)
    tuplamedicos=linea
    archivo.close()

else:
    medico=False

if(os.path.exists("tuplapacientes.txt")):
    archivo=open("tuplapacientes.txt","rb")
    linea=pickle.load(archivo)
    tuplapacientes=linea
    archivo.close()
else:
    paciente=False

if(os.path.exists("tuplaingresos.txt")):
    archivo=open("tuplaingresos.txt","rb")
    linea=pickle.load(archivo)
    tuplaingresos=linea
    archivo.close()

else:
    ingreso=False


"""
Para limpiar la consola de python unicamente, no funciona con el IDLE
os.system('cls')

"""
while True:
    os.system('cls')
    print("1. Incluir Médicos.")
    print("2. Incluir Pacientes.")
    print("3. Incluir ingresos de pacientes.")
    print("4. Mostrar listado de médicos.")
    print("5. Mostrar listado de pacientes.")
    print("6. Mostrar ingresos de pacientes en un periodo de fechas.")
    print("7. Mostrar ingresos de pacientes de acuerdo a un médico.")
    print("8. Salir")
    
    opcion=input("Digite una opcion: ")
    if opcion=="1":
        tuplamedicos=Incluir.Incluir_Medico(tuplamedicos)        
        opcion=""
    if opcion=="2":
        if medico ==True:
            tuplapacientes=Incluir.Incluir_Paciente(tuplapacientes)
            opcion=""
        else:
            print("No hay medicos ingresados")
    if opcion=="3":
        if medico==True and paciente==True:
            tuplaingresos=Incluir.Incluir_Ingresos(tuplaingresos,tuplamedicos,tuplapacientes)
            opcion=""
        else:
            print("No hay medicos o no hay pacientes")
    if opcion=="4":
        Consultas.Mostrar_Medicos(tuplamedicos)
        opcion=""
    if opcion=="5":
        Consultas.Mostrar_Pacientes(tuplapacientes)
        opcion=""        
    if opcion=="6":
        Consultas.Mostrar_Ingresos_Fechas(tuplaingresos,tuplapacientes)
        opcion=""        
    if opcion=="7":
        Consultas.Mostrar_Ingresos_Medicos(tuplamedicos,tuplapacientes,tuplaingresos)
        opcion=""
    if opcion=="8":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Digite una opcion valida, del 1 al 8")
        
        
