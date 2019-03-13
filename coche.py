import interfaz_sonido

class Coche:
    def __init__(self,tamanoVentana,tamanoCoche):
        self.posicionX = int(tamanoVentana[0] / 2)
        self.posicionY = tamanoVentana[1] - tamanoCoche * 2
        self.velocidad = 0
        self.ultimoGiro = 0
        self.tamanoCoche = tamanoCoche
        self.__interfaz_sonido = interfaz_sonido.Interfaz_sonido()
    
    def mover(self):   
        self.posicionX += self.velocidad
        
    def girar(self,sentido):
        if self.ultimoGiro != sentido:
            self.__interfaz_sonido.stop_and_play_sound("frenada")
        self.__interfaz_sonido.play_sound("aceleracion")
        self.velocidad += sentido * 2
        
    def posX(self):
        return self.posicionX
    
    def posY(self):
        return self.posicionY
    
    def tamano(self):
        return self.tamanoCoche
        
        