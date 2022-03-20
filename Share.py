
# share consists of name, wkn, abbreviation and a list of the imported data
class Share:
    def __init__(self):
        self.__name = ""
        self.__wkn = ""
        self.__abbr = ""
        self.csv_lst = []

    def set_all(self,name,wkn,abbr):
        self.__name = name
        self.__wkn = wkn
        self.__abbr = abbr

    def getInfo(self):
        print("NAME: " + self.__name, "WKN: " + self.__wkn, "ABBREVIATION: " + self.__abbr, sep="\n")

    def getName(self):
        return self.__name

    def getAbbr(self):
        return self.__abbr

    def get_csv_lst(self, ):
        return self.csv_lst

    def set_csv_lst(self, lst):
        self.csv_lst = lst

    # method for user to create a share
    def userCreateShare(self):
        self.__name = str(input("Enter NAME of the share: "))
        self.__wkn = str(input("Enter WKN of the share: "))
        self.__abbr = str(input("Enter ABBREVIATION of the share: "))

    def getWkn(self):
        return self.__wkn

# checks if searched for a name or abbreviation
def is_name(check_string):
    if check_string[0] == "#":
        return True
    else:
        return False
