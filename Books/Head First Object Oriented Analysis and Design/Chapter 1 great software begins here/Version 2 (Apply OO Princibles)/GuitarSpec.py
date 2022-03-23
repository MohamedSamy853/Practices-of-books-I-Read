import sys
sys.path.append("..")
from Builder import Builder
from Wood import Wood
from Type import Type
class GuitarSpec():
    def __init__(self , builer :Builder , model :str ,type:Type , backWood:Wood , topWood:Wood )->None:
        self.builder = builer
        self.model = model 
        self.type = type
        self.backWood = backWood
        self.topWood = topWood
        return None
    def getBuilder(self) ->Builder :
        return self.builder
    def getModel(self)->str:
        return self.model
    def getBackWood(self)->Wood:
        return self.backWood
    def getTopWood(self)->Wood:
        return self.topWood
    def getType(self)->Type:
        return self.type
    