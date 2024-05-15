'''
    A photographer is organizing a photo collection about the national parks in the US and
    would like to annotate the information about each of the photos into a separate set of files.
    Write a program that reads the name of a text file containing a list of photo file names.
    The program then reads the photo file names from the text file, replaces the "_photo.jpg"
    portion of the file names with "_info.txt", and outputs the modified file names.

    Assume the unchanged portion of the photo file names contains only letters and numbers,
    and the text file stores one photo file name per line.
    If the text file is empty, the program produces no output.
'''
import os

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

# user_file = input('Enter file name: ')
user_file = 'ParkPhotos.txt'

if not(is_file_empty(user_file)):
    with open (user_file, 'r') as file:
        contents = file.readlines()
        for line in contents:
            line = line.replace('_photo.jpg', '_info.txt')
            print(line, end = '')