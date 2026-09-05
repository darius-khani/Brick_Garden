# Config Kivy to standard IPhone Screen Size
from kivy.config import Config
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '874')   # Yes, it really is that long
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import HomeScreen

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
if __name__ == '__main__':
    BrickGardenApp().run()