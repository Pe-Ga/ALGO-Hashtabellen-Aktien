import csv
from hash_table import Hashtable



def save_hash_table(hast_table_to_save):                    #saves Hashtable object as csv file

    data = hast_table_to_save.get_table()

    file = open('Hash_Directory\\hashtable.csv', 'w', newline='')

    with file:
        write = csv.writer(file)
        for item in data:
            if len(item) == 0:
                write.writerow(["Empty"])
            else:
                write.writerows(data)





def load_hash_table():

    num_lines = sum(1 for line in open('Hash_Directory\\hashtable.csv'))            #counts table_len from saved csv file
    #print(num_lines)
    #Objekt instanzieren
    loaded_data = Hashtable(num_lines)

    with open('Hash_Directory\\hashtable.csv', mode = 'r' ) as file:
        csvFile = csv.DictReader(file)



    return loaded_data