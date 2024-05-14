'''
    Write a program that first reads in the name of an input file and then reads the input file using the
    file.readlines() method. The input file contains an unsorted list of number of seasons followed by
    the corresponding TV show.
    Your program should put the contents of the input file into a dictionary where the number of seasons
    are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).

    Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt.
    Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the
    input file. Next, sort the dictionary by values (alphabetical order), and output the results to a file
    named output_titles.txt.
'''


with open('file1.txt', 'r') as file:
    contents = file.readlines()
    tv_dict = {}

    i = 0
    while i < len(contents):
        key = contents[i].strip()
        value = contents[i+1].strip()

        if key in tv_dict:
            tv_dict[key] += '; ' + value
        else:
            tv_dict[key] = value

        i += 2


with open('output_keys.txt', 'w') as out:
    for key, value in sorted(tv_dict.items()):
        out.write(f'{key}: {value}\n')

with open('output_titles.txt', 'w') as titles:
    for value in sorted(tv_dict.values()):
        if ';' in value:
            temp_values = value.split(';')
            for current in temp_values:
                titles.write(current.strip() + '\n')
        else:
            titles.write(value.strip() + '\n')

