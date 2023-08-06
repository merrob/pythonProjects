class Product:
    def __init__(self,pYield,pTime,pMachine,pRecipe):
        self.dyield = pYield
        self.dRecipe = pRecipe
        self.dTime = pTime
        self.dMachine = pMachine

recipeBook = {
"blue" : Product(1,3,"rCenter",{"mCoil":1,"cBoard":1}),
"mCoil" : Product(2,1,"Constructor",{"magnet":2,"cIngot":1}),
"cBoard" : Product(2,1,"Constructor",{"iIngot":2,"cIngot":1}),
"iIngot" : Product(1,1,"Smelter",{"ironOre":1}),
"cIngot" : Product(1,1,"Smelter",{"copperOre":1}),
"magnet" : Product(1,1.5,"Smelter",{"ironOre":1}),
"red" : Product(1,6,"rCenter",{"eGraphite":2,"Hydrogen": 2}),
"eGraphite" : Product(1,2,"Smelter",{"Coal":2})}

machineBook = {
    "Smelter" : 0.36,
    "Constructor" : 0.54,
    "rCenter" : 0.48 
}
finalResources = ["ironOre","copperOre","Coal","Hydrogen"]
order = {}
machines = {}
storage = {}
power = 0

quant = 1800
minput = recipeBook.get("blue")
#calculates number of machines needed
def num_machines(mQuant,mTime):
    mMachines = mQuant/(60/mTime)
    return mMachines

def calcResources(mTarget,mQuant):
    #get recipe
    calcorder = {}
    recipe = recipeBook.get(mTarget)
    mat_needed = mQuant/recipe.dyield
    for ingredient in recipe.dRecipe:
        if ingredient in calcorder:
            currentIngredient = calcorder[ingredient]
            newIngredient = currentIngredient + mat_needed*recipe.dRecipe[ingredient]
            calcorder.update({ingredient : newIngredient}) 
        else:
            calcorder.update({ingredient : mat_needed*recipe.dRecipe[ingredient]})
    return calcorder


order = {"blue":1800}

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
            

            if "Ore" in oItem:
                continue
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


