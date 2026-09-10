import os
import time

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.properties import ObjectProperty

from random import randint
from kivy.vector import Vector

from data import local_data, Plant

# Keyboard Commands for Testing
from kivy.core.window import Window

# Loads home_screen.kv | Register HomeScreen Rule
Builder.load_file(os.path.join(os.path.dirname(__file__), 'home_screen.kv'))    # Strips 'homescreen.py' from path string and replaces it with 'home_screen.kv'

# USE LAYOUT FOR BUTTONS

# HomeScreen Widget
class HomeScreen(Screen):
    def load_plants(self):
        # Clear old plants
        self.ids.plant_layer.clear_widgets()
        for plant in local_data.plants:
            widget = PlantWidget(plant=plant)
            widget.updateSource()
            self.ids.plant_layer.add_widget(widget)

    def on_enter(self, *args):
        ### TESTING ###
        local_data.stdReset()

        # Load Plants
        self.load_plants()

        # Clocks
        self._update_event = Clock.schedule_interval(self.update, 1.0/20.0)
        self._growthUpdate_event = Clock.schedule_interval(self.growthUpdate, 1)
        self._saveFile_event = Clock.schedule_interval(self.saveFile, 5)

        ### TESTING ###
        Window.bind(on_key_down=self.on_key_down)

    def on_leave(self, *args):
        self._update_event.cancel()
        self._growthUpdate_event.cancel()
        self._saveFile_event.cancel()

        ### TESTING ###
        Window.unbind(on_key_down=self.on_key_down)

    def update(self, dt):

        pass

    def growthUpdate(self, dt):
        for widget in self.ids.plant_layer.children:
            plant = widget.plant
            if plant.data["stage"] < 5:
                old_stage = int(plant.data["stage"])
                plant.data["stage"] += plant.data["growth_rate"] * dt
                # Update Image | Stage Has Incrased
                if plant.data["stage"] - old_stage > 1:
                    widget.updateSource()
                # Stage Max of 5
                if plant.data["stage"] > 5:
                    plant.data["stage"] = 5

        # Update last_pull
        local_data.last_pull = int(time.time() * 1000) # Technically off by dt
        local_data.vitality+=1
        pass

    def saveFile(self, dt):
        local_data.updateData()
        pass

    ### TESTING ###
    def on_key_down(self, window, key, scancode, codepoint, modifier):
        if key == 32:   # spacebar
            local_data.vitality += 10
    pass


class PlantWidget(Image):
    plant = ObjectProperty(None)

    def updateSource(self):
        self.source = "plants/{}_{}.png".format(self.plant.data['name'], int(self.plant.data['stage']))

