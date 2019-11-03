name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
#inche = 2.54 cm
Nheight = 74 * 2.54 
weight = 180 # lbs
# 1lbs= . 454 kg
Nweight = 180 * .454
eyes = ' Blue'
teeth = 'White'
hair =  'Brown'
print(f"lets talk bout {name}.")
print(f"He's {Nheight} cm tall.")
print(f"He's {Nweight} kg heavy.")
print("actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right)
total = age + Nheight + Nweight
print(f"If I add {age} , {Nheight}, and {Nweight} I get {total}.")
