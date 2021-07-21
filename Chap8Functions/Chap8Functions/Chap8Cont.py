#8-5
def plants (plant_name, plant_type):
    """Records plant type and name"""
    print (f"\n{plant_name.title()} is a {plant_type}. \n")

plants (plant_name= 'Jane', plant_type= 'Pothos')

#8-6
plantid = ""
plant = ""
info = ""

def plant (type, age, name= ''):
    """Records plant type, age, and name."""
    if name:
        plantid = f"{type} {age} {name}"
    else:
        plantid = f"{type} {age}\n"
    return plantid.title ()
info = plant ('christmas cactus,', 'fifteen,','ruby')
print (info)
info = plant ('aloe', 'five')
print (info)

#8-7

formatted = ''
Ttype = ''
tree = ''

prompt = 'This will record the tree type and climate. '
prompt += 'Enter "quit" to exit.'

def trees (type, climate):
    """Records tree type, climate found."""
    formatted = f"{type} {climate}"
    return formatted.title()

while Ttype != 'quit':
    print (prompt)
    Ttype = input ('Please enter tree type: ')
    Tclimate = input ('Please enter climate of region: ')
    
    tree = trees (Ttype, Tclimate)
    print (f"{tree}\n")
    Ttype = input ('Would you like to run program again?')