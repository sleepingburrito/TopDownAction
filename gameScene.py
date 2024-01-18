import pygame
import gameConstants
import gamePlayer
import gameWall


_playersList: list[gamePlayer.player] = []
_wallsList: list[gameWall.wall] = []


#players
def InitPlayers() -> None:
    for tmply in gameConstants.PLAYER_ID:
        _playersList.append(gamePlayer.player(tmply))
    #make first player active
    _playersList[gameConstants.PLAYER_ID.ONE].active = True

def TickPlayers() -> None:
    for player in _playersList:
        if player.active:
            player.Tick()

def DrawPlayers(drawToSurface: pygame.surface.SurfaceType) -> None:
    #draw all active players
    for player in _playersList:
        if player.active:
            player.Draw(drawToSurface)

def ResetPlayers() -> None:
    pass
    

#walls
#=======================
def InitWalls() -> None:
    for i in range(gameConstants.WALL_MAX_SCENE):
        _wallsList.append(gameWall.wall((0,0,0,0), i))


def ResetWalla() -> None:
    pass

def DrawWalls(drawToSurface: pygame.surface.SurfaceType) -> None:
    for wall in _wallsList:
        if wall.active:
            wall.Draw(drawToSurface)


#scene
#=======================

def LoadScene() -> None:
    #test data walls
    _wallsList[0].physicsBox.x = 400
    _wallsList[0].physicsBox.y = 150
    _wallsList[0].physicsBox.height = 350
    _wallsList[0].physicsBox.width = 123
    _wallsList[0].active = True


#everything
#=======================
#also helps with object interactions

def PlayersWallsInteraction() -> None:
    
    for player in _playersList:
        if player.active:
            for wall in _wallsList:
                if wall.active:
                    wall.Collide(player.physicsBox)

    #end of tick player

#call to run everything in order
def TickEverything() -> None:
    
    #player
    TickPlayers()
    PlayersWallsInteraction()
    
    
