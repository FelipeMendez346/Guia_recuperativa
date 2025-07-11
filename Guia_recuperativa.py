from abc import abstractclassmethod
from abc import ABCMeta

class EntidadBiologica(metaclass=ABCMeta):
    @abstractclassmethod
    def Procesar(self):
        pass


class Gen(EntidadBiologica):
    def __init__(self):
        self.__nombre=None
        self.__longitud=0
        self.__expresion=None
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
    def set_expresion(self,Nueva_expresion):
        if isinstance(Nueva_expresion,str):
            self.__expresion=Nueva_expresion
    def get_expresion(self):
        return self.__expresion

    def obtener_info(self):
        return self.__nombre,self.__longitud,self.__expresion

    def Procesar(self):
        print(f"Nombre: {self.__nombre}. \n longitud: {self.__longitud}. \n Expresion: {self.__expresion}.")    
    
class Analisis(EntidadBiologica):
    def __init__(self):
        self.__resultados=[]
        self.__nombre=None
    def agregar_resultado(self,*Nuevo_resultado):
            resultados.append(Nuevo_resultado)
    def Procesar(self):
        n=1
        print(f"Nombre de los analisis: {self.__nombre} \n")
        for resultado in __resultados:
            print(f"{n}.{resultado}")
            n+=1

class Muestra(EntidadBiologica):
    def __init__(self):
        self.__nombre=None
        self.__Genes=[]
    def agregar_Gen(self,Nuevo_gen):
        if isinstance(Nuevo_gen,Gen):
            if Nuevo_gen in self.__Genes:
                return
            else:
                self.__Genes.append(Nuevo_gen)
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,Nuevo_nombre):
        if isinstance(Nuevo_nombre,str):
            self.__nombre=Nuevo_nombre
        else:
            print("Error a ingresar nuevo nombre a la muestra")
    def Procesar(self):
        print(f"Nombre de muestra {self.__nombre} \n")
        for Gen in self.__Genes:
            Gen.Procesar()



Gen1=Gen()
Gen2=Gen()
Gen1.set_nombre("Genn1")
Gen2.set_nombre("Genn2")
Gen1.set_longitud(3)
Gen2.set_longitud(3)
Gen1.set_expresion("AGT")
Gen2.set_expresion("ATC")
Muestra1=Muestra()
Muestra1.set_nombre("Numero uno")
Muestra1.agregar_Gen(Gen1)
Muestra1.agregar_Gen(Gen2)
Muestra1.agregar_Gen(Gen1)
Muestra1.Procesar()
