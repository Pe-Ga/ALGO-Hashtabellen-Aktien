import csv_save_load

import numpy as np


def get_last_thirty_days(filepath):
    with open(filepath, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')

        lst = []

        for item in csv_reader:
            lst.insert(0, item)
            #lst = [*[item], *lst]

        lst = lst[0:30]

    return lst


def print_last_thirty_days():
    lst = get_last_thirty_days('Source\\MSFT.csv')
    #print(len(lst))

    print(" /------------+------------+------------+------------+------------+------------+----------+")
    print(" |    Data    |     open   |   high     |    low     |    close   | adj close  |  volume  |")
    print(" +------------+------------+------------+------------+------------+------------+----------+")

    for sublist in lst:
        row = ""
        for item in sublist:
            row = row + " | " + item
        print(row + " |")
        print(" +------------+------------+------------+------------+------------+------------+----------+")
