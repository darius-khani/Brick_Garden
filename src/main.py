from kivy.app import App
from kivy.uix.widget import Widget

class BrickGarden(Widget):
    pass

class BrickGardenApp(App):
    def build(self):
        return BrickGarden()

if __name__ == '__main__':
    BrickGardenApp().run()