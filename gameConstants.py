import math
import os
from enum import IntEnum
from enum import Enum
from enum import auto

#app info
#======================
GAME_NAME = "Top Down Action"
GAME_VERSION = "0.0.0"
GAME_DEBUG = True


#game units screen size
#========================
SCREEN_WIDTH_PIXELS = 960
SCREEN_HEIGHT_PIXELS = 540
SCREEN_WIDTH_PIXELS_HALF = SCREEN_WIDTH_PIXELS / 2
SCREEN_HEIGHT_PIXELS_HALF = SCREEN_HEIGHT_PIXELS / 2


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
    UP = auto() #top
    DOWN = auto() #bottom
    LEFT = auto()
    RIGHT = auto()
    DOWN_RIGHT = auto()
    UP_RIGHT = auto()
    UP_LEFT = auto()
    DOWN_LEFT = auto()
    


RANDOM_MAX = 1000 

#math
#========================
ANGLE_NON = -1
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
SPEED_MIN_ANY = 0.01 #speeds less than this get rounded down, per axis for ACCELERATION and velocity

#values are in per millisecond, always postive values
FRICTION_AIR_PERCENTAGE = 1 - (MILLISECONDS_IN_TICK * 0.00025) # how much you want it to go down divided by the time in a tick. only want to take 0.01% away, so 0.01/8.333 = 0.0012
FRICTION_GROUND_PERCENTAGE = 1 - (MILLISECONDS_IN_TICK * 0.0018)

#max x/y size
PHY_MIN_WIDTH = 1
PHY_MAX_WIDTH = SCREEN_WIDTH_PIXELS
PHY_MIN_HIEGHT = 1
PHY_MAX_HIEGHT = SCREEN_HEIGHT_PIXELS

#z axis stuff
GRAVITY_ACCELERATION = MILLISECONDS_IN_TICK * 0.01
Z_MAX_ACCELERATION = ACCELERATION_MAX
Z_MAX_VELOCITY = VSPEED_MAX
Z_MIN = 0
Z_CEILING_BOUNCE = 0.5 #how much velocity is lost after hitting celing 
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

class PLAYER_TIMER(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    #it, value in milliseconds
    STUN = auto()
    JUMP_TIMING = auto() #grace period

PLAYER_SIZE = 32
PLAYER_MAX_HP = 100

#z overlap
Z_UNDER = -1
Z_OVERLAP = 0
Z_ONTOP = 1

PLAYER_JUMP_AMOUNT = MILLISECONDS_IN_TICK * 0.13
PLAYER_JUMP_INPUT_TIMING = 34 #in ms

PLAYER_WALKING_SPEED = MILLISECONDS_IN_TICK * 0.01
PLAYER_WALKING_SPEED_MAX = MILLISECONDS_IN_TICK * 1


#walls
#=============================
WALL_DEFAULT_ZHEIGHT = Z_MAX
WALL_DEFAULT_Z = Z_MIN



#input
#=============================
class INPUT_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    START = auto()
    BACK = auto()
    ACTION = auto()
    JUMP = auto()
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


