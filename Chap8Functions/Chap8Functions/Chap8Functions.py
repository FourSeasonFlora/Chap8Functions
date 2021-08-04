#8-1
def holiday():
    """Displaying winter holidays."""
    print ('Samhain', 'Thanksgiving', 'Yule')

holiday()

#8-2

def holidays (winter):
    """Displaying winter holidays."""
    print (f"\n{winter.title()} is the best winter holiday!")

holidays ('Yule')

#8-3
def plant_care (sunlight, climate):
    """Displaying plant sunlight and climate requirements."""
    print (f'\nThis plant requires {sunlight} sunlight.')
    print (f'\nThis plant prefers {climate} temperatures.')

plant_care ('full', 'hot')
plant_care ('low', 'humid')

#8-4
def growing_conditions (light, temperature):
    """Plant growing recommendations"""
    print (f'\nThis plant needs {light}light.')
    print (f'\nThis plant needs {temperature} temperature.')
growing_conditions (light= 'low', temperature= 'humid')