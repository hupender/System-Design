from Lift_System.button import Button
from Lift_System.utils import BUTTONTYPE, DIRECTION, LIFTSTATE

class BaseControls:

    def __init__(self, buttons):
        self.buttons = buttons

    def get_buttons(self):
        return self.buttons
    
    def get_button_with_value(self, value):
        button = next((button for button in self.buttons if button.value == value), None)


class OuterControls(BaseControls):

    def __init__(self):
        buttons = []
        buttons.append(Button(value=DIRECTION.UP.value, type=BUTTONTYPE.DIRECTION.value))
        buttons.append(Button(value=DIRECTION.DOWN.value, type=BUTTONTYPE.STATE.value))
        super(OuterControls, self).__init__(buttons)



class InnerControls(BaseControls):

    def __init__(self, numfloors):
        buttons = [Button(i+1, BUTTONTYPE.NUMBER.value) for i in range(numfloors)]
        buttons.append(Button(value=LIFTSTATE.OPEN.value, type=BUTTONTYPE.STATE.value))
        buttons.append(Button(value=LIFTSTATE.CLOSE.value, type=BUTTONTYPE.STATE.value))
        super(InnerControls, self).__init__(buttons)