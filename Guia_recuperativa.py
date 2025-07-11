from abc import abstractclassmethod
from abc import ABCMeta
import random

class EntidadBiologica(metaclass=ABCMeta):
    @abstractclassmethod
    def procesar(self):
        pass

class Expresion():
    @abstractclassmethod
    def exportar_resultado(self):
        pass

class Gen(EntidadBiologica):
    def __init__(self):
        self.__nombre=None
        self.__longitud=0
        self.__nivel_expresion=0
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

    def set_nivel_expresion(self,Nuevo_nivel_expresion):
        if isinstance(Nuevo_nivel_expresion,float):
            self.__nivel_expresion=Nuevo_nivel_expresion

    def get_nivel_expresion(self):
        return self.__nivel_expresion

    def obtener_info(self):
        return self.__nombre,self.__longitud,self.__nivel_expresion

    def procesar(self):
        print(f"Nombre: {self.__nombre}\nLongitud: {self.__longitud}\nNivel de Expresion: {self.__nivel_expresion}")

    def __str__(self):
        return str(self.obtener_info())
    


    
    
class Analisis(EntidadBiologica):
    def __init__(self):
        self.__resultados=[]
        self.__nombre=None
    def agregar_resultado(self,*Nuevo_resultado):
            self.__resultados.extend(Nuevo_resultado)
    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
    def get_nombre(self):
        return self.__nombre
    def procesar(self):
        n=1
        print(f"Nombre del analisis: {self.__nombre} \n")
        for resultado in self.__resultados:
            print(f"{n}.{resultado}")
            n+=1
    def __str__(self):
        return self.__resultados
    
    def exportar_resultado(self):
        print(f"[Exportando analisis {self.__nombre}]")
        for Muestra in self.__resultados:
            print(f" - {Muestra.procesar()}")     

class Muestra(EntidadBiologica):
    def __init__(self):
        self.__nombre=None
        self.__genes=[]
    def agregar_Gen(self,Nuevo_gen):
        if isinstance(Nuevo_gen,Gen):
            if Nuevo_gen in self.__genes:
                return
            else:
                self.__genes.append(Nuevo_gen)
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
        else:
            print("Error a ingresar nuevo nombre a la muestra")
    def procesar(self):
        print(f"Nombre de muestra {self.__nombre} \n")
        for gen in self.__genes:
            gen.procesar()
    
    def __str__(self):
        return self.__nombre,[gen.get_nombre() for gen in self.__genes]
    
    def exportar_resultado(self):
        print(f"[Exportando Muestra {self.__nombre}]")
        for gen in self.__genes:
            print(f" - {gen.obtener_info()}")



Gen1=Gen()
Gen2=Gen()
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
anailisi.agregar_resultado(Muestra1)
anailisi.agregar_resultado(Muestra1)
anailisi.agregar_resultado(Muestra1)
anailisi.exportar_resultado()
Muestra1.exportar_resultado()