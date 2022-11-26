meal_details = input()
options = []
use_default = False
default_menu = [['Budda Bowl (vg)',25,20,10,3],['Eye Fillet Steak',55,25,7,1],['Spaghetti Bolognese',30,22,40,5],['Pad Thai (seafood)',22,17,30,1]]

if meal_details == '.': #If '.' is entered, we use the default menu
    use_default = True

while meal_details != '.': #Manual meal inputs
    details = {'name':'', 'sell_for': '', 'cost_to_make': '', 'cook_time': '','cook_time_stdev': ''}
    details['name'] = meal_details.split(',')[0]
    details['sell_for'] = str(float(meal_details.split(',')[1]))
    details['cost_to_make'] = str(float(meal_details.split(',')[2]))
    details['cook_time'] = str(float(meal_details.split(',')[3]))
    details['cook_time_stdev'] = str(float(meal_details.split(',')[4]))
    options.append(details) #This adds all the individual inputs into a dictionary and the dictionary is added into the list
    meal_details = input()

try:
    cook_number = int(input("Select a meal")) #Asks for the number of the meal that the user wants
    if use_default:
        if cook_number <= len(default_menu) and cook_number > 0: #Ensures that the number inputted is on the menu
            print("now cooking " + default_menu[int(cook_number) - 1][0]) # Needs to -1 as lists starts at 0
        else: #If cook_number is out of bounds, print invalid choice
            print("invalid choice")
    else:
        if cook_number <= len(options) and cook_number > 0:
            print("now cooking " + options[cook_number - 1]['name']) 
        else:
            print("invalid choice")
except (TypeError, ValueError): #If the input is not a number, "invalid choice" will be printed out
    print("invalid choice")