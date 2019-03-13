import assets
import pygame

class Interfaz_sonido:
    def __init__(self):
        pygame.mixer.init()
        self.assets = assets.Assets("./assets")
        self.sounds = dict()
        self._prepare_sounds()
        
    def _prepare_sounds(self):
        self.sounds["aceleraracion"] = pygame.mixer.Sound(self.assets.new_asset_dir_and_file("sounds/ogg","aceleracion.ogg"))
        self.sounds["frenada"] = pygame.mixer.Sound(self.assets.new_asset_dir_and_file("sounds/ogg","frenada.ogg"))
        self.sounds["explosion"] = pygame.mixer.Sound(self.assets.new_asset_dir_and_file("sounds/ogg","explosion.ogg"))
        
    def stop_and_play_sound(self, which_sound):
        pygame.mixer.stop()
        self.play_sound(which_sound)
    
    def play_sound(self,which_sound):
        if which_sound in self.sounds: # Comprobamos si existe el sonido
            self.sounds[which_sound].play()
        

        
