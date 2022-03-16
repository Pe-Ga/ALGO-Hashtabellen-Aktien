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
newShare = userCreateShare()
print(hash_function(newShare))
newShare.getInfo()
################################################################

