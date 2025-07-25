'''
with open('sample.txt','r') as file:

    for line in file:
        print(line.strip())
'''


 try:
    with open('sample.txt', 'r') as file:
      content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file 'sample.txt' wasnot found.")