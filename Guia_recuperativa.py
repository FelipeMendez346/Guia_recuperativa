class Gen():
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

    def print_Gen(self):
        print(f"Nombre: {self.__nombre}. \n longitud: {self.__longitud}. \n Expresion: {self.__expresion}.")    
    
class Analisis():
    def __init__(self):
        self.__resultados=[]
    def agregar_resultado(self,Nuevo_resultado):
            resultados.append(Nuevo_resultado)

class Muestra():
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


