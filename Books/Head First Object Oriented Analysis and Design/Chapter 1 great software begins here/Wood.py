from enum import Enum 
class Wood(Enum):
    INDIAN_ROSWOOD = 0 
    BRAZILIAN_ROSWOOD = 1
    MAHOGANY = 2
    MAPLE = 3
    COCOBOLO = 4
    CADER = 5
    ADRIRONDACK = 6
    ALDER = 7 
    SITKA = 8
    def __str__(self):
        for i in range(9):
            if self.value == i:
                return str(self.name).lower().replace("_" , " ")
        return None
