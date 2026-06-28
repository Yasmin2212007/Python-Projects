

Name=input("Enter Your Name: " )
Age=input("Enter Your Age:  " )
University=input("Enter Your University: " )
Faculty=input("Enter Your Faculty: " )
GPA=input("Enter Your GPA: " )

myList = ["Python","Problem Solving","English"]
myTuple = ("AI","Machine Learning","Data Science")



print("=" * 30)
print("Student Information")
print("=" * 30)


print(f"Name       :{Name}")
print(f"Age        :{Age} ")
print(f"Faculty    :{Faculty}")
print(f"GPA        :{GPA}")
print(f"University :{University}")


print("\nSkills")
print(myList[0])
print(myList[1])
print(myList[2])


print("\nInterested In")
print(myTuple[0])
print(myTuple[1])
print(myTuple[2])


print(f"Your First Character is {Name[0]}")
print(f"Your Last Character is {Name[-1]}")
print(f"First Skill {myList[0]}")
print(f"Last  Skill {myList[-1]}")
print(f"Your First Character is {Age[0]}")
print(f"Your First Character is {University[0]}")
print(f"Your First Character is {Faculty[0]}")
print(f"Your First Character is {GPA[0]}")

print(f"The Type of Name {type(Name)}")
print(f"The Type of Age {type(Age)}")
print(f"The Type of University {type(University)}")
print(f"The Type of Faculty {type(Faculty)}")
print(f"The Type of GPA {type(GPA)}")
print(f"The Type of My Interest is {type(myTuple)}")
print(f"The Type of My Skills is {type(myList)}")

print(f"The Length of Name {len(Name)}")
print(f"The Length of Age {len(Age)}")
print(f"The Length of University {len(University)}")
print(f"The Length of Faculty {len(Faculty)}")
print(f"The Length of GPA {len(GPA)}")
print(f"The Length of My Interest is {len(myTuple)}")
print(f"The Length of My Skills is {len(myList)}")

mySentence="I Love Python"
print(mySentence[0:6])
print(mySentence.title())
print(mySentence.upper())
print(mySentence.lower())
print(mySentence.strip())
print(mySentence.replace("Python","Java"))

newAge=int(Age)+5
print("Your Age After 5 Years is: ")
print(newAge)
