import pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

class Interfaz_entrada:
    def __init__(self):
        self.diccionario_teclas = dict()
        self.diccionario_eventos = dict()
        
        
    def declarar_pulsacion_tecla(self,key,func):
        self.diccionario_teclas[key]=func
        
    
    def declarar_evento(self,evento,func):
        self.diccionario_eventos[evento]=func
        
    def chequear_eventos(self):
        for event in GAME_EVENTS.get():
            if event.type == pygame.KEYDOWN:
                for tecla in self.diccionario_teclas.keys():
                    if event.key == tecla:
                        self.diccionario_teclas[tecla]()
            for evento in self.diccionario_eventos:
                if evento == event.type:
                    self.diccionario_eventos[evento]()

            
            