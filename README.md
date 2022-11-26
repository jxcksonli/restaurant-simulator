# restaurant-simulator
A simple Python restaurant simulator that was completed as part of a school assignment in first semester of degree

1. Interpretating a list of meals\
get_meal.py takes input from the user representing meal information and store these internally. The information consists of name, price, costs to make, cook time etc. Other information can be added through a key-value pair in the dictionary.\
For example, an input of:\
Lamb Madras,25.49,17,10,3\
Lentil Lasagne,22,16.5,30,5\
.\
Will output:\
[{'name': 'Lamb Madras', 'sell_for': 25.49, 'cost_to_make': 17.0, 'cook_time': 10.0, 'cook_time_stdev': 3.0}, {'name': 'Lentil Lasagne', 'sell_for': 22.0, 'cost_to_make': 16.5, 'cook_time': 30.0, 'cook_time_stdev': 5.0}]

2. Displaying the menu\
get_menu.py can either receive a list of menu in the manner in Part.1 or receive a period '.' (indicating a default menu). This file will print off the menu for the user listing the meals in the order they were inputted and follow a specific format.\
For example, an input of:\
Lentil Lasagne,22,16.5,30,5\
Lamb Madras,25.49,17,10,3\
.\
Will output:\
'1. Name:Lentil Lasagne Sells:$22.0 Costs:$16.5 Takes:30.0 mins\
'2. Name:Lamb Madras Sells:$25.49 Costs:$17.0 Takes:10.0 mins

3. User selecting a meal option\
customer_selection.py utilises the previous program to receive a list of menu items, then allows the user to enter a meal selection number which matches the number shown when displaying the menu. There will be appropriate validation on the user response.\
For example, an input of:\
.\
4\
Will output:\
now cooking Pad Thai (seafood)\
And an input of:\
.\
Spaghetti Bolognese\
Will output:\
invalid choice

4. Classifying cooking time and determine the tip the customer pays\
classify_cooking_for_tip.py uses Part.1 in determining the tip a customer pays based on the cooking time involving the mean cooking time and the standard deviation. Then at the end it will print out the cooking category and the cooking tip.\
For example, an input of:\
.\
2,40\
Will output:\
Eye Fillet Steak was very overcooked and cooking tip was -100%

5. Using uniform and normally distributed random numbers for cooking time and additional tips\
random_tips.py uses the random library that takes an input of a cooking time and a cooking time standard deviation then performs a normal distribution. This value is then used as the cooking time. A random tip is similarly determined using the random library.\
For example, an input of:\
10000,5000\
Will output: (Random)\
Actual cooking time was 13016.476351274048 and the tip paid was 5%

6. Restaurant Simulator\
restaurant_simulator.py incorporates all previous parts of the assignments and includes the calculation of profit on a meal, the retrial of cooking a meal up to twice if it is very over or undercooked and repeat all the previous steps of n number of customers and accumulating the profit.
