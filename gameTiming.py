import math
import gameConstants
import gametools

#time helpers
def MinutesToTicks(minutes: float) -> int:
  return math.trunc(minutes * 60 * gameConstants.MILLISECONDS_IN_SECOND * gameConstants.TICKS_IN_MILLISECOND)

def SecondsToTicks(seconds: float) -> int:
  return math.trunc(seconds * gameConstants.MILLISECONDS_IN_SECOND * gameConstants.TICKS_IN_MILLISECOND)

def MillisecondsToTicks(milliseconds: float) -> int:
  return math.trunc(milliseconds * gameConstants.TICKS_IN_MILLISECOND)

def TicksToMilliseconds(ticks: int) -> float:
   return ticks * gameConstants.MILLISECONDS_IN_TICK


#master clock
masterTickTimer = 0

def TickMasterClock() -> None:
   global masterTickTimer
   masterTickTimer += 1

def MasterClockToMs() -> float:
   return TicksToMilliseconds(masterTickTimer)


#timers
class GameTimer:

   def __init__(self, lengthInMs: float) -> None:
      self.Set(lengthInMs)

   def EnforceTimeLimit(self, timeInTicks: int) -> int:
      return gametools.ClampValue(timeInTicks, 0, gameConstants.TIMER_MAX_TICKS)

   def Set(self, lengthInMs: float) -> None:
      self.FullReset()
      self._timerEndTicks = self.EnforceTimeLimit(MillisecondsToTicks(lengthInMs))

   #reset back to zero
   def FullReset(self) -> None:
      self._timerEndTicks = 0
      self._timerStateTicks = 0

   def ResetTimer(self) -> None:
      self._timerStateTicks = 0

   def EndNow(self) -> None:
      self._timerStateTicks = self._timerEndTicks

   #true if the timer is passed, false if not
   def IsDone(self) -> bool:
      return self._timerStateTicks >= self._timerEndTicks

   #run each tick to update the timer
   def Tick(self) -> None:
      self._timerStateTicks += 1 if self._timerStateTicks < gameConstants.TIMER_MAX_TICKS else 0

   #return range 0.0-1.0
   def PercentageCompleted(self) -> float:
      if self._timerEndTicks == 0:
         return 1
      else:
         return self._timerStateTicks / self._timerEndTicks