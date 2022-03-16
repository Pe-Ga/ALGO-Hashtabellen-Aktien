import csv


def get_last_thirty_days(filepath):
    with open(filepath, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')

        next(csv_reader)
        lst = []
        for item in range(30):
            row = next(csv_reader)
            #print(row)
            lst.append(row)

    return lst

