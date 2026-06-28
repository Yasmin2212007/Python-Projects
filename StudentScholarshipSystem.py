
# Student Scholarship System
# This program determines the student's scholarship and grade based on GPA and age.

Name=input("Enter Your Name: ")
Age=int(input("Enter Your Age: "))
GPA=float(input("Enter Your GPA: "))


if GPA < 0 or GPA > 4:
    print("Invalid GPA")


elif GPA >= 3.7 :
    if Age <= 22 :
        print("Eligible For AI Internship")
    else:
        print("Scholarship Only")
    print(f"Congratulations {Name}")
    print(" You Got Full Scholarship")
    print("Your Grade Is A ")



elif GPA >= 3.3 :
    print(f"Congratulations {Name},Your Grade Is B+")


elif GPA >= 3.0  :
    print(f"Congratulations {Name}")
    print("You Got Half Scholarship")
    print("Your Grade Is B")

elif GPA >= 2.5 :
    print(f"Sorry {Name}")
    print("No Scholarship")
    print("Your Grade Is C")


else  :
    print(f"Sorry {Name}")
    print("No Scholarship")
    print("Your Grade Is F")

