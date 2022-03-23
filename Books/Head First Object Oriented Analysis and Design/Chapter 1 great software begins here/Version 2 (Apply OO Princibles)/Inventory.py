from typing import List
from GuitarSpec import GuitarSpec
from Guitar import Guitar
import sys
sys.path.append("..")
from Builder import Builder
from Type import Type
from Wood import Wood
class Inventor:
    global guitars
    guitars = list()
    def addGuiter(self , serialNumber :str , Price :float ,spec :GuitarSpec  )->None:
        guiter = Guitar(serialNumber  , Price  , spec)
        guitars.append(guiter)
        return None
    def getGuiter(self , serialNumber:str)->Guitar or None:
        for guiter in guitars:
            if guiter.getSerialNumber()==serialNumber:
                return guiter
        return None 
    def search(self , serachedGuitar:GuitarSpec)->List[Guitar] or None:
        matched_guitar = list()
        for guitar in guitars:
            guitarSpec = guitar.getSpec()
            builder = guitarSpec.getBuilder()
            if builder != serachedGuitar.getBuilder() :
                continue
            model = guitarSpec.getModel().lower()
            if model!=serachedGuitar.getModel().lower() and model not in ['' , None]:
                continue
            type =  guitarSpec.getType()
            if type != serachedGuitar.getType() :
                continue
            backWood =  guitarSpec.getBackWood()
            if backWood != serachedGuitar.getBackWood() :
                continue
            topWood = guitarSpec.getTopWood()
            if topWood != serachedGuitar.getTopWood() : 
                continue
            #it will execute if all condition before are false that means all features are equal
            matched_guitar.append(guitar)
        
        return matched_guitar if bool(matched_guitar) else None  
if __name__ == '__main__':
    guiterIWant = GuitarSpec(Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD)
    MyInventor = Inventor()
    spec = GuitarSpec(Builder.GIBSON , 'model2' , Type.ACOUSTIC , Wood.CADER , Wood.SITKA)
    MyInventor.addGuiter('1234' , 1250 , spec)
    slectedGuiter = MyInventor.getGuiter('1234')
    print(slectedGuiter.getPrice()) #1250
    print(MyInventor.search(guiterIWant)) #None
    spec = GuitarSpec(Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD)
    MyInventor.addGuiter("234100" , 3000 , spec)
    spec = GuitarSpec(Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD )
    MyInventor.addGuiter('5456' , 1562 ,  spec)
    res = MyInventor.search(guiterIWant)
    if res !=None :
        print("matched guiter are :")
        for match in res :
            print(" "*2 ,match.getSerialNumber() , 'price' , match.getPrice() , sep = " ")
    else :
        print("not found !")