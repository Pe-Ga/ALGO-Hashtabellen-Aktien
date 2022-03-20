from csv_reader import print_last_thirty_days, get_last_thirty_days
from hash_table import Hashtable as ht
from Share import Share, is_name
from harry_plotter import plot_share

name_table = ht(23)
abbr_table = ht(23)


option = str(input("ADD (+), DEL(-), IMPORT(i), SEARCH(?), PLOT(p), SAVE(s), LOAD(l), QUIT(x): "))
while option != "x":
    if option == "+":
        newShare = Share()
        newShare.userCreateShare()
        name_table.new_entry(newShare.getName())
        abbr_table.new_entry(newShare.getAbbr())

        index_name = name_table.search_entry(newShare.getName())
        index_abbr = abbr_table.search_entry(newShare.getAbbr())
        name_table.add_info(index_name, "share", newShare)
        abbr_table.add_info(index_abbr, "share", newShare)

    elif option == "-":
        to_delete = str(input("Type '#NAME' or 'ABBREVIATION' of share to delete it: "))
        if is_name(to_delete):
            name_table.del_entry(to_delete[1:])
        else:
            abbr_table.del_entry(to_delete)

    elif option == "i":
        to_import = str(input("Type 'NAME' of share to import its csv file: "))
        index = name_table.search_entry(to_import)


    elif option == "?":
        to_search = str(input("Type '#NAME' or 'ABBREVIATION' of share to show it: "))
        if is_name(to_search):
            index = name_table.search_entry(to_search[1:])
            name_table.get_entry(index)["share"].getInfo()
        else:
            index = abbr_table.search_entry(to_search)
            abbr_table.get_entry(index)["share"].getInfo()

    elif option == "p":
        #plot_share(get_last_thirty_days(abbr_table.get_entry(index)["share"].getFilepath()))
        print()

    else:
        print("Wrong input try again: ")
    option = str(input("ADD (+), DEL(-), IMPORT(i), SEARCH(?), PLOT(p), SAVE(s), LOAD(l), QUIT(x): "))
