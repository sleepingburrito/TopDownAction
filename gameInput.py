import pygame
import gameConstants
import gameTiming
import math
import gametools

#input classed
class UserInput:
        
    def __init__(self, inputId: gameConstants.INPUT_ID) -> None:
        self.FullReset()
        self.SetInputId(inputId)
        
    def FullReset(self) -> None:
        self._inputTickState = 0
        self.inputId = gameConstants.ID_NON

    def TimerReset(self) -> None:
        self._inputTickState = 0

    def SetInputId(self, newInputId: gameConstants.INPUT_ID) -> None:
        if newInputId in gameConstants.INPUT_ID:
            self.inputId = newInputId
        else:
            raise Exception("unknown input id")

    #isInputActive set true if the key is down, false if not
    #run each tick with pulled input
    def Tick(self, isInputActive: bool) -> None:
        if isInputActive == True:
            self._inputTickState = max(1, self._inputTickState + 1) #reset key timer and add one to it
        elif isInputActive == False:
            self._inputTickState = min(0, self._inputTickState - 1)
        else:
            raise Exception("unknown input state")
        #keep in timer range
        self._inputTickState = gametools.ClampValue(self._inputTickState, -gameConstants.TIMER_MAX_TICKS, gameConstants.TIMER_MAX_TICKS)

    #true if the key is down, false if not
    def IsInputActive(self) -> bool:
        return self._inputTickState > 0
    
    #how long the key has been down or up in milliseconds. Postive is down, negative is up
    def InputTime(self) -> float:
        return gameTiming.TicksToMilliseconds(self._inputTickState)


#global variables
AllUserInput: list[UserInput] = [] #holds all the user input states


#run first the set up the memory for the user input states
def InitInput() -> None:
    AllUserInput.clear()
    for playerId in gameConstants.PLAYER_ID:
        AllUserInput.append([]) #make player
        for inputType in gameConstants.INPUT_ID:
            AllUserInput[playerId.value].append(UserInput(inputType.value)) #make each input state

def ResetAllInputStates() -> None:
    for playerId in gameConstants.PLAYER_ID:
        for inputType in gameConstants.INPUT_ID:
            AllUserInput[playerId.value][inputType.value].TimerReset()

#updates key states, call once per tick.
def TickInputs() -> None:
    #test/todo as of now keymappings are hard coded
    
    #poll keys
    tmpKeys = pygame.key.get_pressed()

    #update keystate based off polled keys
    for playerId in gameConstants.PLAYER_ID:
        for inputType in gameConstants.INPUT_ID:
            tmpPlayerId = playerId.value #test as of now both players share the same keys
            keydown = False
            #key mapping
            match inputType.value:
                case gameConstants.INPUT_ID.UP:
                    keydown = tmpKeys[pygame.K_w]
                case gameConstants.INPUT_ID.DOWN:
                    keydown = tmpKeys[pygame.K_s]
                case gameConstants.INPUT_ID.LEFT:
                    keydown = tmpKeys[pygame.K_a]
                case gameConstants.INPUT_ID.RIGHT:
                    keydown = tmpKeys[pygame.K_d]
                case gameConstants.INPUT_ID.JUMP:
                    keydown = tmpKeys[pygame.K_SPACE]
            #update key input
            AllUserInput[playerId.value][inputType.value].Tick(keydown)


#testing code

