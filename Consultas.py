import time
import os
def Mostrar_Medicos(tuplamedicos):
    os.system('cls')
    print("Codigo del medico:     ", "Nombre del medico:     ", "Apellido del medico:   ","Telefono del medico:   ","Especialidad del medico:")
    for i in range(0,len(tuplamedicos)):
        j=int((30-len(tuplamedicos[i][0]))/8)
        b=int((30-len(tuplamedicos[i][1]))/8)
        c=int((30-len(tuplamedicos[i][2]))/8)
        d=int((30-len(tuplamedicos[i][3]))/8)
        e=int((30-len(tuplamedicos[i][4]))/8)
        x=""
        x=x+(str(tuplamedicos[i][0]))
        for y in range(j):
            x=x+("\t")
        x=x+(str(tuplamedicos[i][1]))
        for y in range(b):
            x=x+("\t")
        x=x+(str(tuplamedicos[i][2]))
        for y in range(c):
            x=x+("\t")
        x=x+(str(tuplamedicos[i][3]))
        for y in range(d):
            x=x+("\t")
        x=x+(str(tuplamedicos[i][4]))
        for y in range(e):
            x=x+("\t")
        print(x)
    time.sleep(10)


def Mostrar_Pacientes(tuplapacientes):   
    os.system('cls')
    print("Codigo del paciente:   ", "Nombre del paciente:   ", "Apellido del paciente: ","Direccion del paciente:","Fecha de nacimiento:   ","Telefono del paciente: ")
    for i in range(0,len(tuplapacientes)):
        j=int((30-len(tuplapacientes[i][0]))/8)
        b=int((30-len(tuplapacientes[i][1]))/8)
        c=int((30-len(tuplapacientes[i][2]))/8)
        d=int((30-len(tuplapacientes[i][3]))/8)
        e=int((30-len(tuplapacientes[i][4]))/8)
        x=""
        x=x+(str(tuplapacientes[i][0]))
        for y in range(j):
            x=x+("\t")
        x=x+(str(tuplapacientes[i][1]))
        for y in range(b):
            x=x+("\t")
        x=x+(str(tuplapacientes[i][2]))
        for y in range(c):
            x=x+("\t")
        x=x+(str(tuplapacientes[i][3]))
        for y in range(d):
            x=x+("\t")
        x=x+(str(tuplapacientes[i][4]))
        for y in range(e):
            x=x+("\t")
        x=x+(str(tuplapacientes[i][5]))
        print(x)
    time.sleep(10)
def Mostrar_Ingresos_Fechas(tuplaingresos,tuplapacientes):
    os.system('cls')
    while True:
        diaa=int(input("Ingrese el dia inicial de la busqueda:"))
        if 0<diaa<32:
            if len(str(diaa))==2:
                break
            if len(str(diaa))>2:
                print("NO digite mas de 1 cero")
            else:
                diaa=("0"+str(diaa))
                break
        else:
            print("Ingrese un dia valido, 1 al 31")
    while True:
        diab=int(input("Ingrese el dia final de la busqueda:"))
        if 0<diab<32:
            if len(str(diab))==2:
                break
            if len(str(diab))>2:
                print("NO digite mas de 1 cero")
            else:
                diab=("0"+str(diab))
                break
        else:
            print("Ingrese un dia valido, 1 al 31")
            
    while True:
        mesa=int(input("Ingrese el mes inicial de la busqueda:"))
        if 0<mesa<32:
            if len(str(mesa))==2:
                break
            if len(str(mesa))>2:
                print("NO digite mas de 1 cero")
            else:
                mesa=("0"+str(mesa))
                break
        else:
            print("Ingrese un mes valido, 1 al 12")
    while True:
        mesb=int(input("Ingrese el mes final de la busqueda:"))
        if 0<mesb<32:
            if len(str(mesb))==2:
                break
            if len(str(mesb))>2:
                print("NO digite mas de 1 cero")
            else:
                mesb=("0"+str(mesb))
                break
        else:
            print("Ingrese un mes valido, 1 al 12")
    while True:
        añoa=int(input("Ingrese el año inicial de la busqueda:"))
        if 0<añoa<=2018:
            if len(str(añoa))==4:
                break
            else:
                print("Ingrese un mes valido, 0000 al 2018")
        else:
            print("Ingrese un mes valido, 0000 al 2018")
    while True:
        añob=int(input("Ingrese el año final de la busqueda:"))
        if 0<añob<=2018:
            break
        else:
            print("Ingrese un mes valido, 0000 al 2018")

    print("El rango es de: "+str(diaa)+"-"+str(mesa)+"-"+str(añoa)+" a "+str(diab)+"-"+str(mesb)+"-"+str(añob))
                                                    

    print("Codigo del paciente:     ", "Nombre del paciente:     ", "Apellidos del paciente:   ","Direccion del paciente:   ","Fecha de nacimiento:    ","Telefono del paciente:  ")
    for i in range(0,len(tuplapacientes)):
        fecha=tuplapacientes[i][4]
        dia=fecha[0:2]
        mes=fecha[3:5]
        año=fecha[6:]
        if int(añoa)<int(año)<int(añob):
            j=int((30-len(tuplapacientes[i][0]))/8)
            b=int((30-len(tuplapacientes[i][1]))/8)
            c=int((30-len(tuplapacientes[i][2]))/8)
            d=int((30-len(tuplapacientes[i][3]))/8)
            e=int((30-len(tuplapacientes[i][4]))/8)
            f=int((30-len(tuplapacientes[i][5]))/8)
            x=""
            x=x+(str(tuplapacientes[i][0]))
            for y in range(j):
                x=x+("\t")
            x=x+(str(tuplapacientes[i][1]))
            for y in range(b):
                x=x+("\t")
            x=x+(str(tuplapacientes[i][2]))
            for y in range(c):
                x=x+("\t")
            x=x+(str(tuplapacientes[i][3]))
            for y in range(d):
                x=x+("\t")
            x=x+(str(tuplapacientes[i][3]))
            for y in range(e):
                x=x+("\t")
            x=x+(str(tuplapacientes[i][4]))
            for y in range(f):
                x=x+("\t")
            x=x+(str(tuplapacientes[i][5]))
            print(x)
        if int(añoa)==int(año) and int(año)==int(añob):
            if int(mesa)<int(mes)<=int(mesb):
                j=int((30-len(tuplapacientes[i][0]))/8)
                b=int((30-len(tuplapacientes[i][1]))/8)
                c=int((30-len(tuplapacientes[i][2]))/8)
                d=int((30-len(tuplapacientes[i][3]))/8)
                e=int((30-len(tuplapacientes[i][4]))/8)
                f=int((30-len(tuplapacientes[i][5]))/8)
                x=""
                x=x+(str(tuplapacientes[i][0]))
                for y in range(j):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][1]))
                for y in range(b):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][2]))
                for y in range(c):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][3]))
                for y in range(d):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][3]))
                for y in range(e):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][4]))
                for y in range(f):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][5]))
                print(x)
        if int(añoa)==int(año) and int(año)==int(añob) and int(mesa)==int(mes) and int(mes)==int(mesb):
            if int(diaa)<int(dia)<=int(diab):
                j=int((30-len(tuplapacientes[i][0]))/8)
                b=int((30-len(tuplapacientes[i][1]))/8)
                c=int((30-len(tuplapacientes[i][2]))/8)
                d=int((30-len(tuplapacientes[i][3]))/8)
                e=int((30-len(tuplapacientes[i][4]))/8)
                f=int((30-len(tuplapacientes[i][5]))/8)
                x=""
                x=x+(str(tuplapacientes[i][0]))
                for y in range(j):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][1]))
                for y in range(b):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][2]))
                for y in range(c):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][3]))
                for y in range(d):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][3]))
                for y in range(e):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][4]))
                for y in range(f):
                    x=x+("\t")
                x=x+(str(tuplapacientes[i][5]))
                print(x)
    time.sleep(10)
def Mostrar_Ingresos_Medicos(tuplamedicos,tuplapacientes,tuplaingresos):
    os.system('cls')
    while True:
        continuar=True
        codigo_medico=input("Ingrese el codigo del medico:")
        for y in range(0, len(tuplamedicos)):
            if codigo_medico==tuplamedicos[y][0]:
                print(tuplamedicos[y][1]+" "+tuplamedicos[y][2])
                continuar=False

        if continuar ==False:
            break
        else:
            print("Codigo de medico no encontrado")
            print("Ingrese otro")
            print("Codigos validos:")
            for x in range(0,len(tuplamedicos)):
                print(tuplamedicos[x][0])
                    
    for j in range(0, len(tuplaingresos)):
        if codigo_medico == tuplaingresos[j][4]:
            codigo_paciente=tuplaingresos[j][5]
            print("Codigo del paciente:   ", "Nombre del paciente:   ", "Apellido del paciente: ","Direccion del paciente:","Fecha de nacimiento:   ","Telefono del paciente: ")
            for i in range(0, len(tuplapacientes)):
                if codigo_paciente==tuplapacientes[i][0]:
                    j=int((30-len(tuplapacientes[i][0]))/8)
                    b=int((30-len(tuplapacientes[i][1]))/8)
                    c=int((30-len(tuplapacientes[i][2]))/8)
                    d=int((30-len(tuplapacientes[i][3]))/8)
                    e=int((30-len(tuplapacientes[i][4]))/8)
                    x=""
                    x=x+(str(tuplapacientes[i][0]))
                    for y in range(j):
                        x=x+("\t")
                    x=x+(str(tuplapacientes[i][1]))
                    for y in range(b):
                        x=x+("\t")
                    x=x+(str(tuplapacientes[i][2]))
                    for y in range(c):
                        x=x+("\t")
                    x=x+(str(tuplapacientes[i][3]))
                    for y in range(d):
                        x=x+("\t")
                    x=x+(str(tuplapacientes[i][4]))
                    for y in range(e):
                        x=x+("\t")
                    x=x+(str(tuplapacientes[i][5]))
                    print(x)
    time.sleep(10)
