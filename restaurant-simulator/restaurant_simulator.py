import random

def get_meals_list_from_user(): 
    options = [] 
    default_menu = [['Budda Bowl (vg)',25,20,10,3],['Eye Fillet Steak',55,25,7,1],['Spaghetti Bolognese',30,22,40,5],['Pad Thai (seafood)',22,17,30,1]]
    meal_details = input() 
    if meal_details == '.': #If meal details is '.', the default menu is printed
        for i in range(len(default_menu)): #For loop to ensure all meals in default menu are entered
            defaults = {'name':'', 'sell_for': '', 'cost_to_make': '', 'cook_time': '','cook_time_stdev': ''}
            defaults['name'] = default_menu[i][0]
            defaults['sell_for'] = float(default_menu[i][1])
            defaults['cost_to_make'] = float(default_menu[i][2])
            defaults['cook_time'] = float(default_menu[i][3])
            defaults['cook_time_stdev'] = float(default_menu[i][4])
            options.append(defaults) #Adds the default meals into the options list (if default menu is chosen)
        return options #Returns the options if only default menu is chosen
    
    while meal_details != '.': #While loop to ensure as many meals can be entered (whilst not '.')
        details = {'name':'', 'sell_for': '', 'cost_to_make': '', 'cook_time': '','cook_time_stdev': ''}
        details['name'] = meal_details.split(',')[0]
        details['sell_for'] = float(meal_details.split(',')[1])
        details['cost_to_make'] = float(meal_details.split(',')[2])
        details['cook_time'] = float(meal_details.split(',')[3])
        details['cook_time_stdev'] = float(meal_details.split(',')[4])
        options.append(details) #This adds all the individual inputs into a dictionary and stores it into the list
        meal_details = input()
    return options #Returns all the manually inputed meals and stores it into the list

def display_menu(options):
    for i in range(len(options)): #Utilising a for loop to display the menu
        print(f"{i+1}. Name:{options[i]['name']} Sells:${options[i]['sell_for']} Costs:${options[i]['cost_to_make']} Takes:{options[i]['cook_time']} mins")

def validate_user_choice(options, users_input):
    valid_choice = False
    if users_input.isdigit() and int(users_input) > 0 and int(users_input) <= len(options):
        valid_choice = True #Valid Choice only if input is digit AND a number on the menu list
    return valid_choice

def classify_cook_time(average_cook_time, stdev_cook_time, actual_cook_time):
#Using mean and standard deviation to classify cooking
    if actual_cook_time < (average_cook_time - 2*stdev_cook_time):
        classification = "very undercooked"
    elif (average_cook_time - 2*stdev_cook_time) <= actual_cook_time <= (average_cook_time - stdev_cook_time):
        classification = "slightly undercooked"
    elif (average_cook_time - stdev_cook_time) < actual_cook_time < (average_cook_time + stdev_cook_time):
        classification = "well cooked"
    elif (average_cook_time + stdev_cook_time) <= actual_cook_time <= (average_cook_time + 2*stdev_cook_time):
        classification = "slightly overcooked"
    elif actual_cook_time > (average_cook_time + 2*stdev_cook_time):
        classification = "very overcooked"
    return classification

def get_cooking_tip(classification, base_tip):
#Based on the classification, a certain amount of cooking tip will be given
    if classification == "very undercooked":
        final_cooking_tip = -100
    if classification == "slightly undercooked":
        final_cooking_tip = 0
    if classification == "well cooked":
        final_cooking_tip = base_tip #Like this??
    if classification == "slightly overcooked":
        final_cooking_tip = 0
    elif classification == "very overcooked":
        final_cooking_tip = -100
    return final_cooking_tip

def random_tip_compute(tip_chance, base_tip_value, random_comparison):
#Random Tips
    if random_comparison < tip_chance:
        base_tip_value = base_tip_value
    elif random_comparison > 1 - tip_chance:
        base_tip_value = -1 * base_tip_value
    else:
        base_tip_value = 0
    return base_tip_value

def order(options):
    print("Please enter your order. The options are given below")
    display_menu(options) #Prints the options in the menu
    meal_number = input("please enter a number to make your choice")

    while not validate_user_choice(options, meal_number):#Ensures user input is valid
        meal_number = input("please enter a number to make your choice")

    print("now cooking " + str(options[int(meal_number) - 1]['name'])) #Note index commences at 0, hence -1 is necessary otherwise we will print the wrong meal
    
    max_attempts = 3 
    profit_calc = []  #Lists to calculate the total profit
    for _ in range(max_attempts):   
        actual_cook_time = float(random.gauss(options[int(meal_number) - 1 ]['cook_time'],options[int(meal_number) - 1]['cook_time_stdev'])) #Random gauss given we have the mean (time) and standard deviation
        average_cook_time = float(options[int(meal_number) - 1 ]['cook_time'])
        stdev_cook_time = float(options[int(meal_number) - 1]['cook_time_stdev']) #Obtain variables to ensure the function below will run 
        classification = classify_cook_time(average_cook_time, stdev_cook_time, actual_cook_time) 
        print(f"{options[int(meal_number)-1]['name']} was {classification} ({round(actual_cook_time, 2)} vs {average_cook_time} mins)")
        base_tip = 10
        cooking_tip = get_cooking_tip(classification, base_tip)

        tip_num = random.random()
        tip_paid = random_tip_compute(0.1, 5, tip_num) #Calculates the tip paid (between 0 and 1 from random random) and uses default values as tests randomises the values
        print(f"cooking tip was {cooking_tip} random tip was {tip_paid} the random value being ({round(tip_num, 2)})")

        selling_price = options[int(meal_number) - 1]['sell_for']*(1+(cooking_tip+tip_paid)*0.01)
        if selling_price <= 0: #If the price turns below 0 (negative), we will turn it into $0
            final_selling_price = 0
        else:
            final_selling_price = round(float(selling_price),2) #Else the price will be rounded for readability purposes
        print(f"final selling price was ${final_selling_price}") #Print the final price
        
        profit = round(final_selling_price - options[int(meal_number) - 1]['cost_to_make'],2)
        profit_calc.append(profit) #Add the profit into the list
        overall_profit = sum(profit_calc) #Calculate the total profit
        print(f"for a profit of ${profit}")
        if classification != "very overcooked" and classification != "very undercooked":
            print("overall, the profit for this meal was $" + str(overall_profit)) #As long as it isnt very over/undercooked, print the overall profit and return the value
            return overall_profit
    print("giving up after 3 failed attempts") #If it cooks a very under/overcooked meal 3 times in a row, give up and return the overall profit still (as shown below)
    print(f"overall, the profit for this meal was ${overall_profit}")
    return overall_profit

def order_for_x_people(x):
    options = get_meals_list_from_user()
    running_total = 0
    orders = 0
    while orders < x: #Not less than or equal as it starts from 0
        running_total += order(options) #Adds the overall profit when it runs the order(options) function
        orders += 1
        print(f"running total ${round(running_total, 2)}") #Prints the running total value
    print(f"After serving meals to {x} people, we made a profit of ${round(running_total,2)}")
    return round(running_total,2) #And finally returns the running total value at the end of the function

if __name__ == "__main__":
    order_for_x_people(3)