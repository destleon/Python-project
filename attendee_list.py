# more examples of lists
myfriends = [ 'berla', 'lois', 'benita', 'andrea', 'venny', 'abena', ]
# to add a new friend to the list,
myfriends.append('jessica') # ijust added jessica to the list
print(myfriends)
#to arrange the names in alphabetical order
myfriends.sort()
print(myfriends)

# i want to replacy andrea with babara
myfriends[1] = 'babara'
print (myfriends)

# another way of doing 
myfriends.insert(1,'babara1')
print(myfriends)

# to remove some of my friends
del myfriends[1]
print(myfriends)

#removing the last friend using pop
myfriends.pop()
print(myfriends)

#what if i don't know the position of the item i want to remove ? i then use remove
myfriends.remove("lois")
print(myfriends)
print("your friends have reduced to " , len(myfriends))
