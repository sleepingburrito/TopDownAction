import pygame
import gametools
import gameConstants
import gameTiming
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
        self._hp = gameConstants.PLAYER_MAX_HP
        self._blockControl = False
        self.RestAllKeys()
        
        #test
        self.jumpTimerTest = gameTiming.GameTimer(2000)

    def __init__(self, playerId: gameConstants.PLAYER_ID ) -> None:
        self._playerId = playerId
        self._physicsBox = gameBoxPhy.box((300,100,100),(gameConstants.PLAYER_SIZE,gameConstants.PLAYER_SIZE,0))
        self.Reset()


    #tick actions
    def Tick(self) -> None:

        #jump test
        self.jumpTimerTest.Tick()
        if self.jumpTimerTest.IsDone():
            self._physicsBox._accelerationZ = 2
            self.jumpTimerTest.ResetTimer()


        self._physicsBox.PhysicsTick()


    #draw
    def Draw(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        self._physicsBox.DebugDrawBox(drawToSurface)


# #input test
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