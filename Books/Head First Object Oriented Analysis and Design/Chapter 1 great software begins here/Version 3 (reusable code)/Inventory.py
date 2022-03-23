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
            if guitarSpec.matches(serachedGuitar):
                matched_guitar.append(guitar)
        return matched_guitar if bool(matched_guitar) else None  
if __name__ == '__main__':
    guiterIWant = GuitarSpec(Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD, 12)
    MyInventor = Inventor()
    spec = GuitarSpec(Builder.GIBSON , 'model2' , Type.ACOUSTIC , Wood.CADER , Wood.SITKA , 13)
    MyInventor.addGuiter('1234' , 1250 , spec)
    slectedGuiter = MyInventor.getGuiter('1234')
    print(slectedGuiter.getPrice()) #1250
    print(MyInventor.search(guiterIWant)) #None
    spec = GuitarSpec(Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD , 12)
    MyInventor.addGuiter("234100" , 3000 , spec)
    spec = GuitarSpec(Builder.FENDER , 'stratcoster' , Type.ELECTRIC, Wood.ALDER , Wood.BRAZILIAN_ROSWOOD , 10 )
    MyInventor.addGuiter('5456' , 1562 ,  spec)
    res = MyInventor.search(guiterIWant)
    if res !=None :
        print("matched guiter are :")
        for match in res :
            print(" "*2 ,"serial number :"+match.getSerialNumber() , 'price' , match.getPrice() , sep = " ")
    else :
        print("not found !")
