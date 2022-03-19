# Note: Python passes references NOT copies. Extra Code needed if origin should be preserved.
# some prime numbers > 1000: (1499, 1747, 1999, 2503)

class Hashtable:
    def __init__(self, table_len):
        self.__table_len = table_len
        self.__table = [{}] * table_len

    def hash_function_new(self, to_hash, base):
        ascii_lst = reversed([ord(letter) for letter in to_hash])
        factor = 1
        hashed_string = 0
        for num in ascii_lst:
            factor *= base  # whatever factor is needed
            hashed_string += (num * factor)
        return hashed_string % self.__table_len

    def new_entry(self, to_hash):
        index = self.hash_function_new(to_hash, 31)
        n = 1
        while ((self.__table_len + 1) / 2) != n:  # go through half the table
            if not self.__table[index]:
                self.__table[index] = {"isDeleted": False, "saved_string": to_hash}
                break
            elif self.__table[index]["isDeleted"]:
                self.__table[index] = {"isDeleted": False, "saved_string": to_hash}
                break
            elif self.__table[index]["saved_string"] == to_hash:
                print("Item already exists")
            else:
                index += n * n
                index = index % self.__table_len
                n += 1
                if (self.__table_len + 1) / 2 == n:
                    print("Not enough space in hashtable!")

    def search_entry(self, to_hash):
        index = self.hash_function_new(to_hash, 31)
        n = 1
        while ((self.__table_len + 1) / 2) != n:  # go through half the table
            if not self.__table[index]:
                print("Item does not exist!")
                return False
            elif self.__table[index]["isDeleted"]:
                index += n * n
                index = index % self.__table_len
                n += 1
                if (self.__table_len + 1) / 2 == n:
                    print("Item not found. Reached end of quadratic probing.")
            elif self.__table[index]["saved_string"] == to_hash:
                print("Item found!")
                return index
            else:
                print("Unexpected Error")
                return False

    def del_entry(self, to_search):
        found_index = self.search_entry(to_search)
        if found_index is False:
            print("Error while searching Index!")
        else:
            self.__table[found_index]["isDeleted"] = True
            self.__table[found_index]["saved_string"] = "deleted"

    def show_table(self):
        print(self.__table)

    def add_info(self, index,  key, value):
        self.__table[index].update({key: value})

    def get_entry(self, index):
        print(self.__table[index])

'''
first_table = Hashtable(23)
option = str(input("what to do? insert, search? "))
while option != "_":
    if option == "i":
        insert = str(input("Insert: "))
        first_table.new_entry(insert)
    elif option == "s":
        search = str(input("Search: "))
        first_table.search_entry(search)
    first_table.show_table()
    option = str(input("what to do? insert, search?"))
'''








