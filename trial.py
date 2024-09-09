'''
Lambda fucntions.

when defining funciton and methods in python typically requires use of the def keyword and a specific name that we can use 
to invokde it lateron.
this syntaz allows us to specify many things like the data types default values, keyword argument and so on.
 
pyhotn provides us with an alternatie for simpel cases like thses.
 the lambda keyword.

 for example say we wanted to to ass 12 to a value as mentioneed above we could write a lambda function like this
'''

new_dozen = lambda n :n + 12

'''
when we invoke new_dozen() on a new number n, out lambda function will add 12 to the total.
lambda fucntion are small anonymous functions that can take any number of arguments and manipulate then in a way that can be carried out in a single line in python code.
'''

# Functions are first class objects. 
'''
while there are a nunmber of casese where it males more sende to define a lambda thatn write n+12 over and over again, 
th real power in lamndas comes firm our ability to pass them as arguments to and return them from other functions.
imagine we wanted t ocreate a fucntion that would add any specific number when invoked 
we could write lamndas for each new number or we could trat our lambdas asa first class object and manipulate it inside of another function.
'''

def myfunc(x):
    return lambda n :n + x 
new_centurry = myfunc(900)

print(new_centurry(4900))

# when to use lambda
'''
they are typically used as arguments and return cvalues certain built-in fucntions like sorted(), take a function key as an argument to determine which values to sort.
'''
my_list = [['red', 'truck','caroline'], ['blue', 'truck', 'gabriel'],['red','sedan','zoey']]
print(sorted(my_list, key = lambda v: v[2], reverse = True)) # this sorts our list by the values at index 1 the type of vehicle with the added option to sort in ascending or descendng (reverse = True)

# explanation for the above code.
'''
my_list - this is a list of list s where each onner list contains wtwo elements, a color and a vehicle type.
2. sorted(my_list , key = lambda v : v[1])
       a) sorted() -> this is a bulut in python function that returns a new list contianing all items from the original list in ascending order.
       b) key = lambda v :v[1] is used to specify  afunction that will be applied to each element of my_list to determine the sorting order.
       c) lambda v:v[1] lambda created an anonymous fucntion without a name: v - represents each element of my_list(which in these case are themeselves lists):
          v[1] -> refers to the second element of each inner list (i.e the vehicle type)
'''

''' we can also return lambdas as new unique functions'''

def myfunc(x):
    return lambda a,b : (a +b ) * x

summation = myfunc(2)

print(summation(10, 20))