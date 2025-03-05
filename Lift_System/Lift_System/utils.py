from enum import Enum

class BUTTONTYPE(Enum):
    DIRECTION = "direction"
    NUMBER = "number"
    STATE = "state"

class DIRECTION(Enum):
    UP = "up"
    DOWN = "down"

class LIFTSTATE(Enum):
    GOING_UP = "going_up"
    GOING_DOWN = "going_down"
    STOP = "stop"
    OPEN = "open"
    CLOSE = "close"
