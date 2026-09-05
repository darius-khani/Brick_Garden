import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# Loads home_screen.kv | Register HomeScreen Rule
Builder.load_file(os.path.join(os.path.dirname(__file__), 'home_screen.kv'))    # Strips 'homescreen.py' from path string and replaces it with 'home_screen.kv'

class HomeScreen(Screen):
    pass