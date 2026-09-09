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

def calculated_bricked_seconds(events, last_pull=None):
    now_ms = time.time() * 1000 # Converting from sec to JavaScript JSON ms

    total_seconds = 0
    previous_timestamp = None   # Update to saved time_stamp in future
    previous_state = "unbricked"

    # If File Has Saved Timestamp
    if last_pull is not None:
        for idx, event in enumerate(reversed(events)):
            if event["timestamp"] <= last_pull:
                # Accounting for index zero in reversed enumerate
                if idx == 0:
                    if event["state"] == "bricked":
                        total_seconds += now_ms - last_pull
                    events = []
                    break
                
                if event["state"] == "bricked":
                    total_seconds += events[idx*-1]["timestamp"] - last_pull
                events = events[idx*-1:]  # events[idx*-1] is the one after event from for loop
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
    num = 2000
    for event in fetch_all_events():
        print(event)
        num -= 1
        if num <=0:
            break
    
    print(calculated_bricked_seconds(fetch_all_events()))
