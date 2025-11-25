# WAP t count no of lines in a text file but not count blank lines give me count
c=0
for line in open("text_file.txt"):
    if line.strip():
        c += 1
print("No of lines in file:", c)

# WAP to nomber of words in a text file

c = 0
for line in open("text_file.txt"):
    words = line.split()
    c += len(words)
print("No of words in file:", c)

'''
WAP get odd  line no of a text file  without with statement ,without enumerate'''
f = open("text_file.txt", "r")
i = 1
for line in f:
    if i % 2 != 0:
        print(line.strip())
    i += 1
f.close()

# WAP to get data for user name,branch,roll no and store in file store datain list for each data
while True:
    print("enter exit for exit in name input")
    name = input("Enter your name: ")
    if (name == 'exit' or branch == 'exit' or roll_no == 'exit'):
        print("Exiting...")
        break
    branch = input("Enter your branch: ")
    roll_no = input("Enter your roll no: ") 
    data = [f"Name: {name}\n", f"Branch: {branch}\n", f"Roll No: {roll_no}\n"]

    f=open("student_info.txt", "w")
    f.writelines(data)

    
    f.close()