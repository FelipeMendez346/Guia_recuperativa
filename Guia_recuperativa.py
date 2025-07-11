from abc import abstractclassmethod
from abc import ABCMeta
import random
#Clases abstracta de EntidaBiologica
class EntidadBiologica(metaclass=ABCMeta):
    @abstractclassmethod
    def procesar(self):
        pass

#Clases abstracta de Exportar
class Exportar(metaclass=ABCMeta):
    @abstractclassmethod
    def exportar_resultado(self):
        pass
#Clase Gen(Herencia)  
class Gen(EntidadBiologica):
    #iniciar variables(visibilidad)
    def __init__(self):
        self.__nombre=None
        self.__longitud=0
        self.__nivel_expresion=0
        self.__expresion_proteina=None
    #metodos de set/get(encapsulamiento)
    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
    def get_nombre(self):
        return self.__nombre

    def set_longitud(self,Nueva_longitud):
        if isinstance(Nueva_longitud,int):
            self.__longitud=Nueva_longitud

    def get_longitud(self):
        return self.__longitud
    
    def set_Proteina(self,Nueva_proteina):
        if isinstance(Nueva_proteina,Proteina):
            self.__expresion_proteina=Nueva_proteina
    
    def get_Proteina(self):
        return self.__expresion_proteina

    def set_nivel_expresion(self,Nuevo_nivel_expresion):
        if isinstance(Nuevo_nivel_expresion,float):
            self.__nivel_expresion=Nuevo_nivel_expresion

    def get_nivel_expresion(self):
        return self.__nivel_expresion
    #obtiene los datos 
    def obtener_info(self):
        return f"Nombre: {self.__nombre}\nLongitud: {self.__longitud}\nNivel de Expresion: {self.__nivel_expresion}"
    #expresa la proteina(Polimorfismo)
    def procesar(self):
        if self.__expresion_proteina is not None:
            print(f"El gen Produjo la proteina {self.__expresion_proteina.get_nombre()}")
        else:
            print("No se sabe que proceso el gen")
    #Devuelve los datos como string(overriding)
    def __str__(self):
        return str(self.obtener_info())
    

#Clase Analisis con exportar(Herencia)    
class Analisis(Exportar):
    #iniciar variables(visibilidad)
    def __init__(self):
        self.__resultados=[]
        self.__nombre=None
    #agregar Muestra(Sobrecarga/Overloading)
    def agregar_resultado(self,*Nuevo_Muestra):
            self.__resultados.extend(Nuevo_Muestra)
    #metodos de set/get(encapsulamiento) 
    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
    def get_nombre(self):
        return self.__nombre
    #Escribe toda la informacion la terminal
    #(metodo abstracto)
    def exportar_resultado(self):
        n=1
        print(f"Exportando Analisis {self.__nombre}\n")
        for resultado in self.__resultados:
            print(f"{n}.{resultado}")
            n+=1
    #devuelve info en una linea de string
    #(Overiding)
    def __str__(self):
        return f"Analisis: {self.nombre},Muestras: {[muestra.get_nombre() for muestra in self.resultados]}"
         
#Clase Proteina(Herencia)  
class Proteina(EntidadBiologica):
    ##iniciar variables(visibilidad)
    def __init__(self):
        self.__nombre=None
        self.__funcion=None
    #metodos de set/get(encapsulamiento)     
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
        else:
            print("Error al ingresar nuevo nombre a la proteina")

    def get_funcion(self):
        return self.__funcion

    def set_funcion(self,Nueva_funcion):
        if isinstance(Nueva_funcion,str):
            self.__funcion=Nueva_funcion
        else:
            print("Error al ingresar nueva funcion a la proteina")
    #Procesar para dar su nombre y funcion(Polimorfismo)
    def procesar(self):
        print(f"Nombre de la proteina {self.__nombre}\nFuncion: {self.__funcion}")

#Clase muestra(Herencia)  
class Muestra(EntidadBiologica,Exportar):
    #iniciar variables(visibilidad)
    def __init__(self):
        self.__nombre=None
        self.__genes=[]
    #agregar Gen(Relacion de Clase)
    def agregar_Gen(self,Nuevo_gen):
        if isinstance(Nuevo_gen,Gen):
            if Nuevo_gen in self.__genes:
                return
            else:
                self.__genes.append(Nuevo_gen)
    #metodos de set/get(encapsulamiento)
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
        else:
            print("Error al ingresar nuevo nombre a la muestra")
    #Proceso de generar(Polimorfismo)
    def procesar(self):
        print(f"Nombre de muestra: {self.__nombre} \n")
        for gen in self.__genes:
            gen.procesar()
    #genera linea de los datos(overiding)
    def __str__(self):
        return f"{self.__nombre}, Genes: {[gen.get_nombre() for gen in self.__genes]}"
    #genera las muestras en terminal(metodos abstractos)
    def exportar_resultado(self):
        print(f"Exportando Muestra {self.__nombre}")
        for gen in self.__genes:
            print(f"{gen.obtener_info()}")

#main
Prote1=Proteina()
Prote2=Proteina()
Prote1.set_funcion("Genera Tejido oseo")
Prote2.set_funcion("Genera Tejido adiposo")
Prote1.set_nombre("Proteina1")
Prote2.set_nombre("Proteina2")
Gen1=Gen()
Gen2=Gen()
Gen1.set_Proteina(Prote1)
Gen2.set_Proteina(Prote2)
Gen1.set_nombre("Genn1")
Gen2.set_nombre("Genn2")
Gen1.set_longitud(30)
Gen2.set_longitud(35)
Gen1.set_nivel_expresion(2.1)
Gen2.set_nivel_expresion(1.2)
Muestra1=Muestra()
Muestra1.set_nombre("Numero uno")
Muestra1.agregar_Gen(Gen1)
Muestra1.agregar_Gen(Gen2)
Muestra1.agregar_Gen(Gen1)
Muestra1.procesar()
anailisi=Analisis()
anailisi.set_nombre("Paciente 1")
anailisi.agregar_resultado(Muestra1)
#Metodos exportar
anailisi.exportar_resultado()
Muestra1.exportar_resultado()