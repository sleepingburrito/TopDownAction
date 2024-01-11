import gameInput
import gameConstants
import pygame
import gametools
import math
import gamePlayer
import gameTiming
import json
import gameBoxPhy

# pygame setup
pygame.init()
pygame.mixer.init()
PgScreen = pygame.display.set_mode((gameConstants.SCREEN_WIDTH_PIXELS, gameConstants.SCREEN_HEIGHT_PIXELS))
PgClock = pygame.time.Clock()
gameRunning = True

#local game code setup
gameInput.InitInput()
testplayer = gamePlayer.player(gameConstants.PLAYER_ID.ONE)
testplayer._physicsBox.SetAccelerationAngleMagnitude(0, 3)


while gameRunning:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    #timing
    gameTiming.TickMasterClock()
    



    #main tick
    testplayer.Tick()


    
    #test draw
    #===========================
    # fill the screen with a color to wipe away anything from last frame
    PgScreen.fill(gameConstants.DEFAULT_BG_COLOR)
    testplayer.Draw(PgScreen)
    # flip() the display to put your work on screen
    pygame.display.flip()
    #limit frame rate
    PgClock.tick(gameConstants.TICK_RATE)

#end steps
pygame.quit()