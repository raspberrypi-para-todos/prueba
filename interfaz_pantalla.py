import pygame


class Interfaz_pantalla:
    def __init__(self,ventana,carretera,coche):
        self.ventana = ventana
        self.carretera = carretera
        self.coche = coche
        
    def representar_carretera(self):
        for indice in range(0,self.carretera.max_carretera()):
            pygame.draw.rect(self.ventana, (0,255,0), (self.carretera.arcen_izquierdo(indice), indice*10, 10, 10))
            pygame.draw.rect(self.ventana, (0,255,0),  (self.carretera.arcen_derecho(indice), indice*10, 10, 10))
            
    def representar_coche(self):
        pygame.draw.rect(self.ventana, (255,0,0), (self.coche.posX(), self.coche.posY(), self.coche.tamano(), self.coche.tamano()))
        
        
        
    