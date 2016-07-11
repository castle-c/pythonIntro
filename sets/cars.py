showroom = set(["z3 coupe", "911", "elise", "f50"])

showroom.add("f50") # Pick one of the items in your show room and add it to the set again. Notice still one instance of item
showroom.update(set(["stingray","viper"])) #Using update(), add two more car models to your showroom with another set.
showroom.discard("911") # You've sold one of your cars. Remove it from the set with the discard() method.


junkyard = set(["accord", "cube", "focus", "elise", "f50"])

sameCar = junkyard.intersection(showroom) #use the intersection method to see which cars exist in both the showroom and that junkyard.

boughtCars = junkyard.union(showroom) #Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
boughtCars.discard("911") # Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
boughtCars.discard("viper")
boughtCars.discard("elise")
boughtCars.discard("f50")
boughtCars.discard("z3 coupe")
boughtCars.discard("stingray")
print showroom
print boughtCars



