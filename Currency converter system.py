#Currency Converter in  PYTHON
def currency_converter(num,b):
            if b == "D":
                print("1 DOLLAR == 82 INR")
                return num*(1/82)
            elif b == "I":
                print("1 DIHRAM == 22 INR")
                return num*(1/22)
            elif b == 'Y':
                print("1 YUAN : 12 INR")
                return num*(1/12)
            elif b== "B":
                print("1 BAHT == 2.35 INR")
                return num*(1/2.35)
            elif b== 'P':
                print("1 POUND == 98 INR")
                return num*(1/98)
            elif b== 'S':
                print("1 SINGAPORE DOLLAR == 61 INR")
                return num*(1/150)

while True:
    a = input("Welcome to Currency Converter Station\n Press 'Y' to continue with this or else press 'N' to exit.\n")
    try:
        a == 'Y' or 'N'
    except:
        print("Please Enter the input acc. to given instructions.")
    if a=='Y':
        num = int(input("Enter the amount you want to convert : "))
        print("Indian Rupees can be convert into 'DOLLAR','DIHRAM','YUAN','BAHT','POUNDS','SINGAPORE DOLLAR'.")
        b = input("Enter the currency in  which you want to convert the indian rupees : [Press 'D' for DOLLAR, 'I' for DIHRAM , 'Y' for YUAN , 'B' for BAHT , 'P' for POUNDS, 'S' for SINGAPORE DOLLAR]\n.")
        try:
            b == "D"or"I"or"Y"or"B"or"P"or"S"
        except:
            print("Please enter the currency acc. to given instructions.")
        d = currency_converter(num,b)
        print(f"The {num}INR is {d}{b}.")
    else:
        print("Thank You and Have a nice day.")
        break
