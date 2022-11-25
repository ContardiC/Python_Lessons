#variabili
num=5
fruit="Mango"
lettera=fruit[0]
pi=3.14
print(num)
print(fruit)
print(lettera)
print(pi)

#Many Values to Multiple Variables

animal1, animal2, animal3="Cat","Dog","Otter"
print(animal1)
print(animal2)
print(animal3)

#One Value to Multiple Variables

animal1=animal2=animal3="Cat"
print(animal1)
print(animal2)
print(animal3)

#Unpack a Collection
animals=["Cat","Dog","Otter"]
animal1,animal2,animal3=animals
print(animal1)
print(animal2)
print(animal3)

#Output Variables

msg="The Cat say:"
print(msg)
statement="HELLO!"
print(msg,statement)

num1=5
num2=10
print(num1+num2)

print(msg,num1)

#global variables

statement="MEOW"
def sayMeow():
    print("PuffoGino say:",statement)

sayMeow()

print("Nino say: ", statement)


def message():
    global txt
    txt="awesome"
    print("The cats are", txt)

message()

print("The otters are", txt)