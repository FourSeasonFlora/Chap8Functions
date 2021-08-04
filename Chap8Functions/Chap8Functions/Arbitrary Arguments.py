Bread = ['White', 'Wheat']
CustomerBread = ''
CustomerSandwich = ''
Ingredients = []
DisplayingSandwich = ''
Ingredient = ''

#Sandwich builder. Exercise 12-14
def MakingSandwiches (Bread, Ingredients):
    """Summarizes the sandwich requested."""
    print (f'We have {Bread} available today.')
    Ingredients.append (input ('Please enter your bread selection: '))
    Ingredients.append (input ('Please provide the items you would like on your sandwich: '))
    
def DisplayingSandwich (Ingredients):
    for Ingredient in Ingredients:
        print (Ingredient)

MakingSandwiches (Bread, Ingredients)
DisplayingSandwich (Ingredients)