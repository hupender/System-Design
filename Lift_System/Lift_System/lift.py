from Lift_System.utils import LIFTSTATE, DIRECTION
from Lift_System.liftSystem import LiftSystem
import time
import heapq

lift_system = LiftSystem()


class Lift:

    def __init__(self, controls, current_floor):
        self.controls = controls
        self.current_floor = current_floor
        self.numer_of_people = 0
        self.weight = 0
        self.direction = None
        self.state = LIFTSTATE.STOP.value
        self.stop_list = []
        self.door_state = LIFTSTATE.CLOSE.value

    def get_direction(self):
        return self.direction
    
    def get_curr_floor(self):
        return self.current_floor
    
    def move(self):
        # move to next floor simulation
        time.sleep(3)
        if self.direction == DIRECTION.UP.value and self.current_floor < lift_system.num_floors:
            self.current_floor += 1
        elif self.direction == DIRECTION.DOWN.value and self.current_floor > 1:
            self.current_floor -= 1
        else:
            self.stop()

        # if it's lift stop then stop or check if there is a request from current floor then stop 
        if (
            self.current_floor in self.stop_list 
            or (self.direction == DIRECTION.UP.vlue and self.current_floor in lift_system.pending_up_requests)
            or (self.direction == DIRECTION.DOWN.value and self.current_floor in lift_system.pending_down_requests)
        ):
            if self.direction == DIRECTION.UP.vlue:
                self.stop_list.pop(0)
            else:
                self.stop_list.pop()
            # unpress button
            button = self.controls.get_button_with_value(self.current_floor)
            button.unselect_buton()

            self.stop()
            self.open_lift()
            # opening simulation
            time.sleep(5)

            # closing simulation
            time.sleep(5)
            self.close_lift()

        if self.stop_list:
            self.move()


    def stop(self):
        self.state = LIFTSTATE.STOP.value

    def open_lift(self):
        if self.state == LIFTSTATE.STOP.value:
            self.door_state = LIFTSTATE.OPEN.value
        else:
            print("Can't perform this action when lift is moving")

    def close_lift(self):
        if self.door_state == LIFTSTATE.OPEN.value:
            self.door_state = LIFTSTATE.CLOSE.value
        elif self.door_state == LIFTSTATE.CLOSE.value:
            print("Lift Already Close")
        else:
            print("Can't perform this action when lift is moving")

    def select_destination(self, floor):
        button = self.controls.get_button_with_value(floor)
        button.press_button()
        heapq.heappush(self.stop_list, floor)
