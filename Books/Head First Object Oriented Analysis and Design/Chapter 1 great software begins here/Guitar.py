
class Guiter(object):
    '''
        this class is designed to store details about guitar
    '''
    def __init__(self , serialNumber :str , Price :float , builder :str , model:str , type:str , bacWood:str , topWood:str) -> None:
        self.serialNumber  = serialNumber
        self.Price = Price
        self.builder = builder
        self.model = model 
        self.type =type
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
        return self.builder
    def getModel(self)->str:
        return self.model
    def getType(self)->str:
        return self.type
    def getBackWood(self)->str:
        return self.bacWood
    def getTopWood(self)->str:
        return self.topWood

