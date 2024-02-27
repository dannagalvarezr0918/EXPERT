import os
from tabulate import tabulate

def menu_principal():
    titulo=("""
+++++++++++++++++++++++++++++++++++++
+   SEGUIMIENTO ACADEMICO CAMPERS   +
+++++++++++++++++++++++++++++++++++++""")
    hasError = True
    print(titulo)
    menu = [["1.","Registrar camper"],["2.","Registrar pruebas"],["3.","Agregar trainer"],["4.","Registrar ruta "],["5.","Matricula"],['6.', 'Reportes'],['7.', 'Salir']]
    print(tabulate(menu,tablefmt="grid"))

    while hasError:
        try:
            return int(input("- "))
        except ValueError:
            print("Dato inválido")
            os.system("pause")
            hasError = True

def menu_reportes():
    titulo="""
    +++++++++++++++++++++++++++++++
    +        MENU REPORTES        +
    +++++++++++++++++++++++++++++++
    """    
    hasError = True
    print(titulo)
    menu = [["1.","Campers Inscritos "],["2.","Campers examen inicial aprobado"],["3.","Trainers"],["4.","Estudiantes con bajo rendimiento"],["5.","Inscritos a ruta de entrenamiento"],['6.', 'Desempeño Modulos por Ruta'],['7.', 'Menu Principal']]
    print(tabulate(menu,tablefmt="grid"))
  
    while hasError:
        try:
            return int(input("- "))
        except ValueError:
            print("Dato inválido")
            os.system("pause")
            hasError = True
