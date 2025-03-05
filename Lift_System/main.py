from Lift_System.liftSystem import LiftSystem
from Lift_System.handle_request import RequestMapping
import textwrap

if __name__ == "__main__":
    systum = LiftSystem(num_lifts=3, num_floors=10)
    systum.display_all_lifts_info()

    while True:
        print(textwrap.dedent(
            """
            Instructions for using lift/n  
            If outide lift, type
            1 -- if you want to go down 
            2 -- if you want to go up
            If inside lift, type
            3 -- open lift (can be used if state is at stop)
            4 -- close lift (can be used if lift is at stop)
            5 -- choose destination
            """
        ))
        inp = int(input("Enter you choice:"))
        if inp >= 1 and inp <= 5:
            RequestMapping[inp].value()
        else:
            print("Give a valid request")
