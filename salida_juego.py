import pygame, sys
import interfaz_teclado
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import interfaz_sonido

class Salida_juego:
    def __init__(self,ventana,tamano_ventana):
        self.ventana = ventana
        self.anchoVentana = tamano_ventana[0]
        self.altoVentana = tamano_ventana[1]
        self.__interfaz_sonido = interfaz_sonido.Interfaz_sonido()       
            
    def _salir(self):
        pygame.quit()
        sys.exit()
    
    def fin_partida(self):
        self.__interfaz_sonido.stop_and_play_sound("explosion")
        pygame.font.init()
        mifuente = pygame.font.SysFont('Comic Sans MS', 100)
        ventanaDeTexto = mifuente.render('Game over!', False, (0, 0, 255 ))
        self.ventana.blit(ventanaDeTexto,(int(self.anchoVentana/2)-200,int(self.altoVentana/2)-50))
        pygame.display.update()
        interfaz_de_fin_juego = interfaz_teclado.Interfaz_entrada()
        
        while True:
            for event in GAME_EVENTS.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._salir()

                if event.type == GAME_GLOBALS.QUIT:
                    self._salir()


        