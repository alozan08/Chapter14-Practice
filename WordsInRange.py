'''
    Write a program that first reads in the name of an input file, followed by two strings representing
    the lower and upper bounds of a search range. The file should be read using the file.readlines() method.
    The input file contains a list of alphabetical, ten-letter strings, each on a separate line.
    Your program should output all strings from the list that are within that range (inclusive of the bounds).
'''

user_file = input("Enter file name: ")
lower_bound = input('Enter lower bound: ')
upper_bound = input('Enter upper bound: ')

with open (user_file, 'r') as file:
    contents = file.readlines()

    for line in contents:
        word = line.strip()
        if lower_bound <= word <= upper_bound:
            print(line, end = '')
