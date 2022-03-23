from DogDoor import DogDoor
class Remote:
    def __init__(self , door:DogDoor) -> None:
        self.door = door
    def pressbutton(self)->None:
        print('pressing into remote control button')
        if self.door.isOpen():
            print('the dog door closes ')
            self.door.close()
        else :
            print('the dog door opens')
            self.door.open()


