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
                # Force Event | Stage Has Incrased
                if plant.data["stage"] - old_stage > 1:
                    widget.updateSource()
                # Stage Max of 5
                if plant.data["stage"] > 5:
                    plant.data["stage"] = 5

        #if local_data.plants[0].data["stage"] < 5:
        #    old_stage = int(local_data.plants[0].data["stage"])
        #    local_data.plants[0].data["stage"] += local_data.plants[0].data["growth_rate"] * dt
        #    if local_data.plants[0].data["stage"] - old_stage > 1:
        #        # Force Event | Stage Has Increased
        #        local_data.plants[0] = local_data.plants[0]
        #        pass
        #    if local_data.plants[0].data["stage"] > 5:
        #        local_data.plants[0].data["stage"] = 5
        
        # Force Event
        #local_data.plants[0] = local_data.plants[0]

        # Update last_pull
        local_data.last_pull = time.time() * 1000  # Technically off by dt
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







"""
        # Sun
        #Color:
        #    rgba: 0.9, 0.65, 0.3, 1
        #Ellipse:
        #   pos: self.width-170, self.height-90
        #    size: 200, 200

        # Clouds
        #Color:
        #    rgba: 0.85, 0.91, 1, 1
        #Ellipse:
        #    pos: 40, self.height-260
        #    size: 100, 80
        #Ellipse:
        #    pos: 80, self.height-280
        #    size: 160, 120
        #Ellipse:
        #    pos: 180, self.height-260
        #    size: 100, 80
        #Ellipse:
        #    pos: 240, self.height-140
        #    size: 100, 80
        #Ellipse:
        #    pos: 280, self.height-160
        #    size: 160, 120
        #Ellipse:
        #    pos: 380, self.height-140
        #    size: 100, 80
        
        # Clouds
        #Color:
        #    rgba: 0.85, 0.91, 1, 1
        #Ellipse:
        #    pos: 40, self.height-260
        #    size: 100, 80
        #Ellipse:
        #    pos: 80, self.height-280
        #    size: 160, 120
        #Ellipse:
        #    pos: 180, self.height-260
        #    size: 100, 80


        # GreenHouse Floor
        Color:
            rgba: 0.6, 0.42, 0.29, 1
        Quad:
            points:
                [0, tool_bar_height, 
                self.width, tool_bar_height, 
                self.width, floor_height + tool_bar_height, 
                0, floor_height + tool_bar_height]
        Color:
            rgba: 0.2, 0.2, 0.2, 1
        Line:
            points: self.width/2, tool_bar_height, self.width/2, floor_height + tool_bar_height
            width: 2
        Line:
            points: self.width/3, tool_bar_height, self.width/3+20, floor_height + tool_bar_height
            width: 2
        Line:
            points: self.width/6, tool_bar_height, self.width/6+40, floor_height + tool_bar_height
            width: 2
        Line:
            points: self.width/80, tool_bar_height, self.width/80+60, floor_height + tool_bar_height
            width: 2
        Line:
            points: self.width*2/3, tool_bar_height, self.width*2/3-20, floor_height + tool_bar_height
            width: 2
        Line:
            points: self.width*5/6, tool_bar_height, self.width*5/6-40, floor_height + tool_bar_height
            width: 2
        Line:
            points: self.width*79/80, tool_bar_height, self.width*79/80-60, floor_height + tool_bar_height
            width: 2

        # GreenHouse Wall
        Color:
            rgba: 1, 1, 1, 0.5
        Rectangle:
            pos: 0, floor_height + tool_bar_height
            size: self.width, greenhouse_height

        # GreenHouse Roof
        Color:
            rgba: 0, 1, 0.7, 0.3
        Rectangle:
            pos: 0, greenhouse_height*4/5 + floor_height + tool_bar_height
            size: self.width, greenhouse_height/5

        #GreenHouse Roof Frame
        Color:
            rgba: 0.25, 0.15, 0.08, 1
        Line:
            points: 0, greenhouse_height + floor_height + tool_bar_height, self.width, greenhouse_height + floor_height + tool_bar_height
            width: 10
        Line:
            points: self.width/3, greenhouse_height*4/5 + floor_height + tool_bar_height, self.width/3+50, greenhouse_height + floor_height + tool_bar_height
            width: 10
        Line:
            points: self.width*2/3, greenhouse_height*4/5 + floor_height + tool_bar_height, self.width*2/3+50, greenhouse_height + floor_height + tool_bar_height
            width: 10
        Line:
            points: 0, greenhouse_height*4/5 + floor_height + tool_bar_height, 0+50, greenhouse_height + floor_height + tool_bar_height
            width: 10
        Line:
            points: self.width, greenhouse_height*4/5 + floor_height + tool_bar_height, self.width+50, greenhouse_height + floor_height + tool_bar_height
            width: 10

        # GreenHouse Wall Frame
        Color:
            rgba: 0.4, 0.26, 0.13, 1
        Line:
            rectangle: 10, floor_height + tool_bar_height, self.width-20, greenhouse_height*4/5
            width: 10
        Line:
            points: self.width/3, floor_height + tool_bar_height, self.width/3, greenhouse_height*4/5 + floor_height + tool_bar_height
            width: 10
        Line:
            points: self.width*2/3, floor_height + tool_bar_height, self.width*2/3, greenhouse_height*4/5 + floor_height + tool_bar_height
            width: 10
        Line:
            points: -30, floor_height + tool_bar_height, self.width+30, floor_height + tool_bar_height
            width: 10

"""