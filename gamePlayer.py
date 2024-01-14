import pygame
import gametools
import gameConstants as gcon
import gameTiming as gTim
import gameBoxPhy
import gameInput
import gameUi


class player:

    #controls
    def RestAllKeys(self) -> None:
        #movement
        self.upKey = 0
        self.downKey = 0
        self.leftKey = 0
        self.rightKey = 0
        #diagonal
        self.upLeft = 0
        self.upRight = 0
        self.downLeft = 0
        self.downRight = 0

    def UpdateKeys(self) -> None:
        #takes a snapshot of current key state if you are able to use keys
        self.RestAllKeys()

        if not self.IsStunned():
            #starting key states
            self.upKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.UP].InputTime()
            self.downKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.DOWN].InputTime() 
            self.leftKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.LEFT].InputTime()
            self.rightKey = gameInput.AllUserInput[gcon.PLAYER_ID.ONE][gcon.INPUT_ID.RIGHT].InputTime()
            #d-pad like lockout
            if self.upKey > 0 and self.downKey > 0:
                self.upKey = 0
                self.downKey = 0
            if self.leftKey > 0 and self.rightKey > 0:
                self.leftKey = 0
                self.rightKey = 0
            #diagonal
            self.upRight = 0
            self.upLeft = 0
            if self.upKey > 0:
                if self.rightKey > 0:
                    self.upRight = min(self.upKey, self.rightKey)
                elif self.leftKey > 0:
                    self.upLeft = min(self.upKey, self.leftKey)
            self.downRight = 0
            self.downLeft = 0
            if self.downKey > 0:
                if self.rightKey > 0:
                    self.downRight = min(self.downKey, self.rightKey)
                elif self.leftKey > 0:
                    self.downLeft = min(self.downKey, self.leftKey)
        
        #update key
            

    #etc
    def Reset(self) -> None:
        self.hp = gcon.PLAYER_MAX_HP
        self.blockControl = False
        self.active = True
        self.visible = True
        self.RestAllKeys()

        #timing reset/set
        for timeTmp in self.timers:
            timeTmp.FullReset()
        #default timer vaules
            
        #end of reset

    def __init__(self, playerId: gcon.PLAYER_ID ) -> None:
        self.playerId = playerId
        self.physicsBox = gameBoxPhy.box((300,100,0),(gcon.PLAYER_SIZE,gcon.PLAYER_SIZE,0))
        self.active = True
        self.visible = True

        #timing init
        self.timers: list[gTim.GameTimer] = []
        for timeTmp in gcon.PLAYER_TIMER:
            self.timers.append(gTim.GameTimer(0))
        
        #end reset/everything else
        self.Reset()
        #end of init

    
    #states
    def IsStunned(self) -> None:
        return self.blockControl or not self.timers[gcon.PLAYER_TIMER.STUN].IsDone()


    #tick actions
    def Tick(self) -> None:
        self.UpdateKeys()
        self.TickMove()
        self.physicsBox.PhysicsTick()



        #end of Tick

    def TickMove(self) -> None:
        angle = gcon.ANGLE_NON
        speed = gcon.PLAYER_WALKING_SPEED

        #check diagonal first
        #up left
        if self.upLeft > 0:
            angle = gcon.ANGLE_UP_LEFT
        #up right
        elif self.upRight > 0:
            angle = gcon.ANGLE_UP_RIGHT
        #down right
        elif self.downRight > 0 :
            angle = gcon.ANGLE_DOWN_RIGHT
        #down left
        elif self.downLeft > 0:
            angle = gcon.ANGLE_DOWN_LEFT
        #if no diagonal, check perpendicular
        #up
        elif self.upKey > 0:
            angle = gcon.ANGLE_UP
        #down
        elif self.downKey > 0:
            angle = gcon.ANGLE_DOWN
        #left
        elif self.leftKey > 0:
            angle = gcon.ANGLE_LEFT
        #right
        elif self.rightKey > 0:
            angle = gcon.ANGLE_RIGHT

        #move
        if angle != gcon.ANGLE_NON:
            self.physicsBox.SetAccelerationMagnitudeRelative(angle, speed)
        
        #end tick move


    #draw
    def Draw(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        if self.visible:
            #testing
            self.physicsBox.DebugDrawBox(drawToSurface)
            gameUi.UpdateTitleBar("player speed: " + str(self.physicsBox.GetVelocityMagnitude()))
        
        #end of draw


