

class Share:
    def __init__(self):
        self.__name = ""
        self.__wkn = ""
        self.__abbr = ""
        self.__filepath = "Source\\" + self.__abbr + ".csv"

    def getInfo(self):
        print("NAME: " + self.__name, "WKN: " + self.__wkn, "ABBREVIATION: " + self.__abbr, sep="\n")

    def getName(self):
        return self.__name

    def getAbbr(self):
        return self.__abbr

    def userCreateShare(self):
        self.__name = str(input("Enter NAME of the share: "))
        self.__wkn = str(input("Enter WKN of the share: "))
        self.__abbr = str(input("Enter ABBREVIATION of the share: "))


def is_name(check_string):
    if check_string[0] == "#":
        check_string = check_string[1:]
        return True
    else:
        return False

################################################################
#TESTING
#newShare = userCreateShare()
#print(hash_function(newShare))
#newShare.getInfo()
################################################################
'''    def __init__(self, name, wkn, abbr):
        self.__name = name
        self.__wkn = wkn
        self.__abbr = abbr
        self.__filepath = "Source\\" + self.__abbr + ".csv"'''




