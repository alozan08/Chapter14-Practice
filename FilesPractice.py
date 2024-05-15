import os

# Complete the function to return the current working directory
# def getCurrentDirectory():
#     return os.getcwd()
#
#
# # expected output: /tmp
# # if using PyFiddle.io otherwise it varies
# print(getCurrentDirectory())


########################################################################################################################
# Complete the function to return the directory name only from the given file name
# def getDirectoryName(fileName):
#     return os.path.dirname(fileName)
#
#
# # expected output: /var/www
# print(getDirectoryName("/var/www/test.html"))
#
# # expected output: /var/www/apple
# print(getDirectoryName("/var/www/apple/test.html"))


########################################################################################################################
# Complete the function to return the file name part only from the given file name
# def getFileName(fileName):
#     return os.path.basename(fileName)
#
#
# # expected output: test.html
# print(getFileName("/var/www/test.html"))
#
# # expected output: names.txt
# print(getFileName("/var/www/apple/names.txt"))


########################################################################################################################
# Complete the function to create the specified file and return the file name
# def createFile(filename):
#     with open(filename, 'w') as f:
#         pass
#     return filename
# # # Student code goes here
# #
# # # expected output: True
# createFile("test.txt")
# print(os.path.exists("test.txt"))


########################################################################################################################
# Complete the function to print all files in the given directory
# def printFiles(someDirectory):
#     print(os.listdir(someDirectory))
#
# # expected output: main.py
# # if using PyFiddle.io otherwise it varies
# printFiles(os.getcwd())


########################################################################################################################
# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
# def whatIsIt(somePath):
#     if os.path.isdir(somePath):
#         return 'DIRECTORY'
#     elif os.path.isfile(somePath):
#         return 'FILE'
#     else:
#         return 'NEITHER'
#
#
# # Student code goes here
#
# # expected output: DIRECTORY
# print(whatIsIt(os.getcwd()))
#
# # expected output: FILE
# print(whatIsIt(os.listdir(os.getcwd())[0]))
#
# # expected output: NEITHER
# print(whatIsIt('apple.pie.123.txt'))


########################################################################################################################
# Complete the function to read the contents of the specified file and print the contents
# def printFileContents(filename):
#     with open(filename) as file:
#         contents = file.read()
#         print(contents)
#
# # Student code goes here
#
# # expected output: Hello
# with open("test.txt", 'w') as f:
#     f.write("Hello")
# printFileContents("test.txt")


########################################################################################################################
# Complete the function to append the given new data to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
    with open(filename, 'a') as file:
        file.write(newData)

    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)


# Student code goes here

# expected output: Hello World
with open("test.txt", 'w') as f:
    f.write("Hello ")
appendAndPrint("test.txt", "World")
