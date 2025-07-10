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
    def get_nombre(self):
        return self.__expresion
    

