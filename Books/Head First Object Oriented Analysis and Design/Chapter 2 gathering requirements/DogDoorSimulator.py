from DogDoor import DogDoor
from Remote import Remote
if __name__ == "__main__":
    door = DogDoor()
    remote = Remote(door)
    print('dog want to go outside')
    remote.pressbutton()
    print('dog has gone outside')
    remote.pressbutton()
    print('dog want to go inside')
    remote.pressbutton()
    print('dog is allready in the home')