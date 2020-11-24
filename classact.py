
Boy_NameOfWeeks = ['Kojo','kwabena','Kwaku','Yaw','Kofi','Kwame','Kwasi']
Girl_nameOfweeks =['Adjoa','Abena','Akua','Yaa','Afia','Ama','Esi']

dayOfBirth = input("please enter your day of birth ")
gender = input("are you a male or a female ")
loglist = []
if (dayOfBirth == 'monday' and gender == 'female'):
        print("your name will be " , Girl_nameOfweeks[0])
elif(dayOfBirth == 'monday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[0])

elif(dayOfBirth == 'tuesday' and gender == 'female'):
        print("your name will be ", Girl_nameOfweeks[1])
elif(dayOfBirth == 'tuesday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[1])

elif(dayOfBirth == 'wednesday' and gender == 'female'):
        print("your name will be ", Girl_nameOfweeks[2])
elif(dayOfBirth == 'wednesday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[2])

elif(dayOfBirth == 'thursday' and gender == 'female'):
        print("your name will be ", Girl_nameOfweeks[3])
elif(dayOfBirth == 'thursday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[3])

elif(dayOfBirth == 'friday' and gender == 'female'):
        print("your name will be ", Girl_nameOfweeks[4])
elif(dayOfBirth == 'friday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[4])

elif(dayOfBirth == 'saturday' and gender == 'female'):
        print("your name will be ", Girl_nameOfweeks[5])
elif(dayOfBirth == 'saturday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[5])

elif(dayOfBirth == 'sunday' and gender == 'female'):
        print("your name will be ", Girl_nameOfweeks[6])
elif(dayOfBirth == 'sunday' and gender == 'male'):
        print("your name will be ", Boy_NameOfWeeks[6])

else:
    print("please check your input and try again")
loglist.append(dayOfBirth)
print("a", loglist , "born just used your app ")  