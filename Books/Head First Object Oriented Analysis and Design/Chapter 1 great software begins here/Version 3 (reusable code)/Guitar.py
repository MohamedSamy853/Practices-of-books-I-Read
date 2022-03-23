from  GuitarSpec import GuitarSpec

class Guitar:
    def __init__(self , serialNumber :str , price :float , spec:GuitarSpec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec
        
    def setPrice(self, new_price :float)->None:
        self.price = new_price
    
    def getPrice(self)->float:
        return self.price
    
    def getSerialNumber(self)->str:
        return self.serialNumber

    def getSpec(self)->GuitarSpec:
        return self.spec

    

