import os
import json
import time
from datetime import datetime

from paths import LOCAL_DATA, BACKUP_DATA, TEMP_DATA

from data import fetch_all_events, calculated_bricked_seconds

from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, StringProperty, DictProperty


class LocalData(EventDispatcher):
    # Local Data
    last_pull: int                  # Last Time App was Open
    vitality = NumericProperty(0)   # Vitality i.e. Currency
    plants = []                     # List of Dictionaries of User's plants

    # Brick Synced Data
    bricked_time: int               # Time phone was bricked since last opened
    bricked: bool                   # Current Brick Status

    # Local Time
    curr_time = StringProperty("")  # Current Time

    # Testing
    #manual_override = True
    #manual_bricked = True
    #manual_bricked_time = 1788907085451

    # On Launch: Pull Local Data and Pull from FireBase | Calculate Bricked Time
    def __init__(self):
        # Inherit from EventDispacher
        super().__init__()

        # Pull From local_data.json
        try:
            self.getData()
        except:
            self.getBackUpData()

        # Load Current Time
        self.curr_time = datetime.now().strftime("%I:%M")

        # Pull From FireBase
        events = fetch_all_events()

        ### TESTING ###
        self.stdReset()
        self.last_pull = int(time.time() * 1000) - 0000

        # Calculate bricked_time lapsed | Add to each plant
        self.bricked_time = calculated_bricked_seconds(events, self.last_pull)
        for plant in self.plants:
            #print(f"{plant.data['name'].title()}: {plant.data["stage"] + self.bricked_time * plant.data["growth_rate"]}")
            plant.data["stage"] += self.bricked_time * plant.data["growth_rate"]

        if events[-1]["state"] == "bricked": self.bricked = True
        else: self.bricked = False

        # Update last_pull to current time in ms and write to local_data.json
        self.last_pull = int(time.time() * 1000)

        self.updateData()

    # Read Data From local_data.json
    def getData(self):
        with open(LOCAL_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.last_pull = data["last_pull"]
            self.vitality = data["vitality"]
            self.plants = [Plant(data=plant) for plant in data["plants"]]

    # Update Data on local_data.json
    def updateData(self):
        # Pull Old Data
        with open(LOCAL_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Update Values
        for key in data:
            if key == "plants":
                data["plants"] = [dict(plant.data) for plant in self.plants]
                continue
            data[key] = getattr(self, key)

        # Update File
        with open(LOCAL_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    # Read Data From backup_data.json
    def getBackUpData(self):
        # Pull Backup Data
        with open(BACKUP_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.last_pull = data["last_pull"]
            self.vitality = data["vitality"]
            self.plants = [Plant(data=plant) for plant in data["plants"]]
        
        # Update File
        with open(LOCAL_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    # Backup Data on backup_data.json
    def backUpData(self):
        # Pull Old Data
        with open(BACKUP_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
    
        # Update Values
        for key in data:
            if key == "plants":
                data["plants"] = [dict(plant.data) for plant in self.plants]
                continue
            data[key] = getattr(self, key)
    
        # Update File
        with open(BACKUP_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)


    ### FOR TESTING ###

    # Print Data
    def printData(self):
        print(f"\nBrick Synced: \n\tBricked: {self.bricked} \n\tBricked Time: {self.bricked_time}")
        print(f"\nLocal Data: \n\tLast Pull: {self.last_pull} \n\tVitality: {self.vitality}")
        print("\tPlants:")
        for plant in self.plants:
            print(f"\t\tName: {plant["name"].replace("_", " ").title()}Stage: {plant["stage"]}")
        print()

    # Reset to Standard Testing Save File
    def stdReset(self):
        with open(TEMP_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
        for key in data:
            if key == "plants":
                self.plants = [Plant(data=plant) for plant in data["plants"]]
                continue
            setattr(self, key, data[key])
        with open(LOCAL_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

class Plant(EventDispatcher):
    data = DictProperty({})



# Universal Data Import
local_data = LocalData()

if __name__ == "__main__":
    local_data.printData()
    #local_data.stdReset()