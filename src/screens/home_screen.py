import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty

from kivy.vector import Vector
from kivy.clock import Clock

from random import randint

from data.local_data import local_data

# Loads home_screen.kv | Register HomeScreen Rule
Builder.load_file(os.path.join(os.path.dirname(__file__), 'home_screen.kv'))    # Strips 'homescreen.py' from path string and replaces it with 'home_screen.kv'

# HomeScreen Widget
class HomeScreen(Screen):
    def on_enter(self, *args):
        self._update_event = Clock.schedule_interval(self.update, 1.0/60.0)

    def on_leave(self, *args):
        self._update_event.cancel()

    def update(self, dt):
        #local_data.last_pull = now_ms
        pass
    
    vitality = NumericProperty(local_data.vitality)
    plant_name = StringProperty(local_data.plants[0]["name"])
    plant_stage = NumericProperty(int(local_data.plants[0]["stage"]))
    pass


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