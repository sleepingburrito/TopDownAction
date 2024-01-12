import pygame
import gametools
import gameConstants as gcon
import gameTiming as gTim
import gameBoxPhy
import gameInput


class player:

    #controls
    def RestAllKeys(self) -> None:
        self.upKey = 0
        self.downKey = 0
        self.leftKey = 0
        self.rightKey = 0

    def UpdateKeys(self) -> None:
        #takes a snapshot of current key state if you are able to use keys
        if not self.IsStunned():
            self.upKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.UP].InputTime()
            self.downKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.DOWN].InputTime() 
            self.leftKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.LEFT].InputTime()
            self.rightKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.RIGHT].InputTime()
        else:
            self.RestAllKeys()


    #etc
    def Reset(self) -> None:
        self.hp = gcon.PLAYER_MAX_HP
        self.blockControl = False
        self.RestAllKeys()

        #timing reset/set
        for timeTmp in self.timers:
            timeTmp.FullReset()
        #default timer vaules
            
        #end of reset

    def __init__(self, playerId: gcon.PLAYER_ID ) -> None:
        self.playerId = playerId
        self.physicsBox = gameBoxPhy.box((300,100,0),(gcon.PLAYER_SIZE,gcon.PLAYER_SIZE,0))

        #timing init
        self.timers: list[gTim.GameTimer] = []
        for timeTmp in gcon.PLAYER_TIMER:
            self.timers.append(gTim.GameTimer(0))
        
        #end reset/everything else
        self.Reset()
        #end of init

    def IsStunned(self) -> None:
        return self.blockControl or not self.timers[gcon.PLAYER_TIMER.STUN].IsDone()

    #tick actions
    def Tick(self) -> None:
        self.UpdateKeys()
        self.TickMove()
        self.physicsBox.PhysicsTick()



        #end of Tick

    def TickMove(self) -> None:
        xspeed = self.physicsBox.GetVelocityX()
        yspeed = self.physicsBox.GetVelocityY()
        speed = self.physicsBox.GetVelocityMagnitude()

        #up
        if (
            self.upKey > 0
            ):
            self.physicsBox.SetAccelerationMagnitudeRelative(gcon.ANGLE_UP, gcon.PLAYER_WALKING_SPEED)
        #down
        if (
            self.downKey > 0
            ):
            self.physicsBox.SetAccelerationMagnitudeRelative(gcon.ANGLE_DOWN, gcon.PLAYER_WALKING_SPEED)
        #left
        if (
            self.leftKey > 0
            ):
            self.physicsBox.SetAccelerationMagnitudeRelative(gcon.ANGLE_LEFT, gcon.PLAYER_WALKING_SPEED)
        #right
        if (
            self.rightKey > 0
            ):
            self.physicsBox.SetAccelerationMagnitudeRelative(gcon.ANGLE_RIGHT, gcon.PLAYER_WALKING_SPEED)

        #end tick walk

    #draw
    def Draw(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        self.physicsBox.DebugDrawBox(drawToSurface)


