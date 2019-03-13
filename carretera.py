from random import randint

class Carretera:
    
    def _reservarCarretera(self):
        for indice in range(0,int(self.altoVentana/10)):
            self.arcenIzquierdo.append(0)
            self.arcenDerecho.append(0)
       
    def __init__(self ,resolucion):
        """
        resolucion: resolucion en pixeles de la pantalla. En una tupla. Siendo el ( ancho , alto )
        """
        # Variables de instancia
        self.arcenIzquierdo = [] # Donde esta el arcen por la izquierda según los recuadros por la Y . El 0 es el superior
        self.arcenDerecho = [] # por la derecha
        self.maxCarretera = 0 # tamaño en recuadros de la carretera
        self.contadorCurva = 0 # contador de veces que está girando en una curva. Desde 5 hasta 0
        self.valorCurvaAnterior = 10 # Valor de giro en las curvas o rectas.
        self.anteriorIzquierda = 1 # ultima posicion x del arcen izquierdo
        self.primera = True  # Es la primera vez que generamos carretera
        self.anchoVentana = resolucion[0] 
        self.altoVentana = resolucion[1]
        self._reservarCarretera()
    
    
    def _aleatorioGiro(self):
        if self.contadorCurva > 0:
            self.contadorCurva -= 1
            return self.valorCurvaAnterior
        valor = randint(0,10)
        if valor < 2 and self.anteriorIzquierda > 140:
            self.valorCurvaAnterior = -10
            self.contadorCurva = 5
            return -10
        elif valor >= 8 and self.anteriorIzquierda < ( self.anchoVentana - 240):
            self.valorCurvaAnterior = 10
            self.contadorCurva = 5
            return 10
        else:
            self.valorCurvaAnterior = 0
            self.contadorCurva = 1
        return 0
    
    def generar_carretera(self):
        if self.primera:
            self.arcenIzquierdo[0]= int(self.anchoVentana/2) - 100
            self.arcenDerecho[0]= int(self.anchoVentana/2) + 100
            self.anteriorIzquierda = self.arcenIzquierdo[0]
            self.maxCarretera = 1
            self.primera = False
        else:
            valorGiro = self._aleatorioGiro()
            self.arcenIzquierdo[0] = self.anteriorIzquierda + valorGiro
            self.anteriorIzquierda = self.arcenIzquierdo[0]
            self.arcenDerecho[0] = self.arcenIzquierdo[0] + 200 + valorGiro
            if self.maxCarretera < int(self.altoVentana / 10):
                self.maxCarretera += 1
                
    def desplazar_carretera(self):
        indice = self.maxCarretera - 1
        while indice > 0:
            self.arcenIzquierdo[indice]= self.arcenIzquierdo[indice -1]
            self.arcenDerecho[indice]= self.arcenDerecho[indice -1]
            indice -= 1
            
    def max_carretera(self):
        return self.maxCarretera
    
    def arcen_izquierdo(self, indice):
        if indice < self.maxCarretera:
            return self.arcenIzquierdo[indice]
        else:
            return 0
        
    def arcen_derecho(self, indice):
        if indice < self.maxCarretera:
            return self.arcenDerecho[indice]
        else:
            return 0
        
        