import os
from tabulate import tabulate
import funciones.maincamper as mc

def validar(valor,txt,tipo):
    valid = True
    while (valid):
        try:
            valor = tipo(input(f"Ingrese {txt}:"))
        except ValueError:
            print("Dato inválido")
            os.system("pause")
        else:
            if tipo==str:
                if len(valor)==0:
                    print("Dato inválido") 
                else:
                    valid = False
            else:   
                if valor<=0:
                    print("Dato inválido")    
                else:
                    valid = False    
    return valor

def registro_trainer():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    trainer = {}
    valor = ""
    isActive = True
    while isActive:
        print("""
    +++++++++++++++++++++++
    +     MENU TRAINER    +
    +++++++++++++++++++++++""")
        menu = (['1.', 'Registrar Trainer'], ['2.', 'Asignar Horario y Ruta y Salon'], ['3', 'Asignar Ruta'], ['4', 'Salir'])
        print(tabulate(menu,tablefmt="grid"))
        try:
            opcion = validar(valor,"Opcion seleccionada",int)
        except ValueError:
            print("Error en el dato de ingreso")
        else:
            if opcion == 1:
                id = validar(valor,"ID del Trainer",str)
                nombre = validar(valor,"Nombre completo del Trainer",str)
                nroCel = validar(valor,"Teléfono celular del Trainer", str)
                trainer={
                    "id":id,
                    "nombre":nombre,
                    "nroCel":nroCel,
                    "ruta":{
                        "manana":"",
                        "tarde":""
                    }
                }
                try:
                    mc.campus["campus"]["trainer"].update({id:trainer})                
                except KeyError:
                    mc.campus["campus"].update({"trainer":{id:trainer}})
                else:
                    mc.campus["campus"]["trainer"].update({id:trainer})
                mc.cf.NewFile(mc.campus)
                os.system("cls")
            elif opcion == 2:
                os.system("cls")
                isActiveTrainer = True
                if len(mc.campus["campus"]["trainer"])==0:
                    print("No se cuenta con Trainers Inscritos")
                    os.system("pause")
                    os.system("cls")
                    isActiveTrainer = False
                while isActiveTrainer:
                    id = validar(valor,"ID del Trainer",str)
                    try:
                        data = mc.campus["campus"]["trainer"][id]
                    except KeyError:
                        print("El Trainer no se encuentra registrado")
                    else: 
                        isTrue = True
                        if len(data["ruta"]["manana"])!=0 and len(data["ruta"]["tarde"])!=0:
                            print("El Trainer ya cuenta con rutas asignadas en las 2 jornadas")
                            isTrue = False
                        while isTrue:
                            if len(data["ruta"]["manana"])!=0:
                                print("El Trainer cuenta con una ruta asignada en la jornada de la mañana, asigne la ruta para la jornada de la tarde")
                                jor="tarde"
                                reg_ruta(jor,id)
                                isTrue = False
                                isActiveTrainer = False
                            elif len(data["ruta"]["tarde"])!=0:
                                print("El Trainer cuenta con una ruta asignada en la jornada de la tarde, asigne la ruta para la jornada de la mañana")
                                jor="manana"
                                reg_ruta(jor,id)
                                isTrue = False
                                isActiveTrainer = False
                            else:
                                try:
                                    jornada = validar(valor,"Ingrese el numero de la jornada (1 - mañana, 2 - tarde): ",str)
                                except ValueError:
                                    print("Dato inválido")
                                else:                                
                                    if jornada == "1":
                                        jor="manana"
                                        reg_ruta(jor,id)
                                        isTrue = False
                                    elif jornada==2:
                                        jor="tarde"
                                        reg_ruta(jor,id)                                    
                                        isTrue = False
                                    else:
                                        print("Opcion seleccionada inexistente.") 
                                        os.system("pause")
                                isActiveTrainer = False

                
            elif opcion == 3:
                pass
            elif opcion == 4:
                isActive = False

    mc.cf.NewFile(mc.campus)

def reg_ruta(jor:str,id):
    temp = {}
    tempS = {}
    valor = 0
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
            ruta = validar(valor,"la ruta",str)
        except ValueError:
            print("Dato inválido")
        else:
            tempRU = temp.get(ruta)
            dataR[tempRU].update({"trainer":id})
            isTrueRu = False
    dataS = mc.campus["campus"]["salones"]
    print("Salones Existentes")
    cont = 1
    for i,item in dataS.items():
        print(f"{cont} - {i}")
        tempS.update({str(cont):i})
        cont+=1
    isTrueSa = True
    while isTrueSa:
        try:
            salon = validar(valor,"el salon",str)
        except ValueError:
            print("Dato inválido")
        else:
            tempSa = tempS.get(salon)
            if len(dataS[tempSa][jor])!=0:
                print("El salon ya se encuentra asignado en esa jornada, intente con otro.")
            else:
                dataS[tempSa].update({jor:tempRU})
                dataR[tempRU].update({"salon":tempSa})
                isTrueSa = False
    mc.campus["campus"]["rutas"][jor].update(dataR)
    mc.campus["campus"]["salones"].update(dataS)
    mc.campus["campus"]["trainer"][id]["ruta"].update({jor:tempRU})    
    mc.cf.NewFile(mc.campus)
    os.system("cls") 