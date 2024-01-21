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
        width = max(gcon.VSPEED_MAX + 1,xywh[2])
        height = max(gcon.VSPEED_MAX + 1,xywh[3])
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
            maxAttempts = gcon.VSPEED_MAX + 1

            #bounching
            bounceAmount = 0
            if otherPhyBox.GetVelocityMagnitude() >= gcon.WALL_BOUNCE_MIN_VOLOCITY: #if going fast enough
                bounceAmount = gcon.WALL_BOUNCE

            #step backwards untill your free
            exitOn = "non"
            while maxAttempts >= 0:
                #step x
                Left += xVelocity
                Right += xVelocity
                if not self.physicsBox.BoxOverlap((Left, Top, Right, Bottem)):
                    #new placement
                    otherPhyBox.SetVelocityX(-(otherPhyBox.GetVelocityX() * bounceAmount)) #bounce
                    otherPhyBox.SetLeft(Left)
                    otherPhyBox.SetTop(Top)
                    break

                #step y
                Top += yVelocity
                Bottem += yVelocity
                if not self.physicsBox.BoxOverlap((Left, Top, Right, Bottem)):
                    otherPhyBox.SetVelocityY(-(otherPhyBox.GetVelocityY() * bounceAmount)) #bounce
                    #new placement
                    otherPhyBox.SetLeft(Left)
                    otherPhyBox.SetTop(Top)
                    break
                
                #sub failsafe
                maxAttempts -= 1
                #end of step backwards

            #if it failed to get out of the wall reset to checkpoiny
            if maxAttempts < 0:
                otherPhyBox.TeleportToCheckpoint()
     
        #Collide end
                


    def Draw(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        if self.visible:
            #testing
            self.physicsBox.DebugDrawBox(drawToSurface)
        #end of draw