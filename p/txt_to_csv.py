import csv
file_path = 'example.txt'
with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        with open('excelfile.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(words)
