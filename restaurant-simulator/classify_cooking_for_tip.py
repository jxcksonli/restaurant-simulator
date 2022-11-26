meal_details = input() 
options = []
default_menu = [['Budda Bowl (vg)',25,20,10,3],['Eye Fillet Steak',55,25,7,1],['Spaghetti Bolognese',30,22,40,5],['Pad Thai (seafood)',22,17,30,1]]
default_status = False 

if meal_details == '.':
    MealNo_and_ActCookTime = input() #Asks for meal number and actual cook time
    cook_time = int(MealNo_and_ActCookTime.split(',')[1]) #Split to obtain cook time, realisitic time and standard deviation and store in a list
    realistic_cook_time = int(default_menu[int(MealNo_and_ActCookTime.split(',')[0]) - 1][3]) #Gets the meal number (from string) then search that index for the time through [3]
    standard_dev = int(default_menu[int(MealNo_and_ActCookTime.split(',')[0]) - 1][4])
    default_status = True

while meal_details != '.':
    details = {'name':'', 'sell_for': '', 'cost_to_make': '', 'cook_time': '', 'cook_time_stdev': ''}
    details['name'] = meal_details.split(',')[0]
    details['sell_for'] = float(meal_details.split(',')[1])
    details['cost_to_make'] = float(meal_details.split(',')[2])
    details['cook_time'] = float(meal_details.split(',')[3])
    details['cook_time_stdev'] = float(meal_details.split(',')[4])
    options.append(details) #Adds the dictionary into the empty list
    meal_details = input() #Will keep asking after for meal details unless a '.' is inputted
    if meal_details == '.':
        MealNo_and_ActCookTime = input() 
        cook_time = float(MealNo_and_ActCookTime.split(',')[1])
        realistic_cook_time = float(options[int(MealNo_and_ActCookTime.split(',')[0]) - 1]['cook_time'])
        standard_dev = float(options[int(MealNo_and_ActCookTime.split(',')[0]) - 1]['cook_time_stdev'])

#Calculates cook status based on average cooking time and standard deviation of the time
if cook_time < realistic_cook_time - 2*standard_dev:
    cook_status = "very undercooked"
    tip_status = "-100%"
elif cook_time >= realistic_cook_time - 2*standard_dev and cook_time <= realistic_cook_time - standard_dev:
    cook_status = "slightly undercooked"
    tip_status = "0%"
elif cook_time > realistic_cook_time - standard_dev and cook_time < realistic_cook_time + standard_dev:
    cook_status = "well cooked"
    tip_status = "10%"
elif cook_time >= realistic_cook_time + standard_dev and cook_time <= realistic_cook_time + 2*standard_dev:
    cook_status = "slightly overcooked"
    tip_status = "0%"
elif cook_time > realistic_cook_time + 2*standard_dev:
    cook_status = "very overcooked"
    tip_status = "-100%"

if default_status: #Prints default menu bit
    print(f"{default_menu[int(MealNo_and_ActCookTime.split(',')[0])-1][0]} was {cook_status} and cooking tip was {tip_status}")
else: #Else if not default, prints manual menu bit
    print(f"{options[int(MealNo_and_ActCookTime.split(',')[0])-1]['name']} was {cook_status} and cooking tip was {tip_status}")