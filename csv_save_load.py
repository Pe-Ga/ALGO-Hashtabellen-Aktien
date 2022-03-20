import csv
from hash_table import Hashtable


def save_hash_table(hash_table_to_save):  # saves Hashtable object as csv file

    data = hash_table_to_save.get_table()

    file = open('Hash_Directory\\hashtable.csv', 'w', newline='')

    with file:
        write = csv.writer(file)
        for item in data:
            if len(item) == 0:
                write.writerow(["Empty"])
            else:
                write.writerows(data)


def load_hash_table():
    num_lines = sum(1 for line in open('Hash_Directory\\hashtable.csv'))  # counts table_len from saved csv file
                                                                          # print(num_lines)
    load_table = Hashtable(num_lines)  # object initialized
    # TODO daten in die tabelle von data per set_table laden und retournieren
    # TODO objekt von Hashtable erstellen
    with open('Hash_Directory\\hashtable.csv', mode='r') as file:       # read from csv
        data = csv.reader(file)
        for row in data:
            load_table.set_table(row)
    return load_table.get_table()                                        #returns list


#print(load_hash_table())
print(type(load_hash_table()))

