# myfriends = [ 'berla', 'lois', 'benita', 'andrea', 'venny', 'abena' ]
#for afriend in myfriends :
 #if afriend == 'venny':
  #print( "hello " + afriend + " my bestie")
 #else:
  #print("sorry i don't know you ")
#print ("all done !")


# another if statement with an input 
print(" hello and welcome to  cinx \n" + "please enter your name and age ")
user_name = input("Name:")
user_age = input(": ")
#user_age = int(user_age)



if (user_age == 18 ):
     print ("Access granted " + user_name + " fresh blood")
else:
    if  (user_age < 18):
     print ("Access Denied !" + " please wait until you are 18")
    else :
     print("Access granted, you are too old to be denied")

