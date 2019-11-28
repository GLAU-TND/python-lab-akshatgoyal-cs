try:
    a=7
    b="pyth"
    c=a+b
except TypeError:
    print("Type Error occured")
else:
    print('Sucsses no error!')
try:
    print(float("Python"))
except ValueError:
    print("Value Error Occured")
else:
    print("N0 error!")

class Attributes(object):
          a=2
          print(a)
try:
    object=Attributes()
    print(object.Attribute)
except AttributeError:
    print("Attribute error occured")
          
