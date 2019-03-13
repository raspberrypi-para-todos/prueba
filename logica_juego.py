import salida_juego

class Logica_juego:
    def __init__(self , ventana, carretera ,coche ,tamanoVentana):
        self.ventana = ventana
        self.carretera = carretera
        self.coche = coche
        self.tamanoVentana = tamanoVentana # tamanoVentana es una tupla con ( ancho , alto )
        
    def _finJuego(self):
        salida = salida_juego.Salida_juego ( self.ventana , self.tamanoVentana )
        salida.fin_partida()     
       
    def _borde_izquierdo(self):
        return self.coche.posX() < ( self.carretera.arcen_izquierdo(self.carretera.max_carretera() - 2) + 20 )
    
    def _borde_derecho(self):
        return self.coche.posX() >= ( self.carretera.arcen_derecho(self.carretera.max_carretera() - 2 ) - 20 )
    
    def control_bordes(self):
        maximoPosible = self.tamanoVentana[1] / 10
        if self.carretera.max_carretera() == maximoPosible:
            if self._borde_izquierdo() or self._borde_derecho() :
                self._finJuego()
        