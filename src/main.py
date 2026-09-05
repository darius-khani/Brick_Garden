# Config Kivy to a IPhone Size Screen
from kivy.config import Config
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '874')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import HomeScreen

# Root Widget - ScreenManager
class BrickGarden(ScreenManager):
    pass

# Loads brickgarden.kv | Returns Root Widget
class BrickGardenApp(App):
    def build(self):
        sm = BrickGarden()
        sm.add_widget(HomeScreen(name='home'))
        return sm

# Runs The Program | python src/main.py
if __name__ == '__main__':
    BrickGardenApp().run()