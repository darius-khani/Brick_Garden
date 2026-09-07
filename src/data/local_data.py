import os
import json

from paths import LOCAL_DATA, TEMP_DATA

class LocalData():
    vitality: int
    bricked_time: int
    plants: list

    # Initialize Using Standard Values
    def __init__(self):
        self.getData()

    # Read Data From local_data.json
    def getData(self):
        with open(LOCAL_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.vitality = data["vitality"]
            self.plants = data["plants"]
            self.bricked_time = data["bricked_time"]

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
        print(f"Bricked Time: {self.bricked_time}")
        print("Plants:")
        for plant in self.plants:
            print(f"\tName: {plant["name"].replace("_", " ").title()} Stage: {plant["stage"]}")
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
    data.vitality += 120
    data.updateData()
    data.getData()
    data.printData()
    data.stdReset()