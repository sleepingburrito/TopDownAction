import pygame
import gametools
import gameConstants as gcon
import gameTiming as gTim
import gameBoxPhy
import gameUi
#import math

class projectile:

    def ResetWall(self) -> None:
        self.active = False
        self.visible = True

    def __init__(self, xywh: tuple[float, float, float, float], instanceId: int ) -> None:
        self.instanceid = instanceId
        #keep the walls bigger than max velcoity so others cant pass
        width = max(gcon.Z_MAX_VELOCITY + 1,xywh[2])
        height = max(gcon.Z_MAX_VELOCITY + 1,xywh[3])
        self.physicsBox = gameBoxPhy.box((xywh[0],xywh[1],gcon.WALL_DEFAULT_Z),(width,height,gcon.WALL_DEFAULT_ZHEIGHT))
        #reset all other items
        self.ResetWall()
        #end of init