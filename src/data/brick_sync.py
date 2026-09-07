# Lets Python Acess Data from URLS
import requests
import time

FIREBASE_URL = "https://brick-garden-default-rtdb.firebaseio.com/events.json"

# Data Retrieval Function
def fetch_all_events():
    response = requests.get(FIREBASE_URL)
    response.raise_for_status()   # Displays Status if Error
    data = response.json()        # Turns JSON txt into Python Dict

    # No Data Logged
    if data is None:
        return []

    events = list(data.values())   # Convert Dict to Ordered List
    events.sort(key=lambda event: event["timestamp"])   # Sort Events Chronologically
    return events

def calculated_bricked_seconds(events):
    now_ms = time.time() * 1000 # Converting from sec to JavaScript JSON ms

    total_seconds = 0
    previous_timestamp = None   # Update to saved time_stamp in future
    previous_state = "unbricked"

    # If File Has Saved Timestamp
    if previous_timestamp is not None :
        for idx, event in enumerate(reversed(events)):
            if event["timestamp"] == previous_timestamp:
                if idx == 0:
                    events = []
                    break
                events = events[idx*-1:]
                break

    # Add Bricked Time Intervals
    for event in events:
        if previous_state == "bricked" and previous_timestamp is not None:
            total_seconds += event["timestamp"] - previous_timestamp
        previous_timestamp = event["timestamp"]
        previous_state = event["state"]

    # If Phone is still Bricked
    if previous_timestamp is not None and previous_state == "bricked":
        total_seconds += now_ms - previous_timestamp

    # Convert to Seconds and Return
    return total_seconds / 1000

# Test Printing Seconds Since Last Save
if __name__ == "__main__": # Protected from running when imported as __name__ changes from __main__ upon importing
    #for event in fetch_all_events():
        #print(event)
    print(calculated_bricked_seconds(fetch_all_events()))
