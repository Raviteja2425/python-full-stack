'''
import NewClassDay10
#print(dir(NewClassDay10))#dir will return all avialable methods
#print(type(NewClassDay10.data))
#print(type(NewClassDay10.details))

"""print(NewClassDay10.data)
print(NewClassDay10.details("Codegnan","Vizag"))"""

from NewClassDay10 import data
print(data)
print(data.keys())

data['marks']=[45,56,45,76,34]
print(data)

#print(details) it raises error as its not imported.

print(NewClassDay10.__doc__)#it returns the doc string (description)
'''


#We can also use * to get all methods/attributes
from NewClassDay10 import *
print(data)
print(details('Codegnan','Vizag'))




