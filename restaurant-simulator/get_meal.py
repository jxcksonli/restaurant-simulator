meal_details = input() #Gets the input of the meal details in order 
options = []
while meal_details != '.': #While '.' is not entered, the system will keep asking for the meal details
    details = {'name':'', 'sell_for': '', 'cost_to_make': '', 'cook_time': '', 'cook_time_stdev': ''}
    details['name'] = meal_details.split(',')[0] #Splits the input and assigns it as a dictionary value
    details['sell_for'] = float(meal_details.split(',')[1])
    details['cost_to_make'] = float(meal_details.split(',')[2])
    details['cook_time'] = float(meal_details.split(',')[3])
    details['cook_time_stdev'] = float(meal_details.split(',')[4])
    options.append(details) #Adds the details of the food into the options list
    meal_details = input() #Asks for next meal (if any)
print(options) #Prints the list of meals if '.' is entered