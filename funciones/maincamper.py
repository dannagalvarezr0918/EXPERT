import funciones.corefile as cf
import os
campus={
    "campus":{
        "campers":{},
        "rutas":{
            "manana":{
                "NodeJs":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "Java":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "NetCore":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                }
            },
            "tarde":{
                "NodeJs":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "Java":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "NetCore":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                }
            }
        },
        "pruebas":{},
        "salones":{
            "Artemis":{
                "manana":"",
                "tarde":""
            },
            "Apolo":{
                "manana":"",
                "tarde":""
            },
            "Sputnik":{
                "manana":"",
                "tarde":""
            }
        },
        "trainer":{}
    }
}

cf.MY_DATABASE='data/campus.json'
def newCamper(campers : dict):
    campus["campus"]["campers"].update(campers)
    cf.AddData(campus)

def searchCamper(id)->dict:
    
    return campus.get("campus").get("campers").get(id,{})

def validarArchivoClientes():
    if(cf.checkFile()):
        print('ok')
        os.system('pause')
    else:
        cf.NewFile(campus)

