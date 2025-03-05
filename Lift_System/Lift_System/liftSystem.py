from Lift_System.Lift_System.utils import DIRECTION
from Lift_System.lift import Lift
from Lift_System.controls import InnerControls, OuterControls
from Lift_System.floor import Floor
import heapq

class LiftSystem:
    _instance = None

    def __init__(self, num_lifts, num_floors):
        self.num_lifts = num_lifts
        self.num_floors = num_floors
        self.lifts = []
        self.floors = []
        self.pending_up_requests = []
        self.pending_down_requests = []
        for _ in range(num_lifts):
            inner_controls = InnerControls(num_floors)
            self.lifts.append(Lift(controls=inner_controls, current_floor=0))

        for i in range(num_floors):
            outer_controls = OuterControls()
            self.floors.append(Floor(outer_controls, i+1))

        

    def __new__(cls, num_lifts=None, num_floors=None):
        if cls._instance is None:
            cls._instance = super(LiftSystem, cls).__new__(cls, num_lifts, num_floors)
        
        return cls._instance
        

    def display_all_lifts_info(self):
        for lift in self.lifts:
            dir = lift.get_direction()
            floor = lift.get_curr_floor()
            print(f"Lift info:-  Direction: {dir}, Floor: {floor}")

    
    def call_lift(self, floor, direction):
        """
        curr floor and destination direction
        """
        if direction == DIRECTION.UP.value:
            heapq.heappush(self.pending_up_requests, floor)
        else:
            heapq.heappush(self.pending_down_requests, floor)
        # algorithm to call lift (lift dispatcher)
        pass
