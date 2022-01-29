from ds_story_nov_2021 import *
from ds_engine_nov_2021 import *
from ds_classes_nov_2021 import *

def take_in(accept):
    choice = input("--[").upper()
    if choice in accept:
        return
    else:
        prt_txt(f"INPUT NOT RECOGNISED.\nACCEPTED INPUTS: {accept.upper()}")

take_in("A / B")
