# weight=int(input("Enter your weight\n"))
# unit=input("(L)bs or (K)gs\n")
# if unit=="k" or unit=="K":
#     print(f"Your weight is {0.45*weight}lbs")
# elif unit=="L"or unit=="l":
#     print(f"Your weight is {weight/0.45}kgs")
# else:
#     print("Wrong input")       
                                                        #!Better Method

weight=int(input("Enter your weight\n"))
unit=input("(L)bs or (K)gs\n")
if unit.upper()=="K": #.upper() converts whatever the user enters to capital case and hence case sensitivity is no longer an issue
    print(f"Your weight is {0.45*weight}lbs")
elif unit.upper()=="L":  #.upper() converts whatever the user enters to capital case and hence case sensitivity is no longer an issue
    print(f"Your weight is {weight/0.45}kgs")
else:
    print("Wrong input")     






