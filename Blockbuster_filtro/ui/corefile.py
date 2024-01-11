import json
import os

MY_DATABASE = ''

def NewFile(*param):
    with open ('data/info_formatos.json',"w") as inf:
        archivos=json.load()
      

def gestorPeliculas(*param):
    with open(MY_DATABASE,"r+") as gp:
        data_file=json.load(gp)
        if(len(param)>1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update({param[0]})
        gp.seek(0)
        json.dump(data_file,gp,indent=4)
        gp.close()



def adminGeneros(*param):
  with open(MY_DATABASE,"r+") as ag:
        data_file=json.load(ag)
        if(len(param)>1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update({param[0]})
        ag.seek(0)
        json.dump(data_file,ag,indent=4)
        ag.close()


def adminActores(*param):
  with open(MY_DATABASE,"r+") as ac:
        data_file=json.load(ac)
        if(len(param)>1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update({param[0]})
        ac.seek(0)
        json.dump(data_file,ac,indent=4)
        ac.close()
        
def adminFormatos(*param):
    with open(MY_DATABASE,"r+") as af:
       data_file=json.load(af)
    if(len(param)>1):
            data_file.update({param[0]:param[1]})
    else:
        data_file.update({param[0]})
        af.seek(0)
        json.dump(data_file,af,indent=4)
        af.close()





