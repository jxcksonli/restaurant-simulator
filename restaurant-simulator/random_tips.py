import random 

cooking_info = input() #Enters cooking time and its standard deviation as a string
cooking_list = cooking_info.split(",") #Splits the string and stores it into a list
approx_cook_time, cook_dev = int(cooking_list[0]), int(cooking_list[1])
cook_time = random.gauss(approx_cook_time,cook_dev) #Performs a normal distribution calculation based on mean and st.dev
tip_num = random.random() #Produces a random number between 0 and 1 to determine the value of the tip given
tip_paid = None

if tip_num <0.1: 
    tip_paid = 5
elif  0.1 <= tip_num <= 0.9:
    tip_paid = 0
elif 0.9 < tip_num <= 1:
    tip_paid = -5
print(f"Actual cooking time was {cook_time} and the tip paid was {tip_paid}%") #Prints resulting cooking time and tip paid
