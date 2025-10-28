list1 = [2, 3, 4, "Anna", "BIL", "Taylor"]
list1.append("Sasha")
if "Sasha" in list1:
    print ("He is in")
else:
    print ("No he is not")

if "Sasha" not in list1:
    print ("he is not in the list")













exit()
age = input("Enter your age ")
if age == str(age):
    print ('You did not have written your age with numbers, try on more time')

age_2 = input("Enter your age ")

if int(age_2) < 18 :
    print (f"You are in group 'kids'")
elif int(age_2) >= 18 and int(age_2) <= 35 :
    print ("You are in group 'young people' ")
elif int(age_2) > 35 and int(age_2) <= 60:
    print ("You are in group 'old hand' ") 
else:
    print (f"You are in group 'pensioner' ")    
