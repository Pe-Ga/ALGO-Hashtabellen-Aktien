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

def print_last_thirty_days():

    lst = get_last_thirty_days('Source\MSFT.csv')

    print(" /------------+------------+------------+------------+------------+------------+----------+")
    print(" |    Data    |     open   |   high     |    low     |    close   | adj close  |  volume  |")
    print(" +------------+------------+------------+------------+------------+------------+----------+")

    for sublist in lst:
        row = ""
        for item in sublist:
            row = row + " | " + item
        print(row + " |")
        print(" +------------+------------+------------+------------+------------+------------+----------+")







