import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import interfaz_teclado
import interfaz_pantalla
import carretera
import coche
import logica_juego

pygame.init()

anchoVentana = 500
altoVentana = 500
velocidad_refresco = 10
resolucion = (anchoVentana, altoVentana)
clock = pygame.time.Clock()

ventana = pygame.display.set_mode(resolucion)
pygame.display.set_caption('POO')

entrada_teclado = interfaz_teclado.Interfaz_entrada()

def salir():
    pygame.quit()
    sys.exit()
    
def izquierda():
    coche.girar(-1)
    
def derecha():
    coche.girar(1)

entrada_teclado.declarar_evento(GAME_GLOBALS.QUIT,salir)
entrada_teclado.declarar_pulsacion_tecla(pygame.K_LEFT,izquierda)
entrada_teclado.declarar_pulsacion_tecla(pygame.K_RIGHT,derecha)
entrada_teclado.declarar_pulsacion_tecla(pygame.K_ESCAPE,salir)

carretera = carretera.Carretera(resolucion)
coche = coche.Coche(resolucion,20)
presentacion = interfaz_pantalla.Interfaz_pantalla(ventana,carretera,coche)
logica = logica_juego.Logica_juego(ventana,carretera,coche,resolucion)

while True:
    ventana.fill((0,0,0))
    carretera.generar_carretera()
    carretera.desplazar_carretera()
    presentacion.representar_carretera()
    presentacion.representar_coche()
    
    coche.mover()
    
    clock.tick(velocidad_refresco)
    pygame.display.update()
    
    logica.control_bordes()
    
    entrada_teclado.chequear_eventos()