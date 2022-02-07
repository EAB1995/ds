from ds_story_nov_2021 import *
from ds_engine_nov_2021 import *
from ds_classes_nov_2021 import *
from ds_logging import *

logger.setLevel(logging.INFO)

player_1 = abbot
player_2 = miller

abbot.add_inventory(slug_pistol)
miller.add_inventory(ray_gun)
miller.add_inventory(battle_rifle)

seq_2(player_1, player_2)
