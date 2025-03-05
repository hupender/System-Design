from enum import Enum
from Lift_System.utils import DIRECTION
from Lift_System.liftSystem import LiftSystem

class HandleRequest:

    def __init__(self):
        pass

    def go_up(self):
        floor = int(input("Enter your floor: "))
        LiftSystem().call_lift(floor, DIRECTION.UP.value)

    def go_down(self):
        floor = int(input("Enter your floor: "))
        LiftSystem().call_lift(floor, DIRECTION.DOWN.value)

    def open_lift(self, lift):
        lift.open_lift()

    def close_lift(self, lift):
        lift.close_lift()

    def select_destination(self, lift, floor):
        lift.select_destination(floor)

class RequestMapping(Enum):
    1 = HandleRequest.go_up
    2 = HandleRequest.go_down
    3 = HandleRequest.open_lift
    4 = HandleRequest.close_lift
    5 = HandleRequest.select_destination