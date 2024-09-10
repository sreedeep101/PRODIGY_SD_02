from random import randint 

random_int=randint(0,10)
prediction=int(input("enter your prediction\n(in between 0 to 10)\n"))
if random_int == prediction:
    print("\nyour prediction is correct\n")
    print("you won\n")
elif random_int != prediction:
    print("\nWrong prediction\n")
    print("you loss...\n")
    print(f"the correct randomnumber is {random_int}")
