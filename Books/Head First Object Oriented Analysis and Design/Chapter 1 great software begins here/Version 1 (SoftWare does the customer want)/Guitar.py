import sys
sys.path.append('..')
from  Builder import Builder
from  Type import Type
from  Wood import Wood
class Guiter(object):
    '''
        this class is designed to store details about guitar
    '''
    def __init__(self , serialNumber :str , Price :float , builder :Builder , model:str , type:Type , bacWood:Wood , topWood:Wood) -> None:
        self.serialNumber  = serialNumber
        self.Price = Price
        self.builder = builder
        self.model = model 
        self.type = type
        self.bacWood = bacWood
        self.topWood =topWood
        return None 
    def setPrice(self , new_price:float)->None :
        self.Price= new_price
    def getSerialNumber(self)->str:
        return self.serialNumber
    def getPrice(self)->float:
        return self.Price
    def getBuilder(self)->str:
        return self.builder.name
    def getModel(self)->str:
        return self.model
    def getType(self)->str:
        return self.type.name
    def getBackWood(self)->str:
        return self.bacWood.name
    def getTopWood(self)->str:
        return self.topWood.name 

