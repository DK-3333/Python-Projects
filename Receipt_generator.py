# Indian Kirana Store Calculator & Receipt Generator
"Write a python program which will keep adding a stream of numbers inputed by the user.The adding stops as soon as user presses q key on the keyboard."
sum = 0
c = [] 
while True:
    a = input("Enter The Item Price or press q to quit: ")
    if (a!="q"):
        b = int(a)
        sum = sum + b
        c.append(b)
    
    else:
        print(f"Total Bill Amount is  : {sum}")
        print("Thanks for using our calculator.")
        break

print(f"Bill Summary : {c}")






 




