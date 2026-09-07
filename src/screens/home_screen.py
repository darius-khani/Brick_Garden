import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty

from data.local_data import local_data

# Loads home_screen.kv | Register HomeScreen Rule
Builder.load_file(os.path.join(os.path.dirname(__file__), 'home_screen.kv'))    # Strips 'homescreen.py' from path string and replaces it with 'home_screen.kv'

# HomeScreen Widget
class HomeScreen(Screen):
    vitality = NumericProperty(10)
    plant_name = StringProperty("monstera")
    plant_stage = NumericProperty(5)
    pass