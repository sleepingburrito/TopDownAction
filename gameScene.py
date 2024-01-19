import pygame
import gameConstants
import gamePlayer
import gameWall
import os
import json


_playersList: list[gamePlayer.player] = []
_ActivePlayers: list[bool] = []

_wallsList: list[gameWall.wall] = []


#players
def InitPlayers() -> None:
    for tmply in gameConstants.PLAYER_ID:
        _playersList.append(gamePlayer.player(tmply))
        _ActivePlayers.append(False)
    #make first player active
    _playersList[gameConstants.PLAYER_ID.ONE].active = True
    _ActivePlayers[gameConstants.PLAYER_ID.ONE] = True

def MakePlayersActive() -> None:
    for i in range(len(_playersList)):
        _playersList[i].active = _ActivePlayers[i]

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
    for player in _playersList:
        player.Reset()

    MakePlayersActive()
    

#walls
#=======================
def InitWalls() -> None:
    for i in range(gameConstants.WALL_MAX_SCENE):
        _wallsList.append(gameWall.wall((0,0,0,0), i))

def ResetWalls() -> None:
    for wall in _wallsList:
        wall.ResetWall()

def DrawWalls(drawToSurface: pygame.surface.SurfaceType) -> None:
    for wall in _wallsList:
        if wall.active:
            wall.Draw(drawToSurface)


#scene
#=======================

def ResetScene() -> None:
    ResetPlayers()
    ResetWalls()

#returns true if no errors
def LoadScene(mapFileName: str) -> bool:
    #test data walls
    # _wallsList[0].physicsBox.x = 400
    # _wallsList[0].physicsBox.y = 150
    # _wallsList[0].physicsBox.height = 350
    # _wallsList[0].physicsBox.width = 123
    # _wallsList[0].active = True
    ResetScene()

    #load file
    file = open(os.path.join(gameConstants.SCENE_BASE_DIRECTORY, mapFileName))
    mapData = json.load(file)
    file.close()

    #load flags
    loadedObjects = False
    loadedPlayerSpawn = False
    loadedWalls =  False
    mapWallIndex = 0

    #loading scene json
    for layer in mapData["layers"]:
        match layer["name"]:
            #load scene objects
            case gameConstants.SCENE_JSON_LAYER_OBJECTS:
                if loadedObjects:
                    print("already loaded ", gameConstants.SCENE_JSON_LAYER_OBJECTS, " skipping other ones")
                else:
                    #map object match
                    loadedObjects = True
                    for mapObject in layer["objects"]:
                        match mapObject["name"]:
                            #player spawn / starting checkpoint
                            case gameConstants.SCENE_JSON_PLAYER_SPAWN:
                                loadedPlayerSpawn = True
                                x = float(mapObject['x'])
                                y = float(mapObject['y'])
                                for player in _playersList:
                                    player.physicsBox.checkpointX = x
                                    player.physicsBox.checkpointY = y
                                    player.physicsBox.TeleportToCheckpoint()
                                
                        
                    #end of map object match
            #end of scene objects

            #load map walls
            case gameConstants.SCENE_JSON_LAYER_WALLS:
                if loadedWalls:
                    print("already loaded ", gameConstants.SCENE_JSON_LAYER_WALLS, " skipping other ones")
                else:
                    loadedWalls = True
                    for wall in layer["objects"]:
                        if mapWallIndex >= gameConstants.WALL_MAX_SCENE:
                            print("Too many walls, cutoff at max ", gameConstants.WALL_MAX_SCENE)
                        else:
                            #parse wall data
                            _wallsList[mapWallIndex].physicsBox.x = float(wall['x'])
                            _wallsList[mapWallIndex].physicsBox.y = float(wall['y'])
                            _wallsList[mapWallIndex].physicsBox.height = float(wall['height'])
                            _wallsList[mapWallIndex].physicsBox.width = float(wall['width'])
                            _wallsList[mapWallIndex].active = True
                            mapWallIndex += 1
                            
                    
            #end of loading maps
                    
    #end of reading data
    
    return loadedObjects and loadedWalls and loadedPlayerSpawn and mapWallIndex < gameConstants.WALL_MAX_SCENE



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
    
    
