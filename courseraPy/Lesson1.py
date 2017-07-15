#%%
def name():
    """ This function takes all details from
    a person and prints it"""
    firstName = input("Enter your first name :")
    lastName = input("Enter your last name :")
    city = input("Enter your city :")
    nation = input("Enter your nation :")
    print("Your name is :",firstName+" "+lastName)
    print("You live in :",city," , ",nation)
    
#%%
def testIf():
    """ This is to test If """
    print("Testing if condition")
    number = int(input("Enter a number : "))

    if( number > 0):
        print("number is positive and it's valus is ",number)
    elif(number < 0):
        print("number is negative and it's value is ",number)
    else:
        print("number is zero")
#%%
def testWhile():
    """ This is to test while and break"""
    while True:
        number = int(input("Enter 999 to exit. Enter any number"))
        if(number == 999):
            break       
        elif(number > 0):
            print("number is positive and it's value is ",number)
        elif(number < 0):
            print("number is negative and it's value is ",number)
        else:
            print("number is zero")
            
#%%
def testEquals():
    """ This method test equals"""
    while True:
        print("If you enter 999, program exits")
        
        number1 = input("Enter first number : ")
        
        while True:
            ##if(not(number1) or not(number1.isdigit())):
            if(isNumberValid(number1)):
                break
            else:
                number1 = input("Enter valid number : ")
        
        number2 = input("Enter second number : ")
        
        while True:
            ##if(not(number2) or not(number2.isdigit())):
            if(isNumberValid(number2)):
                break
            else:
                number2 = input("Enter valid number : ")
            
        number1 = int(number1)
        number2 = int(number2)
        
        
        if((number1 == 999) or (number2 == 999)):
            print("Program is exiting")
            break
        else:
            if(number1 == number2):
                print("Numbers you have entered are equal")
            else:
                print("Numbers you have entered are not equal")
    ##print(isNumberValid(12))
    
#%%
def isNumberValid(number):
    """ This is utility mentod to test if number is proper """    
    if(not(number) or not(number.isdigit())):
        ##print("return false")
        return False
    else:
        ##print("return true")
        return True
#%%
    isNumberValid('89y')
#%%
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    