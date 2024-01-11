import os
import corefile

menus=['Administrador de generos','administrador de actores','administrador de formatos','gestor de informes','gestor de peliculas','salir']

def menuPeliculas():
   menuActivo = True   
header="""
*************************
* ||||||||||||||||||||| *                      
*    MENU DE OPCIONES   *
* ||||||||||||||||||||| *                      
*************************

"""

menuActivo = False

opciones=menus


print(header)
for i,item in enumerate(menus):
       print(f'{i+1}-{item}')

while (menuActivo):
   
   os.system('cls')
   for i,item in enumerate(menus):
       print(f'{i+1}-{item}') 

try:
    opciones=int(input("Seleccione la opcion que desee ejecutar : "))
    
    
except ValueError:
      print("error con la opcion ingresada")
else:
    if (opciones == 1):
        id=(input("Ingrese la id del genero : "))
        nombre=(input("Ingrese el nombre del genero : "))
        
        
    elif (opciones == 2):
        pass
        
    elif (opciones == 3):
        pass
        
    elif (opciones == 4):
        pass
        
    elif (opciones == 5):
        pass
    
    elif (opciones == 6):
        menuActivo=False


