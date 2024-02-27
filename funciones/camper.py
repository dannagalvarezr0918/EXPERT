import os
import funciones.maincamper as mc

campers ={}

def validar(valor,txt,tipo):
    valid = True
    while (valid):
        try:
            valor = tipo(input(f"Ingrese {txt} del camper: "))
        except ValueError:
            print("Error en el dato de ingreso, intente de nuevo")
            os.system("pause")
        else:
            if tipo==str:
                if len(valor)==0:
                    print("Error en el dato de ingreso, intente de nuevo") 
                else:
                    valid = False
            else:   
                if valor<=0:
                    print("Error en el dato de ingreso, intente de nuevo")    
                else:
                    valid = False    
    return valor

def registro_camper():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    valor = ""
    print("""
    +++++++++++++++++++++++++++++
    +      INFO DEL CAMPER     +
    +++++++++++++++++++++++++++++
    """)
    id = validar(valor,"ID",str)
    nombre = validar(valor,"nombre",str)
    apellido= validar(valor,"apellidos",str)
    direccion = validar(valor,"direccion",str)
    nroTelCel = validar(valor,"teléfono celular", str)
    nroTelFijo = validar(valor, "teléfono fijo", str)
    os.system("cls")
    
    print("""
    ++++++++++++++++++++++++++++++
    +     DATOS DEL ACUDIENTE    +
    ++++++++++++++++++++++++++++++
    """)
    idAcudiente = validar(valor,"ID del acudiente",str)
    nombreAcudiente = validar(valor,"nombre del acudiente",str)
    telAcudiente = validar(valor,"número de teléfono del acudiente",str)

    camper = {
        "NroId" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Direccion" : direccion,
        "Acudiente" : {},
        "Telecontacto" : {},
        "Estado" : "Inscrito"
    }

    acudiente = {
        "id" : idAcudiente,
        "nrotel" : telAcudiente,
        "nombre" : nombreAcudiente
    }

    phoneCel = {
        "id" : str((len(camper["Telecontacto"]) + 1)),
        "nrotel" : nroTelCel
    }

    phoneFijo = {
        "id" : str((len(camper["Telecontacto"]) + 1)),
        "nrotel" : nroTelFijo
    }

    camper["Acudiente"].update({str((len(camper["Acudiente"]) + 1)).zfill(3) : acudiente})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3) : phoneCel})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3) : phoneFijo})
    campers.update({id : camper})
    mc.newCamper(campers)

def estado_camper():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    valor = ""
    isActive = True
    titulo="""
    ++++++++++++++++++++++++++++++
    +         MATRICULAS         +
    ++++++++++++++++++++++++++++++
    """    
    while isActive:
        print(titulo)
        print("1. Matricular Camper\n2. Salir")
        try:
            opcion = validar(valor,"Opcion seleccionada",int)
        except ValueError:
            print("Error en el dato de ingreso")
        else:
            if opcion == 1:
                temp = {}
                id = validar(valor,"ID",str)
                isTrue = True
                while isTrue:
                    try:
                        jor = validar(valor,"El numero de la jornada (1 - mañana, 2 - tarde)",str)                    
                    except ValueError:
                        print("Error, intente nuevamente")
                    else:                                
                        if jor == "1":
                            jor="manana"
                            isTrue = False
                        elif jor==2:
                            jor="tarde"                                   
                            isTrue = False
                        else:
                            print("Opcion inexistente.")                    
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
                        print("Error en el dato de ingreso, intente nuevamente")
                    else:
                        tempRU = temp.get(ruta)
                        if len(dataR[tempRU]["campers"])<33:
                            tempID ={}
                            dataID = mc.campus["campus"]["campers"][id]
                            tempID.update({"NroId":dataID["NroId"]})
                            tempID.update({"nombre":dataID["Nombre"]})
                            tempID.update({"apellido":dataID["Apellido"]})

                            dataR[tempRU]["campers"].update({id:tempID})
                            print(f"El salon asignado al camper es {dataR[tempRU]['salon']}")
                            print(f"El trainer asignado al camper es {dataR[tempRU]['trainer']}")
                            isTrueRu = False
                        else:
                            print("La ruta esta llena, Intente matricular al camper en otra ruta")
                            os.system("pause")

            
            elif opcion == 2:
                isActive = False
            else:
                print("Error en el dato de ingreso.")
                os.system("pause")
            os.system("cls")

    mc.cf.NewFile(mc.campus)
