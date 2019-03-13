class Assets:
    class __Assets:
        """
        Haciendo uso del patrón Singleton se establece el directorio raiz donde estan los assets con una clase privada
        """
        def __init__(self,assets_directory):
            self.dir=assets_directory
        def __str__(self):
            return self.dir
    
    instance = None
    def __init__(self,assets_directory):
        if not Assets.instance:
            Assets.instance = Assets.__Assets(assets_directory)
        else:
            Assets.instance.dir = assets_directory
        
    def new_asset_dir_and_file(self,directorio_base,fichero):
        return Assets.instance.dir+"/"+directorio_base+"/"+fichero
    
    def new_asset_file(self,fichero):
        return Assets.instance.dir+"/"+fichero