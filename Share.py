import csv
class Share:
    def __init__(self, name, wkn, abbr):
        self.__name = name
        self.__wkn = wkn
        self.__abbr = abbr

    def getInfo(self):
        print("NAME: " + self.__name, "WKN: " + self.__wkn, "ABBREVIATION: " + self.__abbr, sep="\n")
    def getName(self):
        return self.__name


def userCreateShare():
    share_name = str(input("Enter NAME of the share: "))
    share_wkn = str(input("Enter WKN of the share: "))
    share_abbr = str(input("Enter ABBREVIATION of the share: "))
    assert len(share_abbr) < 10, "Abbreviation too long! (less then 10!)"

    return Share(share_name, share_wkn, share_abbr)


def hash_function(share):
    toHash = share.getName()
    temp_lst = [ord(letter) for letter in toHash]
    factor = 1
    hash_key = 0
    for num in reversed(temp_lst):
        factor *= 31            # whatever factor is needed
        hash_key += (num * factor)

    return hash_key % 23



################################################################
#TESTING
#newShare = userCreateShare()
#print(hash_function(newShare))
#newShare.getInfo()
################################################################




def get_last_thirty_days(filepath):         # reads last 30 days from csv file and puts it into a list
    with open(filepath, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')

        next(csv_reader)
        lst = []
        for item in range(30):              #limit for 30 items
            row = next(csv_reader)
            #print(row)
            lst.append(row)

    return lst                             #returns a list of list

def print_last_thirty_days():               #prints last 30 days in a table form

    lst = get_last_thirty_days('Source\MSFT.csv')

    #header of tabulatur
    print(" /------------+------------+------------+------------+------------+------------+----------+")
    print(" |    Data    |     open   |   high     |    low     |    close   | adj close  |  volume  |")
    print(" +------------+------------+------------+------------+------------+------------+----------+")

    for sublist in lst:                     #iterating through list of list
        row = ""
        for item in sublist:
            row = row + " | " + item        #string concatination for each row
        print(row + " |")
        print(" +------------+------------+------------+------------+------------+------------+----------+")








