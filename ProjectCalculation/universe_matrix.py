#first change for github
class Product:
    def __init__(self,pYield,pTime,pMachine,pRecipe):
        self.dyield = pYield
        self.dRecipe = pRecipe
        self.dTime = pTime
        self.dMachine = pMachine

recipeBook = {
#"product",Yield,ProductionTime,Machine,Ingredients,quantity
"Blue" : Product(1,3,"rCenter",{"mCoil":1,"cBoard":1}),
"Red" : Product(1,6,"rCenter",{"eGraphite":2,"Hydrogen": 2}),
"Yellow" : Product(1,8,"rCenter",{"Diamond":1,"tCrystal":1}),
"Purple" : Product(1,10,"rCenter",{"Processor":2,"pBroadband":1}),
"Green" : Product(2,24,"rCenter",{"gLens":1,"qChip":1}),
"White" : Product(1,15,"rCenter",{"Blue":1,"Red":1,"Yellow":1,"Purple":1,"Green":1,"Antimatter":1,}),
"Antimatter" : Product(2,2,"pCollider",{"cPhoton":1}),
"iIngot" : Product(1,1,"Smelter",{"ironOre":1}),
"cIngot" : Product(1,1,"Smelter",{"copperOre":1}),
"tIngot" : Product(1,2,"Smelter",{"tOre":2}),
"tCrystal" : Product(1,4,"Assembler",{"oCrystal":1,"tIngot":3}),
"hpSilicone" : Product(1,2,"Smelter",{"siliconOre":2}),
"eGraphite" : Product(1,2,"Smelter",{"Coal":2}),
"cNanotube" : Product(2,4,"cFacility",{"ssCrystal":6}),
"cSilicon" : Product(2,1.5,"Smelter",{"fSilicon":1}),
"gLens" : Product(1,6,"Assembler",{"Diamond":4,"sMatter":1}),
"sMatter" : Product(1,8,"pCollider",{"pContainer":2,"iIngot":2,"Deuterium":10}),
"pContainer" : Product(1,4,"Assembler",{"uMagnet":10,"cIngot":2}),
"Diamond" : Product(2,1.5,"Smelter",{"kOre":1}),
"Graphene" : Product(2,2,"cFacility",{"fIce":2}),
"Magnet" : Product(1,1.5,"Smelter",{"ironOre":1}),
"mCoil" : Product(2,1,"Assembler",{"Magnet":2,"cIngot":1}),
"cBoard" : Product(2,1,"Assembler",{"iIngot":2,"cIngot":1}),
"mComponent" : Product(1,2,"Assembler",{"hpSilicone":2,"cIngot":1}),
"Processor" : Product(1,3,"Assembler",{"cBoard":2,"mComponent":2}),
"qChip" : Product(1,6,"Assembler",{"Processor":2,"pFilter":2}),
"pFilter" : Product(1,12,"Assembler",{"cCrystal":1,"tGlass":2}),
"cCrystal" : Product(1,4,"Assembler",{"ogCrystal":8,"Graphene":2,"Hydrogen":12}),
"tGlass" : Product(2,5,"Assembler",{"Glass":2,"tIngot":2,"Water":2}),
"Glass" : Product(1,2,"Smelter",{"Stone":2}),

"pBroadband" : Product(1,8,"Assembler",{"cNanotube":2,"cSilicon":2,"Plastic":1}),
"Plastic" : Product(1,3,"cFacility",{"rOil":2,"eGraphite":1}),
"rOil" : Product(2,4,"rFacility",{"cOil":2}),
}

machineBook = {
    "Smelter" : 0.36,
    "Assembler" : 0.54,
    "rCenter" : 0.48,
    "cFacility" : 0.72,
    "rFacility" : 0.96,
    "pCollider" : 12
}
finalResources = ["ironOre","copperOre","Coal",
                  "Hydrogen","kOre","oCrystal",
                  "tOre","ssCrystal","fSilicon",
                  "cOil","uMagnet","Deuterium",
                  "ogCrystal","Water","Stone",
                  "siliconOre","fIce","cPhoton"]
order = {}
machines = {}
storage = {}
power = 0

#calculates number of machines needed
def num_machines(mQuant,mTime):
    mMachines = mQuant/(60/mTime)
    return mMachines

def calcResources(mTarget,mQuant):
    #get recipe
    calcorder = {}
    recipe = recipeBook.get(mTarget)
    try:
        mat_needed = mQuant/recipe.dyield
    except:
         print(mTarget)
    for ingredient in recipe.dRecipe:
        if ingredient in calcorder:
            currentIngredient = calcorder[ingredient]
            newIngredient = currentIngredient + mat_needed*recipe.dRecipe[ingredient]
            calcorder.update({ingredient : newIngredient}) 
        else:
            calcorder.update({ingredient : mat_needed*recipe.dRecipe[ingredient]})
    return calcorder


order = {"White":1800}

newOrder = {}
while True:
    print(f"your order is {order}")
    newOrder = {}

    if len(order) == 0:
        
        break
    for item in order:

        recipeItem = recipeBook.get(item)
        sub_order = calcResources(item, order[item])
        usedMachine = recipeItem.dMachine
        newMachines = num_machines(order[item],recipeItem.dTime)
        power = power + machineBook[usedMachine]*newMachines
        #checking if items in itemOrder already exist, and update the othersd
        if usedMachine in machines:
             newMachines = machines[usedMachine] + newMachines
             machines.update({usedMachine : newMachines})
        else:
             machines.update({usedMachine : newMachines})
        if item in storage:
                    currentItem = storage[item]
                    newItem = currentItem + order[item]
                    storage.update({item : newItem})

        else: 
                    storage.update({item : order[item]})

        
        for oItem in sub_order:
            
            if oItem in finalResources:
                if oItem in storage:
                    currentItem = storage[oItem]
                    newItem = currentItem + sub_order[oItem]
                    storage.update({oItem : newItem})
                else: 
                    storage.update({oItem : sub_order[oItem]})
                
            else:
                if oItem in newOrder:
                    currentItem = newOrder[oItem]
                    newItem = currentItem + sub_order[oItem]
                    newOrder.update({oItem : newItem})
                else: 
                    newOrder.update({oItem : sub_order[oItem]})


    order = newOrder
print(storage)
print(machines)
print(f"power used: {power}MW")


