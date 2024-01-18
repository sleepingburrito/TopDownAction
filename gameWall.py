import pygame
import gametools
import gameConstants as gcon
#import gameTiming as gTim
import gameBoxPhy
import gameUi
#import math

#test wall ids
# _nextWallId = -1
# def GetNextWallId() -> int:
#     global _nextWallId
#     _nextWallId += 1
#     return _nextWallId

class wall:

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

    def Collide(self, otherPhyBox: gameBoxPhy.box) -> None:
        if otherPhyBox.BoxOverlap(self.physicsBox.GetLTRB()):
            
            #velocity
            velocitySigns = otherPhyBox.PhysicsLastTickVelocity() #get which dir other is moving
            #find which way to step backwards
            xVelocity = -gametools.ClampValue(velocitySigns[0], -1, 1)
            yVelocity = -gametools.ClampValue(velocitySigns[1], -1, 1)
            
            #get where other is at
            otherLTRB = otherPhyBox.GetLTRB()
            #brake it down to its parts
            Left = otherLTRB[0]
            Right = otherLTRB[2]
            Top = otherLTRB[1]
            Bottem = otherLTRB[3]
            
            #fail safe
            maxAttempts = max(abs(xVelocity), abs(yVelocity)) + 1

            #step backwards untill your free
            while maxAttempts >= 0:
                #test x
                Left += xVelocity
                Right += xVelocity
                if not self.physicsBox.BoxOverlap((Left, Top, Right, Bottem)):
                    otherPhyBox.SetLeft(Left)
                    otherPhyBox.SetTop(Top)
                    otherPhyBox.SetVelocityX(-(otherPhyBox.GetVelocityX() * gcon.WALL_BOUNCE))
                    break

                #test y
                Top += yVelocity
                Bottem += yVelocity
                if not self.physicsBox.BoxOverlap((Left, Top, Right, Bottem)):
                    otherPhyBox.SetLeft(Left)
                    otherPhyBox.SetTop(Top)
                    otherPhyBox.SetVelocityY(-(otherPhyBox.GetVelocityY() * gcon.WALL_BOUNCE))
                    break
                
                #sub failsafe
                maxAttempts -= 1

            #if it failed to get out
            if maxAttempts < 0:
                otherPhyBox.TeleportToCheckpoint()
                otherPhyBox.ResetAccelerationAndVelocity()
                


    def Draw(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        if self.visible:
            #testing
            self.physicsBox.DebugDrawBox(drawToSurface)
        #end of draw