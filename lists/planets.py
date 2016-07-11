
### Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto

planet_list = ["Mercury", "Mars"]
p_list = ["Uranus, Neptune"]


planet_list.append("Jupiter") #Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Saturn")
planet_list.extend(p_list) #Use the extend() method to add another list of the last two planets in our solar system to the end of the list.

planet_list.insert(1, "Venus") #Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(2, "Earth")
planet_list.append("Pluto") #Use append() again to add Pluto to the end of the list.
print planet_list

rocky_planets = []

rocky_planets = planet_list[0:4] #Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.

print rocky_planets

del planet_list[7] #Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.


print planet_list

probes = [ ( 'Cassini', 'Saturn'),
  ( 'Pathfinder', 'Mars'),
  ( 'Galileo', 'Jupiter'),
  ( 'Rocket', 'Sun'),
  ( 'Magellan', 'Venus') ]

print "we have visited.."
for p in planet_list: #Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.

  for pr in probes:

   visited = pr[1]


   if visited == p:

    print p




