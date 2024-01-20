import math

#value helpers
def ClampValue(value, minValue, maxValue):
    return max(min(value, maxValue), minValue)

def CopySign(value):
    return math.copysign(1, value)

#returns bool if its between two values, inclusionary
def IsBetween(value, minValue, maxValue):
    return maxValue >= value >= minValue

#Vectors
def FindDistance(xy1: tuple[float, float],xy2: tuple[float, float]) -> float:
    return math.sqrt((xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2)

def VectorMagnitude(xy: tuple[float, float]) -> float:
    return math.sqrt(xy[0]**2 + xy[1]**2)

def VectorAngle(xy: tuple[float, float]) -> float:
    return math.atan2(xy[0],xy[1])

def VectorNew(angleNew: float, magnitudeNew: float) -> tuple[float, float]:
    return (magnitudeNew * math.sin(angleNew), magnitudeNew * math.cos(angleNew))

def VectorNormalize(v: tuple[float, float]) -> tuple[float, float]:
    mag = VectorMagnitude(v)
    return (v[0]/mag, v[1]/mag)

def VectorMultiplyConstant(v: tuple[float, float], m: float) -> tuple[float, float]:
    return (v[0] * m, v[1] * m)

def VectorsAdd(v1: tuple[float, float], v2: tuple[float, float]) -> tuple[float, float]:
    return (v1[0] + v2[0], v1[1] + v2[1])

#rectangle/boxes
#input: x,y,hight,width output: left, top, right, bottom (LTRB)
def BoxMakeXYHWtoLTRB(xy: tuple[float, float], widthHight: tuple[float, float]) -> tuple[float, float, float, float]:
    return (
        xy[0],
        xy[1],
        xy[0] + widthHight[0],
        xy[1] + widthHight[1]
    )

#box format needs to be output: left 0, top 1, right 2, bottom 3 (LTRB)
#   1
#   _
# 0| |2
#   -
#   3
#AABB check, true if not touch, false if touch
def BoxIsOverlap(box0: tuple[float, float, float, float], box1: tuple[float, float, float, float]) -> bool:
    return not ( 
        box0[0] > box1[2] 
        or box0[2] < box1[0] 
        or box0[1] > box1[3] 
        or box0[3] < box1[1] 
        )

#true if point in box (LTRB)
def PointInBox(pointXY: tuple[float, float], boxLTRB: tuple[float, float, float, float]) -> bool:
    return not (
        pointXY[0] < boxLTRB[0] #x more than box left
        or pointXY[0] > boxLTRB[2] #x more than right
        or pointXY[1] < boxLTRB[1] #y is above
        or pointXY[1] > boxLTRB[3] #y is below
    )

#velocity

def VelocityXGoingLeft(vx: float) -> bool:
    return vx < 0

def VelocityXGoingRigh(vx: float) -> bool:
    return vx > 0

def VelocityYGoingUp(vx: float) -> bool:
    return vx < 0

def VelocityYGoingDown(vx: float) -> bool:
    return vx > 0

def VelocityZGoingDown(vx: float) -> bool:
    return vx < 0

def VelocityZGoingUp(vx: float) -> bool:
    return vx > 0