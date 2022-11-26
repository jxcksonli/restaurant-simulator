meal_details = input() #Asks for the meal details
options = [] 
default_menu = [['Budda Bowl (vg)',25,20,10,3],['Eye Fillet Steak',55,25,7,1],['Spaghetti Bolognese',30,22,40,5],['Pad Thai (seafood)',22,17,30,1]] 

if meal_details == ".": #If meal detail is '.', print the default menu
    for i in range(len(default_menu)):
        print(f"{i+1}.Name: {default_menu[i][0]} Sells:${float(default_menu[i][1])} Costs:${float(default_menu[i][2])} Takes:{float(default_menu[i][3])} mins")

while meal_details != '.': #If '.' is not entered, we will assume the inputs given by the user are meal details 
    details = {'name':'', 'sell_for': '', 'cost_to_make': '', 'cook_time': '','cook_time_stdev': ''}
    details['name'] = meal_details.split(',')[0]
    details['sell_for'] = float(meal_details.split(',')[1])
    details['cost_to_make'] = float(meal_details.split(',')[2])
    details['cook_time'] = float(meal_details.split(',')[3])
    details['cook_time_stdev'] = float(meal_details.split(',')[4])
    options.append(details) #This adds the dictonary into the list 
    meal_details = input() #Keeps asking for input until a '.' is received

for i in range(len(options)):#For loop to print the number of inputs given in a format string
    print(f"{i+1}. Name:{options[i]['name']} Sells:${options[i]['sell_for']} Costs:${options[i]['cost_to_make']} Takes:{options[i]['cook_time']} mins")