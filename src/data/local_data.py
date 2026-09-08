import os
import json

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

    # Initialize Using Standard Values
    def __init__(self):
        # Pull From local_data.json
        self.getData()

        # Pull From FireBase
        events = brick_sync.fetch_all_events()

        self.bricked_time = brick_sync.calculated_bricked_seconds(events)
        if events[-1]["state"] == "bricked": self.bricked = True
        else: self.bricked = False

    # Read Data From local_data.json
    def getData(self):
        with open(LOCAL_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.vitality = data["vitality"]
            self.plants = data["plants"]
            self.last_pull = data["last_pull"]

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

    def printData(self):
        print(f"\nVitality: {self.vitality}")
        print(f"Bricked: {self.bricked}")
        print(f"Bricked Time: {self.bricked_time}")
        print("Plants:")
        for plant in self.plants:
            print(f"\tName: {plant["name"].replace("_", " ").title()}Stage: {plant["stage"]}")
        print()



    ### FOR TESTING ###

    # Reset to Standard Testing Save File
    def stdReset(self):
        with open(TEMP_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
        for key in data:
            setattr(self, key, data[key])
        with open(LOCAL_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)   

# Universal Data
local_data = LocalData()

if __name__ == "__main__":
    data = LocalData()
    data.printData()
    #data.vitality += 120
    data.updateData()
    data.getData()
    data.printData()
    data.stdReset()