from Guitar import Guiter
class Inventor:
    global guitars
    guitars = list()
    def addGuiter(self , serialNumber :str , Price :float , builder :str , model:str , type:str , bacWood:str , topWood:str)->None:
        guiter = Guiter(serialNumber  , Price  , builder  , model , type , bacWood , topWood)
        guitars.append(guiter)
        return None
    def getGuiter(self , serialNumber:str)->Guiter or None:
        for guiter in guitars:
            if guiter.getSerialNumber()==serialNumber:
                return guiter
        return None 
    def search(self , serachedGuitar:Guiter)->Guiter or None:
        for guitar in guitars:
            builder = guitar.getBuilder()
            if builder != serachedGuitar.getBuilder() and builder not in ['' , None]:
                continue
            model = guitar.getModel()
            if model!=serachedGuitar.getModel() and model not in ['' , None]:
                continue
            type =  guitar.getType()
            if type != serachedGuitar.getType() and type not in ['' , None]:
                continue
            backWood =  guitar.getBackWood()
            if backWood != serachedGuitar.getBackWood() and backWood not in ['' , None]:
                continue
            topWood = guitar.getTopWood()
            if topWood != serachedGuitar.getTopWood() and topWood not in ['' , None]: 
                continue
            #it will execute if all condition before are false that means all features are equal
            print("it founded")
            return guitar
                
        return None 

guiterIWant = Guiter('1234' , 120 , 'fender' , 'stratcoster ' , 'electric' , 'Alder' , 'Alder')
MyInventor = Inventor()
MyInventor.addGuiter('1234' , 1250 , 'egypt' , 'model2' , 'electric' , 'lblb' , 'lblb')
slectedGuiter = MyInventor.getGuiter('1234')
print(slectedGuiter.getPrice()) #1250
print(MyInventor.search(guiterIWant)) #None
MyInventor.addGuiter('5456' , 1562 , 'fender' ,'stratcoster ' , 'electric' , 'Alder' , 'Alder' )
print(MyInventor.search(guiterIWant))
