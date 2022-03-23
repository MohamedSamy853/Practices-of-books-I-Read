from typing import List
import sys
sys.path.append("..")
from Guitar import Guiter
from Type import Type 
from Builder import Builder
from Wood import Wood 
class Inventor:
    global guitars
    guitars = list()
    def addGuiter(self , serialNumber :str , Price :float , builder :Builder , model:str , type:Type , bacWood:Wood , topWood:Wood)->None:
        guiter = Guiter(serialNumber  , Price  , builder  , model , type , bacWood , topWood)
        guitars.append(guiter)
        return None
    def getGuiter(self , serialNumber:str)->Guiter or None:
        for guiter in guitars:
            if guiter.getSerialNumber()==serialNumber:
                return guiter
        return None 
    def search(self , serachedGuitar:Guiter)->List[Guiter] or None:
        matched_guitar = list()
        for guitar in guitars:
            builder = guitar.getBuilder()
            if builder != serachedGuitar.getBuilder() :
                continue
            model = guitar.getModel().lower()
            if model!=serachedGuitar.getModel().lower() and model not in ['' , None]:
                continue
            type =  guitar.getType()
            if type != serachedGuitar.getType() :
                continue
            backWood =  guitar.getBackWood()
            if backWood != serachedGuitar.getBackWood() :
                continue
            topWood = guitar.getTopWood()
            if topWood != serachedGuitar.getTopWood() : 
                continue
            #it will execute if all condition before are false that means all features are equal
            matched_guitar.append(guitar)
        
        return matched_guitar if bool(matched_guitar) else None  
if __name__ == '__main__':
    guiterIWant = Guiter('1234' , 120  , Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD)
    MyInventor = Inventor()
    MyInventor.addGuiter('1234' , 1250 , Builder.GIBSON , 'model2' , Type.ACOUSTIC , Wood.CADER , Wood.SITKA)
    slectedGuiter = MyInventor.getGuiter('1234')
    print(slectedGuiter.getPrice()) #1250
    print(MyInventor.search(guiterIWant)) #None
    MyInventor.addGuiter("234100" , 3000 , Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD)
    MyInventor.addGuiter('5456' , 1562 ,  Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD )
    res = MyInventor.search(guiterIWant)
    if res !=None :
        print("matched guiter are :")
        for match in res :
            print(" "*2 ,match.getSerialNumber() , 'price' , match.getPrice() , sep = " ")

    else :
        print("not found !")