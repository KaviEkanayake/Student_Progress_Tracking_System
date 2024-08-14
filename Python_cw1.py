#I declare that my work contains no examples of misconduct,such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Name : Kavindi Ekanayake
#Student ID : 20221327
#UOW Number : w1956105
#Date : 2023/06/28

#Part 1

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
rerun = 'y'
while rerun == 'y' :
    while True:
        try:
            creditAtPass = int(input("Please enter your credits at pass: "))
        except ValueError:
            print("Integer required")
            print()
            continue
        else:
            if creditAtPass in range(0,140,20):
                break
            elif creditAtPass not in range(0,140,20):
                print("Out of range.")
                print()
                
                
    while True:
        try:
            creditAtDefer = int(input("Please enter your credits at defer: "))
        except ValueError:
            print("Integer required")
            print()
            continue
        else:
            if creditAtDefer in range(0,140,20):
                break
            elif creditAtDefer not in range(0,140,20):
                print("Out of range.")
                print()
                
                             
    while True:
        try:
            creditAtFail = int(input("Please enter your credits at fail: "))
        except ValueError:
            print("Integer required")
            print()
            continue
        else:
            if creditAtFail in range(0,140,20):
                break
            elif creditAtFail not in range(0,140,20):
                print("Out of range.")
                print()

    totalCredit = creditAtPass + creditAtDefer + creditAtFail
    if totalCredit > 120:
        print("Total incorrect.")
        print()
    else:
        if creditAtPass == 120:
            print("Progress")
            progressCount += 1
            progress_list.append([creditAtPass,creditAtDefer,creditAtFail])
        elif creditAtPass == 100:
            print("Progress(module trailer)")
            trailerCount += 1
            trailer_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
        elif creditAtPass == 80:
            print("Module retriever")
            retrieverCount += 1
            retriever_list.append([creditAtPass,creditAtDefer,creditAtFail])
        elif creditAtPass == 60:
            print("Module retriever")
            retrieverCount += 1
            retriever_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
        elif creditAtPass == 40:
            if creditAtFail == 80:
                print("Exclude")
                excludeCount += 1
                exclude_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
            else:
                print("Module retriever")
                retrieverCount += 1
                retriever_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
        elif creditAtPass == 20:
            if creditAtDefer >= 40:
                print("Module retriever")
                retrieverCount += 1
                retriever_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
            else:
                print("Exclude")
                excludeCount += 1
                exclude_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
        elif creditAtPass == 0:
            if creditAtDefer >= 60:
                print("Module retriever")
                retrieverCount += 1
                retriever_list.append([creditAtPass,creditAtDefer,creditAtFail]) 
            else:
                print("Exclude")
                excludeCount += 1
                exclude_list.append([creditAtPass,creditAtDefer,creditAtFail])

    rerunCount += 1
    print("\nWould you like to enter another set of data?")
    rerun = input("Enter 'y' for yes or 'q' to quit and viwe results: ")
    print("\n")
    continue

print("---------------------------------------------------------------")
print("Histogram")
print("Progress",progressCount," :",progressCount * "*")
print("Trailer",trailerCount,"  :",trailerCount * "*")
print("Retriever",retrieverCount,":",retrieverCount * "*")
print("Excluded",excludeCount," :",excludeCount * "*")
print()

studentCount = progressCount + trailerCount + retrieverCount + excludeCount
print(studentCount,"outcomes in total.")
print("---------------------------------------------------------------")


#Part 2

print("\nPart 2:")
print()

for i in range(0,len(progress_list)):
    print("Progress - ",end=" ")
    print(progress_list[i][0],end=", ")
    print(progress_list[i][1],end=", ")
    print(progress_list[i][2])

for i in range(0,len(trailer_list)):
    print("Progress (module trailer) - ",end=" ")
    print(trailer_list[i][0],end=", ")
    print(trailer_list[i][1],end=", ") 
    print(trailer_list[i][2])

for i in range(0,len(retriever_list)):
    print("Module retriever - ",end=" ")
    print(retriever_list[i][0],end=", ")
    print(retriever_list[i][1],end=", ")
    print(retriever_list[i][2])

for i in range(0,len(exclude_list)):
    print("Exclude - ",end=" ")
    print(exclude_list[i][0],end=", ")
    print(exclude_list[i][1],end=", ") 
    print(exclude_list[i][2])
            

#Part 3

print("\nPart 3:")
print()

f = open('data.txt','w')
for i in range(0,len(progress_list)):
    f.write(f"Progress - {progress_list[i][0]},{progress_list[i][1]},{progress_list[i][2]}\n")

for i in range(0,len(trailer_list)):
    f.write(f"Progress (module triever) - {trailer_list[i][0]},{trailer_list[i][1]},{trailer_list[i][2]}\n")

for i in range(0,len(retriever_list)):
    f.write(f"Module retriever - {retriever_list[i][0]},{retriever_list[i][1]},{retriever_list[i][2]}\n")

for i in range(0,len(exclude_list)):
    f.write(f"Exclude - {exclude_list[i][0]},{exclude_list[i][1]},{exclude_list[i][2]}\n")

f.close()
f = open('data.txt','r')

for i in f:
    print(i,end="")
        



