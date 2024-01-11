import pygame
import gametools
import gameConstants as gcon
import gameTiming as gTim
import gameBoxPhy
import gameInput


class player:

    #controls
    def RestAllKeys(self) -> None:
        self._keyUp = 0
        self._keyDown = 0
        self._keyLeft = 0
        self._keyRight = 0

    def UpdateKeys(self) -> None:
        #takes a snapshot of current key state if you are able to use keys
        #if not self._blockControl
        pass

    #etc
    def Reset(self) -> None:
        self._hp = gcon.PLAYER_MAX_HP
        self._blockControl = False
        self.RestAllKeys()

        #timing reset/set
        for timeTmp in self._timers:
            timeTmp.FullReset()
        #default timer vaules


    #end of reset


    def __init__(self, playerId: gcon.PLAYER_ID ) -> None:
        self._playerId = playerId
        self._physicsBox = gameBoxPhy.box((300,100,100),(gcon.PLAYER_SIZE,gcon.PLAYER_SIZE,0))
        
        #timing init
        self._timers: list[gTim.GameTimer] = []
        for timeTmp in gcon.PLAYER_TIMER.STUN:
            self._timers.append(gTim.GameTimer(timeTmp[1]))
        
        #end reset/everything else
        self.Reset()
    #end of init


    #tick actions
    def Tick(self) -> None:
        self._physicsBox.PhysicsTick()

        #test timer

    #end of Tick


    #draw
    def Draw(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        self._physicsBox.DebugDrawBox(drawToSurface)


# #input test
                #self._timers[gcon.PLAYER_TIMER.STUN] = gcon.PLAYER_TIME_STUN_TEST #test
# gameInput.TickInputs()
# testspeed = gameConstants.WALKING_SPEED
# upKey = gameInput.AllUserInput[gameConstants.PLAYER_ID.ONE][gameConstants.INPUT_ID.UP].IsInputActive()
# downKey = gameInput.AllUserInput[gameConstants.PLAYER_ID.ONE][gameConstants.INPUT_ID.DOWN].IsInputActive() 
# leftKey = gameInput.AllUserInput[gameConstants.PLAYER_ID.ONE][gameConstants.INPUT_ID.LEFT].IsInputActive()
# rightKey = gameInput.AllUserInput[gameConstants.PLAYER_ID.ONE][gameConstants.INPUT_ID.RIGHT].IsInputActive()
# xspeed = testPhyBox.GetVelocityX()
# yspeed = testPhyBox.GetVelocityY()
# speed = testPhyBox.GetVelocityMagnitude()
# if upKey:
#     player_pos.y -= testspeed
# if downKey:
#         player_pos.y += testspeed
# if leftKey:
#         player_pos.x -= testspeed
# if rightKey:
#     player_pos.x += testspeed