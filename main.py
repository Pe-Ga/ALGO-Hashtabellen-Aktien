from csv_reader import print_last_thirty_days,get_last_thirty_days
from hash_table import Hashtable as ht
from Share import Share, is_name

name_table = ht(23)
abbr_table = ht(23)

new_list = [{}]*10
print(new_list)
print(not new_list[0])
new_list[0] = {"greeting": "hi"}
print(new_list[0])


option = str(input("ADD (+), DEL(-), IMPORT(i), SEARCH(?), PLOT(p), SAVE(s), LOAD(l), QUIT(x): "))
while option != "x":
    if option == "+":
        newShare = Share()
        newShare.userCreateShare()
        name_table.new_entry(newShare.getName())
        abbr_table.new_entry(newShare.getAbbr())
    elif option == "-":
        to_delete = str(input("Type '#NAME' or 'ABBREVIATION' of share to delete it: "))
        if is_name(to_delete):
            name_table.del_entry(to_delete[1:])
        else:
            abbr_table.del_entry(to_delete)
    elif option == "i":
        print()
    elif option == "?":
        to_search = str(input("Type '#NAME' or 'ABBREVIATION' of share to show it: "))
        if is_name(to_search):
            index = name_table.search_entry(to_search[1:])
            name_table.get_entry(index)
        else:
            index = abbr_table.search_entry(to_search)
            print(abbr_table.get_entry(index))
    elif option == "p":
        print()
    else:
        print("Wrong input try again: ")
    option = str(input("ADD (+), DEL(-), IMPORT(i), SEARCH(?), PLOT(p), SAVE(s), LOAD(l), QUIT(x): "))
