zoo = ("zebra", "emu", "squirrel") #Create a tuple named zoo that contains your favorite animals.

zoo.index("zebra") #Find one of your animals using the .index(value) method on the tuple.

print zoo.index("zebra")

for x in zoo: #Determine if an animal is in your tuple by using for value in tuple.

  if x == "zebra":

    print x

    (zebra, emu, squirrel) = zoo #Create a variable for each of the animals in your tuple with this cool feature of Python.
    print(zebra)

zooList = list(zoo) #Convert your tuple into a list.

zooList.extend(["penguin", "monkey", "giraffe"]) #Use extend() to add three more animals to your zoo.

print zooList

zooTuple = tuple(zooList) #Convert the list back into a tuple.
print zooTuple
