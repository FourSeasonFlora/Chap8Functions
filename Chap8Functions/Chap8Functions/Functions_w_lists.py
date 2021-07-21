#8-6
users_location = ""
city = ""
state = ""
user_response = ""

prompt = "Thank you for using MyCity recorder. "
prompt += "Enter 'exit' to leave program. "

def print_citystate (city, state):
    """Accepts users city and state. Returns input."""
    users_location = f"{city}, {state}"
    return users_location.title()

user_response = input (prompt)

while user_response != 'exit':
    city = input ("\nPLease enter your city: ")
    state = input ("\nPlease enter your state: ")

    location = print_citystate (city,state)
    print (f"\nYou have provided {location}.")
    user_response = input ("Would you like to run the program again? Or enter 'exit' to leave the program. ")

#8-7
make = ""
model =""
vehicle = ""
UserMake =""
UserModel = ""

def GetCars (make, model):
    "Returns make and model of car user provided."
    vehicle = {'make': make, 'model': model,}
    return vehicle

UserMake = input ("\nPlease provide the make of your car: ")
UserModel = input ("\nPlease provide the model of your car: ")

UserVehicle = GetCars (UserMake, UserModel)

print (UserVehicle['make'])