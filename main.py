import os
import json
import menu.menu as menu
import funciones.camper as camp
import funciones.pruebas as prue
import funciones.reportes as rep
import funciones.trainer as train
import funciones.rutas as rut

if __name__=='__main__':
    isAcamptive = True
    while isAcamptive:
        os.system("cls")
        try:
            opMenu = menu.menu_principal()
        except ValueError:
            print("Dato inválido")
        else:
            if opMenu==1:
                camp.registro_camper()
            elif opMenu==2:
                prue.registro_prueba()
            elif opMenu==3:
                train.registro_trainer()
            elif opMenu==4:
                rut.rutas()
            elif opMenu==5:
                camp.estado_camper()
            elif opMenu==6:
                flag = True
                os.system("cls")
                while flag:
                    try:
                        opRep = menu.menu_reportes()
                    except ValueError:
                        print("Dato inválido")
                    else:                           
                        if opRep==1:
                            rep.inscritos()
                        elif opRep==2:
                            rep.aprobados()
                        elif opRep==3:
                            rep.trainer()
                        elif opRep==4:
                            rep.camper_condicional()
                        elif opRep==5:
                            rep.check_ruta()
                        elif opRep==6:
                            rep.dev_ruta()
                        elif opRep==7:
                            flag = False
                        else:
                            print("Opcion inválida") 
                            os.system("pause")                  
            elif opMenu==7:
                isActive = False
                os.system ('cls')
            else:
                print("Opcion inválida") 
                os.system("pause")     
                os.system("cls")             