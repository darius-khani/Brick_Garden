import os
import json
import time

from paths import LOCAL_DATA, TEMP_DATA

from data import brick_sync

class LocalData():
    # Local Data
    last_pull: int
    vitality: int
    plants: list

    # Brick Synced Data
    bricked_time: int
    bricked: bool

    # Testing
    manual_override = True
    manual_bricked = True
    manual_bricked_time = 1788907085451

    # Initialize Using Standard Values
    def __init__(self):
        # Pull From local_data.json
        self.getData()

        # Pull From FireBase
        events = brick_sync.fetch_all_events()

        self.bricked_time = brick_sync.calculated_bricked_seconds(events, self.last_pull)
        
        if events[-1]["state"] == "bricked": self.bricked = True
        else: self.bricked = False

        # Update last_pull to current time in ms
        self.last_pull = time.time() * 1000


    # Read Data From local_data.json
    def getData(self):
        with open(LOCAL_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.last_pull = data["last_pull"]
            self.vitality = data["vitality"]
            self.plants = data["plants"]

    # Update Data on local_data.json
    def updateData(self):
        # Read Old Data
        with open(LOCAL_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Update Values
        for key in data:
            data[key] = getattr(self, key)

        # Update File
        with open(LOCAL_DATA, "w", encoding="utf-8") as file:
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
            setattr(self, key, data[key])
        with open(LOCAL_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)   


# Universal Data Import
local_data = LocalData()

if __name__ == "__main__":
    data = LocalData()
    data.printData()
    #data.vitality += 120
    data.updateData()
    #data.getData()
    data.printData()
    #data.stdReset()