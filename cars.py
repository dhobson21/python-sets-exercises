#Create an empty set named showroom.
show_room = set()

# Add four of your favorite car model names to the set.
show_room = {'mustang', 'f150', 'rav4', 'corvette'}

# Print the length of your set.
print(len(show_room))

# Pick one of the items in your show room and add it to the set again.

show_room = {'mustang', 'f150', 'rav4', 'corvette', 'f150'}

# Print your showroom. Notice how there's still only one instance of that model in there.
print(show_room)

#Using update(), add two more car models to your showroom with another set.

new_car = set()
new_car = {'camry', 'maxima'}
show_room.update(new_car)
print(show_room)
# You've sold one of your cars. Remove it from the set with the discard() method.
show_room.discard('corvette')
print(show_room)

#Acquiring more cars
#Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junk_yard = set()
junk_yard = {'f150', 'bug', 'el camino', 'oddesy', 'ultima', 'rav4'}

#Use the intersection method to see which cars exist in both the showroom and that junkyard.
print(show_room.intersection(junk_yard))

#Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
all_cars = show_room.union(junk_yard)
print(all_cars)
#Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
all_cars.discard('bug')
all_cars.discard('oddesy')
all_cars.discard('el camino')
all_cars.discard('bug')
print(all_cars)