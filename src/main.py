# Config Kivy to standard IPhone Screen Size
from kivy.config import Config
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '874')   # Yes, it really is that long
Config.set('graphics', 'resizable', False)

# Kivy 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

# Screens
from screens import HomeScreen

# Path Set Up
import os
from paths import *

### MUST BE DONE BEFORE APP LOADS ###

# Load Universal Data Object
from data.local_data import local_data

#####################################

# Add Resource Path for Kivy
from kivy.resources import resource_add_path
resource_add_path(ASSETS_DIR)

# Register Fonts
LabelBase.register(name='IndieFlower', fn_regular=os.path.join(ASSETS_DIR, 'fonts/Indie_Flower/IndieFlower-Regular.ttf'))
LabelBase.register(name='NanumBrush', fn_regular=os.path.join(ASSETS_DIR, 'fonts/Nanum_Brush_Script/NanumBrushScript-Regular.ttf'))
LabelBase.register(name='PixelifySans', fn_regular=os.path.join(ASSETS_DIR, 'fonts/Pixelify_Sans/PixelifySans-Regular.ttf'))

# Builds App | Creates ScreenManager | Loads brickgarden.kv
class BrickGardenApp(App):
    def build(self):
        sm = BrickGarden()

        #List of Screens
        sm.add_widget(HomeScreen(name='home'))   # Automatically Displays First Listed
        #sm.add_widget(Breathing(name='breathing'))
        return sm


# Root Widget | Extends ScreenManager
class BrickGarden(ScreenManager):
    pass

# Runs The Program | python src/main.py
if __name__ == '__main__': # Protected from running when imported
    BrickGardenApp().run()