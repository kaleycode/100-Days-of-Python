with open('spoiler.txt', 'r') as file:
    for line in file:
        if 'spoiler' in line:
            print(line)