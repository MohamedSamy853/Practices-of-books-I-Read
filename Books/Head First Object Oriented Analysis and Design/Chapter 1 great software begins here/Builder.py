from enum import Enum
class Builder(Enum):
    FENDER = 0
    MARTIN = 1
    GIBSON = 2
    COLLINGS = 3
    OLSON = 4
    PYAN = 5
    PRS = 6
    ANY = 7
    def __str__(self):
        for i in range(8):
            if self.value == i:
                return str(self.name).lower()
        return None 
