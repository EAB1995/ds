from ds_story_nov_2021 import *
from ds_engine_nov_2021 import *
from ds_classes_nov_2021 import *

abbot.add_inventory(slug_pistol)
miller.add_inventory(ray_gun)

abbot.show_inventory()

Choose_Player_Ranged(abbot, miller, engineer, [], None, "seq_2")