import os

SRC_DIR    = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SRC_DIR, "assets")
DATA_DIR   = os.path.join(SRC_DIR, "data")

LOCAL_DATA = os.path.join(DATA_DIR, "local_data.json")
TEMP_DATA  = os.path.join(DATA_DIR, "temp_data.json")