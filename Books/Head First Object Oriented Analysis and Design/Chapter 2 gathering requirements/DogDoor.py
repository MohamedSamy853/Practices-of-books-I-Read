class DogDoor:
    __open = False
    def __init__(self) -> None:
        self.__open = False
    def open(self )->None:
        self.__open = True
    def close(self)->None:
        self.__open = False
    def isOpen(self)->bool:
        return self.__open