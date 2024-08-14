#I declare that my work contains no examples of misconduct,such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Name : Kavindi Ekanayake
#Student ID : 20221327
#UOW Number : w1956105
#Date : 2023/07/11

#Part 4

number = [0,20,40,60,80,100,120]
creditAtPass = 0
creditAtDefer = 0
creditAtFail = 0
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludeCount = 0
totalCredit = 0
studentCount = 0
rerunCount = 0
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []
student_id = " "
dict = {}

print("\nPart 4: ")
print()

def generateOutcome():
    global student_id, pass_credit, fail_credit, defer_credit, dict
    totalCredit = creditAtPass + creditAtDefer + creditAtFail
    if totalCredit > 120:
        print("Total incorrect.")
        print()
    else:
        if creditAtPass == 120:
            print("Progress")
            dict[student_id] = "Progress -", [creditAtPass,creditAtDefer,creditAtFail]
        elif creditAtPass == 100:
            print("Progress(module trailer)")
            dict[student_id] = "Progress(module trailer) -", [creditAtPass,creditAtDefer,creditAtFail] 
        elif creditAtPass == 80:
            print("Module retriever")
            dict[student_id] = "Module retriever -", [creditAtPass,creditAtDefer,creditAtFail]
        elif creditAtPass == 60:
            print("Module retriever")
            dict[student_id] = "Module retriever -", [creditAtPass,creditAtDefer,creditAtFail] 
        elif creditAtPass == 40:
            if creditAtFail == 80:
                print("Exclude")
                dict[student_id] = "Exclude -", [creditAtPass,creditAtDefer,creditAtFail] 
            else:
                print("Module retriever")
                dict[student_id] = "Module retriever -", [creditAtPass,creditAtDefer,creditAtFail] 
        elif creditAtPass == 20:
            if creditAtDefer >= 40:
                print("Module retriever")
                dict[student_id] = "Module retriever -", [creditAtPass,creditAtDefer,creditAtFail] 
            else:
                print("Exclude")
                dict[student_id] = "Exclude -",[creditAtPass,creditAtDefer,creditAtFail] 
        elif creditAtPass == 0:
            if creditAtDefer >= 60:
                print("Module retriever")
                dict[student_id] = "Module retriever -", [creditAtPass,creditAtDefer,creditAtFail] 
            else:
                print("Exclude")
                dict[student_id] = "Exclude -", [creditAtPass,creditAtDefer,creditAtFail]
   
while True:
        try:
            student_id = input("Enter your student ID: ")
            while True:
                creditAtPass = int(input("Please enter your credits at pass: "))
                if creditAtPass not in range(0, 140, 20):
                    print("Out of range.")
                else:
                    break
            while True:
                creditAtDefer = int(input("Please enter your credits at defer: "))
                if creditAtDefer  not in range(0, 140, 20):
                    print("Out of range.")
                else:
                    break
            while True:
                creditAtFail = int(input("Please enter your credits at fail: "))
                if creditAtFail  not in range(0, 140, 20):
                    print("Out of range")
                else:
                    break
        except ValueError:
            print("Integer required")
            print()
            continue

        generateOutcome(); 
        
        rerunCount = rerunCount + 1
        print("\nWould you like to enter another set of data?")
        rerun = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        if rerun == 'y':
            continue
        if rerun == 'q':
            print(dict)
            break
        

