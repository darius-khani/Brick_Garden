from kivy.app import App
from kivy.uix.widget import Widget

# Root Widget
class BrickGarden(Widget):
    pass

# Loads brickgarden.kv | Returns Root Widget
class BrickGardenApp(App):
    def build(self):
        return BrickGarden()

# Runs The Program | python src/main.py
if __name__ == '__main__':
    BrickGardenApp().run()