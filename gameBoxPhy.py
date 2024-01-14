#main rectangle tools and physics
import gametools
import gameConstants
import pygame


class box:

    #resets
    def ResetVelocity(self):
        self._velocityX = 0
        self._velocityY = 0
        self._velocityZ = 0

    def ResetAcceleration(self) -> None:
        self._accelerationX = 0
        self._accelerationY = 0
        self._accelerationZ = 0

    def ResetAccelerationAndVelocity(self) -> None:
        self.ResetVelocity()
        self.ResetAcceleration()

    def ResetAll(self) -> None:
        #location and size
        self._x = 0 #top
        self._y = 0 #left
        self._z = gameConstants.Z_MIN #note: z axis/height items are calculated separately from z/y. Z also counts as the "bottom" of the box.
        self._checkpointX = 0
        self._checkpointY = 0
        self._checkpointZ = gameConstants.Z_MIN
        self._width = gameConstants.PHY_MIN_WIDTH
        self._height = gameConstants.PHY_MIN_HIEGHT
        self._zHeight = gameConstants.ZHIEGHT_MIN
        self._friction = gameConstants.FRICTION_GROUND_PERCENTAGE

        #physics
        self.ResetAccelerationAndVelocity()

        #settings
        self._physicsOn = True
        self._collisionDetection = True 

        #flags
        self._physicsTickVelocityXYZsign = (0,0,0) #holds x/y/z tuple of the signs of the velocity of the last physics tick


    #get/set settings
    @property
    def physicsOn(self) -> bool:
        return self._physicsOn
    @physicsOn.setter
    def physicsOn(self, input: bool):
        self._physicsOn = input

    @property
    def collisionDetection(self) -> bool:
        return self._collisionDetection
    @collisionDetection.setter
    def collisionDetection(self, input: bool):
        self._collisionDetection = input


    #set/get location
    @property
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, input: float):
        self._x = input
    
    @property
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, input: float):
        self._y = input

    @property
    def z(self) -> float:
        return self._z
    @z.setter
    def z(self, input: float):
        self._z = gametools.ClampValue(input, gameConstants.Z_MIN, gameConstants.Z_MAX)

    @property
    def checkpointX(self) -> float:
        return self._checkpointX
    @checkpointX.setter
    def checkpointX(self, input: float):
        self._checkpointX = input
    
    @property
    def checkpointY(self) -> float:
        return self.checkpointY
    @checkpointY.setter
    def checkpointY(self, input: float):
        self._checkpointY = input

    @property
    def checkpointZ(self) -> float:
        return self.checkpointZ
    @checkpointY.setter
    def checkpointZ(self, input: float):
        self._checkpointZ = gametools.ClampValue(input, gameConstants.Z_MIN, gameConstants.Z_MAX)


    @property
    def width(self) -> float:
        return self._width
    @width.setter
    def width(self, input: float):
        self._width = gametools.ClampValue(input, gameConstants.PHY_MIN_WIDTH, gameConstants.PHY_MAX_WIDTH)

    @property
    def height(self) -> float:
        return self._height
    @height.setter
    def height(self, input: float):
        self._height = gametools.ClampValue(input, gameConstants.PHY_MIN_HIEGHT, gameConstants.PHY_MAX_HIEGHT)

    @property
    def zHeight(self) -> float:
        return self._zHeight
    @zHeight.setter
    def zHeight(self, input: float):
        self._zHeight = gametools.ClampValue(input, gameConstants.ZHIEGHT_MIN, gameConstants.ZHEIGHT_MAX)

    # @property
    # def friction(self) -> float:
    #     return self._friction
    # @friction.setter
    # def friction(self, input: float):
    #     self._friction = input


    #x/y/z
    def SetXrelative(self, x: float) -> None:
        self.x += x

    def SetYrelative(self, y: float) -> None:
        self.y += y

    def SetZrelative(self, z: float) -> None:
        self.z += z

    def WarpXY(self) -> None:
        #x
        if self.GetRight() < 0:
            self.x = gameConstants.SCREEN_WIDTH_PIXELS - 1
        elif self.GetLeft() >= gameConstants.SCREEN_WIDTH_PIXELS:
            self.x = -(self.width + 1) 
        #y
        if self.GetBottom() < 0:
            self.y = gameConstants.SCREEN_HEIGHT_PIXELS - 1
        elif self.GetTop() >= gameConstants.SCREEN_HEIGHT_PIXELS:
            self.y = -(self.height + 1)



    #velocity
    #note: Will be x/y unless it says its Z
    def GetVelocityMagnitude(self) -> float:
        return gametools.VectorMagnitude((self._velocityX, self._velocityY))

    def GetVelocityAngle(self) -> float:
        return gametools.VectorAngle((self._velocityX, self._velocityY))

    def SetVelocityAngleMagnitude(self, angleNew: float, magnitudeNew: float) -> None:
        #clobbers old values and replaces them with new values
        tmpVec = gametools.VectorNew(angleNew, magnitudeNew)
        self._velocityX = tmpVec[0]
        self._velocityY = tmpVec[1]

    def SetVelocityMagnitudeRelative(self, angleNew: float, magnitudeNew: float) -> None:
        tmpVec = gametools.VectorNew(angleNew, magnitudeNew)
        self._velocityX += tmpVec[0]
        self._velocityY += tmpVec[1]

    def VelocitySpeedLimiter(self) -> None:
        if self.GetVelocityMagnitude() > gameConstants.ACCELERATION_MAX:
            self.SetVelocityAngleMagnitude(
                self.GetVelocityAngle(),
                gameConstants.ACCELERATION_MAX)
            
        self._velocityZ = gametools.ClampValue(self._velocityZ, -gameConstants.Z_MAX_VELOCITY, gameConstants.Z_MAX_ACCELERATION)

    def SetVelocityZ(self, z: float) -> None:
        self._velocityZ = z

    def SetVelocityXrelative(self, x: float) -> None:
        self._velocityX += x

    def SetVelocityYrelative(self, y: float) -> None:
        self._velocityY += y

    def SetVelocityZrelative(self, z: float) -> None:
        self._velocityZ += z

    def GetVelocityX(self) -> float:
        return self._velocityX
    
    def GetVelocityY(self) -> float:
        return self._velocityY

    def GetVelocityZ(self) -> float:
        return self._velocityZ

    def GetVelocitySign(self) -> tuple[float,float, float]:
        return (gametools.CopySign(self._x),gametools.CopySign(self._y),gametools.CopySign(self._z))

    def VelocityFrictionX(self, frictionAmount: float) -> None:
        self._velocityX *= frictionAmount

    def VelocityFrictionY(self, frictionAmount: float) -> None:
        self._velocityY *= frictionAmount

    def VelocityFrictionXY(self, frictionAmount: float) -> None:
        self.VelocityFrictionX(frictionAmount)
        self.VelocityFrictionY(frictionAmount)

    def VelocityMinSpeedLimit(self) -> float:
        if self.GetVelocityMagnitude() < gameConstants.SPEED_MIN_ANY:
            self._velocityX = 0
            self._velocityY = 0


    #acceleration
    #only does x/y unless noted as doing z
    def GetAccelerationMagnitude(self) -> float:
        return gametools.VectorMagnitude((self._accelerationX, self._accelerationY))

    def GetAccelerationAngle(self) -> float:
        return gametools.VectorAngle((self._accelerationX, self._accelerationY))

    def SetAccelerationAngleMagnitude(self, angleNew: float, magnitudeNew: float) -> None:
        #clobbers old values and replaces them with new values
        tmpVec = gametools.VectorNew(angleNew, magnitudeNew)
        self._accelerationX = tmpVec[0]
        self._accelerationY = tmpVec[1]

    def SetAccelerationMagnitudeRelative(self, angleNew: float, magnitudeNew: float) -> None:
        tmpVec = gametools.VectorNew(angleNew, magnitudeNew)
        self._accelerationX += tmpVec[0]
        self._accelerationY += tmpVec[1]

    def SetAccelerationZ(self, z: float) -> None:
        self._accelerationZ = z

    def AccelerationSpeedLimiter(self) -> None:
        if self.GetAccelerationMagnitude() > gameConstants.ACCELERATION_MAX:
            self.SetAccelerationAngleMagnitude(
                self.GetAccelerationAngle(),
                gameConstants.ACCELERATION_MAX)
        
        self._accelerationZ = gametools.ClampValue(self._accelerationZ, -gameConstants.Z_MAX_ACCELERATION, gameConstants.Z_MAX_ACCELERATION)

    def SetAccelerationXrelative(self, x: float) -> None:
        self._accelerationX += x

    def SetAccelerationYrelative(self, y: float) -> None:
        self._accelerationY += y

    def SetAccelerationZrelative(self, z: float) -> None:
        self._accelerationZ += z

    def GetAccelerationX(self) -> float:
        return self._accelerationX
    
    def GetAccelerationY(self) -> float:
        return self._accelerationY

    def GetAccelerationZ(self) -> float:
        return self._accelerationZ

    def AccelerationMinSpeedLimit(self) -> float:
        if self.GetAccelerationMagnitude() <= gameConstants.SPEED_MIN_ANY:
            self._accelerationX = 0
            self._accelerationY = 0



    #physics
    def UpdateAirGroundFriction(self) -> None:
        if self.z <= 0:
            self._friction = gameConstants.FRICTION_GROUND_PERCENTAGE
        else:
            self._friction = gameConstants.FRICTION_AIR_PERCENTAGE

    def PhysicsTick(self) -> None:
        if (not self.physicsOn):
            return
        
        #Acceleration
        self.AccelerationMinSpeedLimit()
        self.AccelerationSpeedLimiter()
        self.SetVelocityXrelative(self._accelerationX)
        self.SetVelocityYrelative(self._accelerationY)
        self.SetVelocityZrelative(self._accelerationZ)
        self.SetVelocityZrelative(-gameConstants.GRAVITY_ACCELERATION)
        self.ResetAcceleration()
        
        
        #Velocity
        self.VelocitySpeedLimiter()
        self.UpdateAirGroundFriction()
        self.VelocityFrictionXY(self._friction)
        self.VelocityMinSpeedLimit()
        self._physicsTickVelocityXYZsign = self.GetVelocitySign()

        #x/y
        self.SetXrelative(self._velocityX)
        self.SetYrelative(self._velocityY)
        self.SetZrelative(self._velocityZ)

        #gravity/floor
        if self.z <= 0 and self._velocityZ < 0:
            #ground collision
            self.z = 0
            self.SetVelocityZ(0)
        elif self.GetOnCeiling() and self._velocityZ > 0:
            #bouce off ceiling
            self.SetVelocityZ(-self._velocityZ * gameConstants.Z_CEILING_BOUNCE)

        #out of bounds warp
        self.WarpXY()

    def PhysicsTickVelocitySign(self) -> tuple[float, float, float]:
        return self._physicsTickVelocityXYZsign


    #checkpoints
    def TeleportToCheckpoint(self) -> None:
        self.ResetAccelerationAndVelocity()
        self.x = self.checkpointX
        self.y = self.checkpointY
        self.z = self.checkpointZ
        self.WarpXY()


    #get location and size
    def GetXY(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def GetWH(self) -> tuple[float, float]:
        return (self.width, self.height)
    
    def GetXYWH(self) -> tuple[float, float, float, float]:
        return (self.x, self.y, self.width, self.height)

    def GetXYHW(self) -> tuple[float, float, float, float]:
        return (self.x, self.y, self.height, self.width)
    
    def GetXYHWwithZYoffset(self) -> tuple[float, float, float, float]:
        return (self.x, self.y - self.z, self.height, self.width)

    def GetCenterXY(self) -> tuple[float, float]:
        return (self.x + self._width / 2, self.y + self.height / 2)
    
    def GetLeft(self) -> float:
        return self.x
    
    def GetTop(self) -> float:
        return self.y
    
    def GetTopZ(self) -> float:
        return self.z + self.zHeight

    def GetRight(self) -> float:
        return self.x + self.width
    
    def GetBottom(self) -> float:
        return self.y + self.height

    def GetBottomZ(self) -> float:
        return self.z

    def GetLTRB(self) -> tuple[float, float, float, float]:
        return (self.x, self.y, self.GetRight(), self.GetBottom())

    def GetTopBottomZ(self) -> tuple[float, float]:
        return (self.GetTopZ(), self.z)

    def GetOnGround(self) -> bool:
        return self.z == gameConstants.Z_MIN

    def GetOnCeiling(self) -> bool:
        return self.z >= gameConstants.Z_MAX

    def __init__(self, xyz: [float, float, float], widthHeightZheight: [float, float, float]) -> None:
        self.ResetAll()
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]
        self.checkpointX = xyz[0]
        self.checkpointY = xyz[1]
        self.checkpointZ = xyz[2]
        self.height = widthHeightZheight[0]
        self.width = widthHeightZheight[1]
        self.zHeight = widthHeightZheight[2]
        #bounds checking
        self.WarpXY()

    #overlap tools
    def BoxOverlap(self, boxLTRB: tuple[float, float, float, float]) -> bool:
        return gametools.BoxIsOverlap(self.GetLTRB(), boxLTRB)

    def PointOverlap(self, pointXY: tuple[float, float]) -> bool:
        return gametools.PointInBox(pointXY, self.GetLTRB())

    #overlap z testing, returns if its under above or in based on z
    def Zoverlap(self, TopBottom: tuple[float, float]) -> int:
        if self.GetTopZ() < TopBottom[1]:
            return gameConstants.Z_UNDER
        elif self.GetBottomZ() > TopBottom[0]:
            return gameConstants.Z_ONTOP
        else:
            return gameConstants.Z_OVERLAP
    
    #etc
    def DebugDrawBox(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        if gameConstants.GAME_DEBUG:
            #shadow
            if self.z > 0:
                pygame.draw.rect(drawToSurface, gameConstants.DEBUG_SHADOW_COLOR, self.GetXYHW(), width = gameConstants.DEBUG_BOX_WIDTH)
            #box
            pygame.draw.rect(drawToSurface, gameConstants.DEBUG_BOX_COLOR, self.GetXYHWwithZYoffset(), width = gameConstants.DEBUG_BOX_WIDTH)