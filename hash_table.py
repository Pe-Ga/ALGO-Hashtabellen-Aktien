# Note: Python passes references NOT copies. Extra Code needed if origin should be preserved.
# some prime numbers > 1000: (1499, 1747, 1999, 2503)


# params(string, int, int prime_number)
# returns index


table_len = 23
generic_table = [None] * table_len


def hash_function_new(to_hash, base):
    ascii_lst = reversed([ord(letter) for letter in to_hash])
    factor = 1
    hashed_string = 0
    for num in ascii_lst:
        factor *= base         # whatever factor is needed
        hashed_string += (num * factor)

    return hashed_string % table_len


# object is a generalization of the share. Not sure if this is ideal =)
def new_entry(to_hash, outer_list):
    index = hash_function_new(to_hash, 31)
    n = 1
    while ((table_len + 1) / 2) != n:   # go through half the table
        if outer_list[index] is None:
            outer_list[index] = {"isDeleted": False, "object": to_hash}
            break
        elif outer_list[index]["isDeleted"]:
            outer_list[index] = {"isDeleted": False, "object": to_hash}
            break
        elif outer_list[index]["object"] == to_hash:
            print("Item already exists")
        else:
            index += n*n
            index = index % table_len
            n += 1
            if(table_len + 1) / 2 == n:
                print("Not enough space in hashtable!")


def search_entry(to_hash, outer_list):
    index = hash_function_new(to_hash, 31)
    n = 1
    while ((table_len + 1) / 2) != n:   # go through half the table
        if outer_list[index] is None:
            print("Item does not exist!")
            return False
        elif outer_list[index]["isDeleted"]:
            index += n*n
            index = index % table_len
            n += 1
            if (table_len + 1) / 2 == n:
                print("Item not found. Reached end of quadratic probing.")
        elif outer_list[index]["object"] == to_hash:
            print("Item found!")
            return index
        else:
            print("Unexpected Error")
            return False


def del_entry(to_search, outer_list):
    found_index = search_entry(to_search, outer_list)
    if found_index is False:
        print("Error while searching Index!")
    else:
        outer_list[found_index]["isDeleted"] = True
        outer_list[found_index]["object"] = "deleted"
