import os
import json

class LocalData():
    vitality = 0
    bricked_time = 0
    plants = []

    # Initialize Using local_data.json
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), "local_data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
            self.vitality = data["vitality"]
            self.plants = data["plants"]
            self.bricked_time = data["bricked_time"]

    def getData(self):
        with open(os.path.join(os.path.dirname(__file__), "local_data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
            self.vitality = data["vitality"]
            self.plants = data["plants"]
            self.bricked_time = data["bricked_time"]

    def updateData(self):
        # Read Old Data
        with open(os.path.join(os.path.dirname(__file__), "local_data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)

        # Update Values
        for key in data:
            data[key] = getattr(self, key)

        # Update File
        with open(os.path.join(os.path.dirname(__file__), "local_data.json"), "w", encoding="utf-8") as file:
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
        with open(os.path.join(os.path.dirname(__file__), "temp_data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
        for key in data:
            setattr(self, key, data[key])
        with open(os.path.join(os.path.dirname(__file__), "local_data.json"), "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)   

if __name__ == "__main__":
    data = LocalData()
    data.printData()
    data.vitality += 120
    data.updateData()
    data.getData()
    data.printData()
    data.stdReset()