class Button:
    
    def __init__(self, value, type):
        self.value = value
        self.isClicked = False
        self.type = type

    def press_button(self):
        self.isClicked = True

    def unselect_buton(self):
        self.isClicked = True