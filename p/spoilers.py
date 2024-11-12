# find all lines in a file that contain the word 'spoiler'
with open('spoiler.txt', 'r') as file:
    for line in file:
        if 'spoiler' in line:
            print(line)
