#%%
# This is hello world function ctrl I inside def
def hello():
    """This function says Hello """
    print("Hello World")
    
#%%
def sayHi(name,company):
    """ Pass a name to say Hi """
    print("Hi There",name,". How is ",company,"?")
    
#%%
def checkQuote():
    """This checks Quote"""
    print("Hi, this is to tet 'quote'")
    print('This one as "well"')
#%%
sayHi("Anveshan","IBM")
#%%
def areaOfCircle(radius):
    """This function calculates area of circle"""
    area = (22/7)*radius**2
    print("Area of circle of radius",radius,"is ",area)
#%%
areaOfCircle(7)
#%%
def checkMixedQuote():
    """ This function displays single and double quotes"""
    print("My cat's name is \"Button\"")
#%%
def fahrenheit_to_celsius(temp):
    newTemp = 5*(temp - 32)/9
    print("Temperature in Fahreinheit , ",temp,end='')
    print("Temperature in celsius, ",newTemp)