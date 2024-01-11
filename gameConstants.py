import math
import os
from enum import IntEnum
from enum import Enum
from enum import auto

#app info
#======================
GAME_NAME = "Top Down Action"
GAME_VERSION = "0.0.0"


#game units screen size
#========================
SCREEN_WIDTH_PIXELS = 960
SCREEN_HEIGHT_PIXELS = 540



#time/timer
#========================
TICK_RATE = 60 #refresh rate
MILLISECONDS_IN_SECOND = 1000
MILLISECONDS_IN_TICK = MILLISECONDS_IN_SECOND / TICK_RATE
TICKS_IN_MILLISECOND = TICK_RATE / MILLISECONDS_IN_SECOND
#timer
TIMER_MAX_VALUE_MILLISECONDS = MILLISECONDS_IN_SECOND * 60 * 60 #1 hour
TIMER_MAX_TICKS = math.trunc(TIMER_MAX_VALUE_MILLISECONDS * TICKS_IN_MILLISECOND)


#map
#=================

#tile units map
#MAP_TILE_SIZE = 32 #pixels
#MAP_TILE_WIDTH_SCREEN = SCREEN_WIDTH_PIXELS // MAP_TILE_SIZE
#MAP_TILE_HEIGHT_SCREEN = SCREEN_HEIGHT_PIXELS // MAP_TILE_SIZE


#etc
#=====================
ID_NON = -1 #universal blank id

class DIRECTIONS(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    LEFT = auto()
    UP = auto() #top
    RIGHT = auto()
    DOWN = auto() #bottom

RANDOM_MAX = 1000 

#math
#========================
ANGLE_UP = math.radians(180)
ANGLE_DOWN = 0
ANGLE_LEFT = math.radians(270)
ANGLE_RIGHT = math.radians(90)

ANGLE_DOWN_RIGHT = math.radians(45)
ANGLE_UP_RIGHT = math.radians(135)
ANGLE_UP_LEFT = math.radians(225)
ANGLE_DOWN_LEFT = math.radians(315)


#physics
#======================
#max values are all in a single tick
VSPEED_MAX = 32
ACCELERATION_MAX = VSPEED_MAX / 2
SPEED_MIN_ANY = 0.0001 #speeds less than this get rounded down, per axis for ACCELERATION and velocity

#values are in per millisecond, always postive values
FRICTION_AIR_PERCENTAGE = 1 - (MILLISECONDS_IN_TICK * 0.0012) # how much you want it to go down divided by the time in a tick. only want to take 0.01% away, so 0.01/8.333 = 0.0012
FRICTION_GROUND_PERCENTAGE = MILLISECONDS_IN_TICK * 0.01

#max x/y size
PHY_MIN_WIDTH = 1
PHY_MAX_WIDTH = SCREEN_WIDTH_PIXELS
PHY_MIN_HIEGHT = 1
PHY_MAX_HIEGHT = SCREEN_HEIGHT_PIXELS

#z axis stuff
GRAVITY_ACCELERATION = MILLISECONDS_IN_TICK * 0.005
Z_MAX_ACCELERATION = ACCELERATION_MAX
Z_MAX_VELOCITY = VSPEED_MAX
Z_MIN = 0
Z_MAX = 100
ZHIEGHT_MIN = 1
ZHEIGHT_MAX = Z_MAX

#player
#=============================
class PLAYER_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    ONE = auto()
    TWO = auto()

PLAYER_SIZE = 32
PLAYER_MAX_HP = 100

#z overlap
Z_UNDER = -1
Z_OVERLAP = 0
Z_ONTOP = 1

#active objects
#=============================
WALKING_SPEED = MILLISECONDS_IN_TICK * 0.1
WALKING_SPEED_MAX = MILLISECONDS_IN_TICK * 0.5



#input
#=============================
class INPUT_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    START = auto()
    BACK = auto()
    ACTION = auto()
    CHARGE_SHOOT = auto()
    PLACE_HOLDER1 = auto()
    PLACE_HOLDER2 = auto()
    PLACE_HOLDER3 = auto()
    PLACE_HOLDER4 = auto()
    PLACE_HOLDER5 = auto()
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


#graphics
#=============================
DEBUG_BOX_COLOR = "red"
DEBUG_BOX_WIDTH = 1
DEBUG_SHADOW_COLOR = "blue"

DEFAULT_BG_COLOR = "black"



#sound
#======================
""" SOUND_FADEIN_MS = 500
SOUND_FADEOUT_MS = 500

class SOUND_TYPE_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    EFFECT = auto()
    MUSIC = auto()


BASE_SOUND_LOCATION = "sound"
BASE_SOUND_EFFECT_LOCATION = "effects"
BASE_SOUND_MUSIC_LOCATION = "music"
class SOUND_ID(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    #id, type, file name
    #effects
    TEST0 = (auto(), SOUND_TYPE_ID.EFFECT.value, "se1.ogg")
    TEST1 = (auto(), SOUND_TYPE_ID.EFFECT.value, "se2.ogg")
    #music
    MTEST0 = (auto(), SOUND_TYPE_ID.MUSIC.value, "test1.ogg")
    MTEST1 = (auto(), SOUND_TYPE_ID.MUSIC.value, "test2.ogg") """

