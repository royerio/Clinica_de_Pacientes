import os
import os.path
import pickle
import Estructuras
from ast import literal_eval

tuplamedicos=[]

tuplapacientes=[]

tuplaingresos=[]

def Incluir_Medico(tuplamedicosv):
    os.system('cls')
    for x in range(0,len(tuplamedicosv)):
        tuplamedicos.append((tuplamedicosv[x][0],tuplamedicosv[x][1],tuplamedicosv[x][2],tuplamedicosv[x][3],tuplamedicosv[x][4]))
        
    
    while True:
      nuevo_medico=Estructuras.Medico
      nuevo_medico.codigo_medico=input("Ingrese el codigo del medico:")
      nuevo_medico.nombre_medico=input("Ingrese el nombre del medico:")
      nuevo_medico.apellidos_medico=input("Ingrese los apellidos del medico:")
      nuevo_medico.telefono_medico=input("Ingrese el telefono del medico:")
      nuevo_medico.especialidad=input("Ingrese la especialidad del medico:")
      """"""
      tuplamedicos.append((nuevo_medico.codigo_medico,nuevo_medico.nombre_medico,nuevo_medico.apellidos_medico,nuevo_medico.telefono_medico,nuevo_medico.especialidad))
      continuar=input("Preciones <ENTER> para finalizar, cualquier otra tecla para continuar:")
      if not continuar:
          os.system('cls')
          break

    archivo=open("tuplamedicos.txt","wb")
    pickle.dump(tuplamedicos,archivo)
    archivo.close()
    return tuplamedicos

def Incluir_Paciente(tuplapacientesv):
    os.system('cls')
    for x in range(0,len(tuplapacientesv)):
        tuplapacientes.append((tuplapacientesv[x][0],tuplapacientesv[x][1],tuplapacientesv[x][2],tuplapacientesv[x][3],tuplapacientesv[x][4],tuplapacientesv[x][5]))
    while True:
        nuevo_Paciente=Estructuras.Paciente
        nuevo_Paciente.codigo_paciente=input("Ingrese el codigo del paciente:")
        nuevo_Paciente.nombre_paciente=input("Ingrese el nombre del paciente:")
        nuevo_Paciente.apellidos_paciente=input("Ingrese los apellidos del paciente:")
        nuevo_Paciente.direccion_paciente=input("Ingrese la direccion del paciente:")
        while True:
            dia=int(input("Ingrese el dia de nacimiento del paciente:"))
            if 0<dia<32:
                if len(str(dia))==2:
                    break
                if len(str(dia))>2:
                    print("NO digite mas de 1 cero")
                else:
                    dia=("0"+str(dia))
                    break
            else:
                print("Ingrese un dia valido, 1 al 31")
        while True:
            mes=int(input("Ingrese el mes de nacimiento del paciente:"))
            if 0<mes<13:
                if len(str(mes))==2:
                    break
                if len(str(mes))>2:
                    print("NO digite mas de 1 cero")
                else:
                    mes=("0"+str(mes))
                    break
            else:
                print("Ingrese un mes valido, 1 al 12")
        while True:
            año=int(input("Ingrese el año de nacimiento del paciente:"))
            if 0<año<2019:
                break
            else:
                print("Ingrese un mes valido, 0000 al 2018")
        nuevo_Paciente.fecha_nacimiento=str(str(dia)+"-"+str(mes)+"-"+str(año))
        nuevo_Paciente.telefono_paciente=input("Ingrese el telefono del paciente:")
        """"""
        tuplapacientes.append((nuevo_Paciente.codigo_paciente,nuevo_Paciente.nombre_paciente,nuevo_Paciente.apellidos_paciente,nuevo_Paciente.direccion_paciente,nuevo_Paciente.fecha_nacimiento,nuevo_Paciente.telefono_paciente))
        continuar=input("Preciones <ENTER> para finalizar, cualquier otra tecla para continuar:")
        if not continuar:
            os.system('cls')
            break
        
    archivo=open("tuplapacientes.txt","wb")
    pickle.dump(tuplapacientes,archivo)
    archivo.close()
    return tuplapacientes
def Incluir_Ingresos(tuplaingresosv,tuplamedicos,tuplapacientes):
    os.system('cls')
    for x in range(0,len(tuplaingresosv)):
        tuplaingresos.append((tuplaingresosv[x][0],tuplaingresosv[x][1],tuplaingresosv[x][2],tuplaingresosv[x][3],tuplaingresosv[x][4],tuplaingresosv[x][5]))
    while True:
        nuevo_Ingreso=Estructuras.Ingresos
        nuevo_Ingreso.n_ingreso=int(len(tuplaingresos)+1)
        nuevo_Ingreso.habitacion=input("Ingrese la habitacion del paciente:")
        nuevo_Ingreso.cama=input("Ingrese en numero de cama del paciente:")
        while True:
            dia=int(input("Ingrese el dia en el que entra el paciente:"))
            if 0<dia<32:
                if len(str(dia))==2:
                    break
                if len(str(dia))>2:
                    print("NO digite mas de 1 cero")
                else:
                    dia=("0"+str(dia))
                    break
            else:
                print("Ingrese un dia valido, 1 al 31")
        while True:
            mes=int(input("Ingrese el mes en el que entra el paciente:"))
            if 0<mes<32:
                if len(str(mes))==2:
                    break
                if len(str(mes))>2:
                    print("NO digite mas de 1 cero")
                else:
                    mes=("0"+str(mes))
                    break
            else:
                print("Ingrese un mes valido, 1 al 12")
        while True:
            año=int(input("Ingrese el año en el que entra el paciente:"))
            if 0<año<2018:
                break
            else:
                print("Ingrese un mes valido, 0000 al 2018")
        
        nuevo_Ingreso.fecha_ingreso=str(str(dia)+"-"+str(mes)+"-"+str(año))
        continuar=""
        while True:
            codigo_medico=input("Ingrese el codigo del medico:")
            
            for x in range(0,len(tuplamedicos)):
                if (str(codigo_medico))== (str(tuplamedicos[x][0])):
                    nuevo_Ingreso.codigo_medico=codigo_medico
                    continuar="encontrado"
                    print(str(tuplamedicos[x][1]+" "+str(tuplamedicos[x][2])))
                    

            if continuar=="encontrado":
                break
            else:
                print("Codigo de medico no encontrado")
                print("Ingrese otro")
                print("Codigos validos:")
                for x in range(0,len(tuplamedicos)):
                    print(tuplamedicos[x][0])
        continuar=""
        while True:
            codigo_paciente=input("Ingrese el codigo del paciente:")
            
            for x in range(0,len(tuplapacientes)):
                if (str(codigo_paciente))== (str(tuplapacientes[x][0])):
                    nuevo_Ingreso.codigo_paciente=codigo_paciente
                    continuar="encontrado"
                    print(str(tuplapacientes[x][1]+" "+str(tuplapacientes[x][2])))

            if continuar=="encontrado":
                break
            else:
                print("Codigo de medico no encontrado")
                print("Ingrese otro")
                print("Codigos validos:")
                for x in range(0,len(tuplapacientes)):
                    print(tuplapacientes[x][0])

        tuplaingresos.append((nuevo_Ingreso.n_ingreso,nuevo_Ingreso.habitacion,nuevo_Ingreso.cama,nuevo_Ingreso.fecha_ingreso,nuevo_Ingreso.codigo_medico,nuevo_Ingreso.codigo_paciente))
        continuar=input("Preciones <ENTER> para finalizar, cualquier otra tecla para continuar:")
        if not continuar:
                      os.system('cls')
                      break 
    
    archivo=open("tuplaingresos.txt","wb")
    pickle.dump(tuplaingresos,archivo)
    archivo.close()    
    return tuplaingresos
