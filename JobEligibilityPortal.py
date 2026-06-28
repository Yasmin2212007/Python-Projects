print("*" *50)
print("Welcome To My Job Eligibility Portal System")
print("You must answer three questions, let's begin")
print("*" *50)


Name=input("Enter your first Name: ").strip().capitalize()

print("You can write the first letter of the word or the whole word")

first_question=input(f"Are you good at Python {Name} Y / N ").strip().capitalize()

experience=int(input(f"Enter the number of years of your experience {Name} "))

Last_Question=input(f"Do you have a university degree in computers and information or have completed an bootcamp {Name} Y / N ").strip().capitalize()



if first_question=="N" or first_question=="No" :
    print(f"Sorry,{Name} Your current qualifications do not allow you to move to the next stage")
    
elif experience <2 :
    print(f"Sorry,{Name} Your current qualifications do not allow you to move to the next stage")
    
elif Last_Question=="N" or Last_Question=="No" :
    print(f"Sorry,{Name} Your current qualifications do not allow you to move to the next stage")

else:
    print(f" Congratulations,{Name} you have qualified with us for the offline interview. We will send you the details via email ")