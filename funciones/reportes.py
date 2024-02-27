import os
import funciones.maincamper as mc
import funciones.trainer as t

def inscritos():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    cont = 0
    print("Estudiantes en estado Inscrito: \n")
    print("ID\t\tNombre\t\tApellido\t\tEstado\n")
    for i,items in data.items():
        if data[i]["Estado"]=="Inscrito":
            print(f"{i}\t\t{data[i]['Nombre']}\t\t{data[i]['Apellido']}\t\t{data[i]['Estado']}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers en estado Inscrito")
    print("")
    os.system("pause")    
    os.system("cls")

def camper_condicional():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    cont = 0
    print("Estudiantes en riesgo en el ultimo modulo presentado: \n")
    print("ID\t\tNombre\t\tApellido\t\tModulo\n")
    for i,items in data.items():
        dataC = mc.campus["campus"]["pruebas"][i]
        last = str(len(dataC.keys()))
        if data[i]["Estado"]=="Bajo Rendimiento":
            print(f"{i}\t\t{data.get(i).get('Nombre')}\t\t{data.get(i).get('Apellido')}\t\tModulo {last}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers en riesgo en el ultimo modulo")
    print("")
    os.system("pause")
    os.system("cls")

def trainer():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["trainer"]
    print("Trainers que se encuentran trabajando en Campuslands: \n")
    print("ID\t\tNombre\t\tApellido\n")
    if len(data.keys())==0:
        os.system("cls")
        print("No se encuentran Trainers registrados")
    else:
        for i,items in data.items():
            print(f"{i}\t\t{data[i]['nombre']}\t\t{data[i]['nroCel']}")
    print("")
    os.system("pause")
    os.system("cls")

def aprobados():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    print("Estudiantes que aprobaron el examen inicial: \n")
    print("ID\t\tNombre\t\tApellido\t\tEstado\n")
    cont = 0
    for i,items in data.items():
        if data[i]["Estado"]=="Aprobado":
            print(f"{i}\t\t{data[i]['Nombre']}\t\t{data[i]['Apellido']}\t\t{data[i]['Estado']}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers con el examen incial aprobado")
    print("")
    os.system("pause")

def check_ruta():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    temp = {}
    valor = 0
    isTrue = True
    while isTrue:
        try:
            jor = t.validar(valor,"el numero de la jornada (1 - mañana, 2 - tarde)",str)                    
        except ValueError:
            print("Dato inválido")
        else:                                
            if jor == "1":
                jor="manana"
                isTrue = False
            elif jor==2:
                jor="tarde"                                   
                isTrue = False
            else:
                print("Dato no existe")  
        dataR = mc.campus["campus"]["rutas"][jor]
        print("Rutas Existentes")
        cont = 1
        for i,item in dataR.items():
            print(f"{cont} - {i}")
            temp.update({str(cont):i})
            cont+=1
            isTrueRu = True
        while isTrueRu:
            try:
                ruta = t.validar(valor,"la ruta",str)
            except ValueError:
                print("Dato inválido")
            else:
                os.system("cls")
                tempRU = temp.get(ruta)   
                id = dataR[tempRU]['trainer']           
                print(f"\t{tempRU.upper()} - {jor.upper()}\n")
                print(f"TRAINER : {mc.campus['campus']['trainer'][id]['nombre'].upper()}\n")
                print(f"Salon : {dataR[tempRU]['salon'].upper()}\n")
                print("Nombre\t\tApellidos\n")
                dataRU = dataR[tempRU]["campers"]
                for i,item in dataRU.items():
                    print(f"{dataRU[i]['nombre']}\t\t{dataRU[i]['apellido']}") 
                os.system("pause")
                isTrueRu = False

def dev_ruta():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    temp = {}
    valor = 0
    isTrue = True
    while isTrue:
        try:
            jor = t.validar(valor,"El numero de la jornada (1 - mañana, 2 - tarde)",str)                    
        except ValueError:
            print("Dato inválido")
        else:                                
            if jor == "1":
                jor="manana"
                isTrue = False
            elif jor==2:
                jor="tarde"                                   
                isTrue = False
            else:
                print("Opcion seleccionada inexistente.")  
        dataR = mc.campus["campus"]["rutas"][jor]
        print("Rutas Existentes")
        cont = 1
        for i,item in dataR.items():
            print(f"{cont} - {i}")
            temp.update({str(cont):i})
            cont+=1
            isTrueRu = True
        while isTrueRu:
            try:
                ruta = t.validar(valor,"la ruta",str)
            except ValueError:
                print("Dato inválido")
            else:
                os.system("cls")
                tempRU = temp.get(ruta)   
                id = dataR[tempRU]['trainer']           
                print(f"\t{tempRU.upper()} - {jor.upper()}\n")
                print(f"TRAINER : {mc.campus['campus']['trainer'][id]['nombre'].upper()}\n")
                print(f"Salon : {dataR[tempRU]['salon'].upper()}\n")
                contador ={}
                contA = 0
                modA = ""
                contP = 0
                modP = ""
                dataP = mc.campus["campus"]["pruebas"]
                for i,item in dataP.items():
                    for key,value in item.items():
                        if value == "Aprobado":
                            contA+=1
                            contador ={
                                key:{
                                    "contA":contA,
                                    "contP":contP
                                }
                            }
                                

                isTrueRu = False





