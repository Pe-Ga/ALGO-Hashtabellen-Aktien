# Note: Python passes references NOT copies. Extra Code needed if origin should be preserved.
# some prime numbers > 1000: (1499, 1747, 1999, 2503)

class Hashtable:
    def __init__(self, table_len):
        self.__table_len = table_len
        self.__table = [{}] * table_len     # create list with empty dicts
        # errors can be handled in a better way for sure...
        self.__error_codes = ["success", "ERht01", "ERht02", "ERht03", "ERht04"]
        self.__error_decoding = {"success": "Actions successful",
                          "ERht01": "Entry already exists!",
                          "ERht02": "Reached end of quadratic probing",
                          "ERht03": "Item does not exist",
                          "ERht04": "Unexpected Error"}

    # if error return false
    def error_reader(self, err_num):
        err_msg_key = self.__error_codes[-err_num]
        print(self.__error_decoding[err_msg_key])
        return False

    # string to big integer modulo table length
    def hash_function_new(self, to_hash, base):
        ascii_lst = reversed([ord(letter) for letter in to_hash])
        factor = 1
        hashed_string = 0
        for num in ascii_lst:
            factor *= base  # whatever factor is needed
            hashed_string += (num * factor)
        return hashed_string % self.__table_len

    # makes new entry to table takes string input
    # entry looks like: {"isDeleted": False, "saved_string": parameter_string}
    def new_entry(self, to_hash):
        initial_index = self.hash_function_new(to_hash, 31)
        index = initial_index
        n = 1
        while ((self.__table_len + 1) / 2) != n:  # go through half the table
            # check if index is completely empty
            if not self.__table[index]:
                self.__table[index] = {"isDeleted": False, "saved_string": to_hash}
                return 0
            # check if index already deleted
            elif self.__table[index]["isDeleted"]:
                self.__table[index] = {"isDeleted": False, "saved_string": to_hash}
                return 0
            # checks if string is the same
            elif self.__table[index]["saved_string"] == to_hash:
                return self.error_reader(-1)  # "ERht01"
            # quadratic probing
            else:
                index = initial_index
                index += n * n
                index = index % self.__table_len
                n += 1
                if (self.__table_len + 1) / 2 == n:
                    return self.error_reader(-2)   # "ERht02"

    def search_entry(self, to_hash):
        initial_index = self.hash_function_new(to_hash, 31)
        index = initial_index
        n = 1
        while ((self.__table_len + 1) / 2) != n:  # go through half the table
            if not self.__table[index]:
                return self.error_reader(-3)   # "ERht03"
            elif self.__table[index]["isDeleted"]:
                index = initial_index
                index += n * n
                index = index % self.__table_len
                n += 1
                if (self.__table_len + 1) / 2 == n:
                    return self.error_reader(-2)   # "ERht02"
            elif self.__table[index]["saved_string"] == to_hash:
                return index
            else:
                return self.error_reader(-4)   # "ERht04"

    def del_entry(self, to_search):
        found_index = self.search_entry(to_search)
        if not found_index:
            return found_index
        else:
            # sets original entry to isDeleted: True
            self.__table[found_index] = {"isDeleted": True}
            return True

    # testing purpose
    def show_table(self):
        print(self.__table)

    # add more info to dictionary, missing a lot of testing and limitation
    def add_info(self, index,  key, value):
        self.__table[index].update({key: value})

    # gets dictionary at index
    def get_entry(self, index):
        return self.__table[index]

    def get_table(self):
        return self.__table

    def set_table(self, table_input):
        self.__table = table_input
