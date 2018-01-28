--------------------------------------------
Simple demo of Default Arguments
1.You dont have to pass args
2.you can pass one arg with no keyword argument
3.you can pass one/two keyword args
4.you can pass dictonary to unpack. But use "**" to unpack dictonary

def calc(a = 20,b = 30):
...     print('Addition is ',(a + b))
calc() 
Addition is  50
calc(50)
Addition is  80
calc(b = 80)
Addition is  100
dict = {'a' : 70, 'b' : 80}
calc(**dict)
Addition is  150

--------------------------------------------
>>> def xlist(argList):
...     for x in argList:
...          print(x,end = ',')
xlist([4,9,67])
4,9,67,
r = [2,5,6]
xlist(r)
2,5,6,
--------------------------------------------
range and list can be passed  as an argument where a function defines list as param
>>> def add(list):
...     total = 0
...     for x in list:
...         total = total + x
...     return total
... 
>>> add([4,5,8])
17
>>> add(range(1,10))
45
--------------------------------------------
To define arbitrary params use "*".
If you define varargs as param , then list has to be unpacked to be send as argument
If you define list as param, then don't unpack list, send as the list as it is

>>> def addArbitary(*nums):
...     total = 0
...     for x in nums:
...         total = total + x
...     return total
...
addArbitary(10,20,45)
75
list = [12,45,89]
addArbitary(*list)
146
--------------------------------------------
You can unpack list when passing as argument, provided the size of the list matches the numbers
of params defined in the funtion

 def addNums(a,b,c):
...    return a + b+ c
... 
v = [45,78,90]
addNums(*v)
213
--------------------------------------------


>>> def testvarArgs(**args):
...     for key in args:
...         print(args[key])
...
testvarArgs(a = 'apple')
apple
testvarArgs(a = 'apple',b = 'ball')
apple
ball
dict = {'a':'Apps','b':'Baps'}
testvarArgs(**dict)
Apps
Baps
--------------------------------------------
Lambda :
>>> list = [12,45,67,34,90,37]
list.sort()
list
[12, 34, 37, 45, 67, 90]
>>> list.sort(key = lambda x : x)
>>> list
[12, 34, 37, 45, 67, 90]
>>> list.sort(key = lambda x : -x)
>>> list
[90, 67, 45, 37, 34, 12]
--------------------------------------------
List/Stack
>>> list = [1,2,3]
>>> type(list)
<class 'list'>
>>> set = {1,2,3,2}
>>> type(set)
<class 'set'>
>>> set
{1, 2, 3}
>>> tuple = (1,2,3,2)
>>> type(tuple)
<class 'tuple'>
>>> tuple
(1, 2, 3, 2)
>>> range = range(1,4)
>>> type(range)
<class 'range'>
>>> range
range(1, 4)
>>> dict = {1:'one',2:'two',3:'three'}
>>> type(dict)
<class 'dict'>
>>> dict
{1: 'one', 2: 'two', 3: 'three'}
>>> from collections import deque
>>> queue = deque([1,2,3,1])
>>> type(queue)
<class 'collections.deque'>
>>> queue
deque([1, 2, 3, 1])
--------------------------------------------


