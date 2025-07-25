num=int(input('Enter a number: '))


file = open('output.txt','w')
writing_file = file.write('Hello, Python!\n')
file.close()

file1 = open('output.txt','r')
reading_file = file1.read()
file1.close()


file = open('output.txt','a')
appending_file = file.write('Learning file handling in Python.\n')
file.close()

with open('output.txt','r') as file:
     for line in file:
         print(line.strip())

