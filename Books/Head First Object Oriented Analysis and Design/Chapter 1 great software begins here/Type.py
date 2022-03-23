from enum import Enum  
class Type(Enum):
    ACOUSTIC = 0
    ELECTRIC = 1
    def __str__(self):
        if self.value == 0:
            return 'accoustic'
        if self.value == 1:
            return 'electric'

