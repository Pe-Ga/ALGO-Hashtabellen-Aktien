from csv_reader import print_last_thirty_days, get_last_thirty_days
from hash_table import Hashtable as ht
from Share import Share, is_name
from harry_plotter import plot_share

name_table = ht(23)
abbr_table = ht(23)

option = str(input("ADD (+), SAVE(s), LOAD(l), QUIT(x), or SEARCH(?) for more options: "))
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

    elif option == "?":
        to_search = str(input("Type '#NAME' or 'ABBREVIATION' of share to show it: "))
        if is_name(to_search):
            index_name = name_table.search_entry(to_search[1:])
            name_table.get_entry(index_name)["share"].getInfo()

            name = to_search
            abbr = name_table.get_entry(index_name)["share"].getAbbr()
            index_abbr = abbr_table.search_entry(abbr)

        else:
            index_abbr = abbr_table.search_entry(to_search)
            abbr_table.get_entry(index_abbr)["share"].getInfo()

            abbr = to_search
            name = abbr_table.get_entry(index_abbr)["share"].getName()
            index_name = name_table.search_entry(name)

        share_option = str(input("DEL(-), IMPORT(i) or PLOT(p) chosen share or EXIT(x) to main menu: "))
        while share_option != "x":
            if share_option == "-":
                name_table.del_entry(name)
                abbr_table.del_entry(abbr)

            elif share_option == "i":
                user_filepath = str(input("Enter path to csv file: "))
                lst = get_last_thirty_days(user_filepath)
                name_table.get_entry(index_name)["share"].csv_lst = lst

            elif share_option == "p":
                plot_lst = abbr_table.get_entry(index_abbr)["share"].csv_lst
                plot_share(plot_lst)
            else:
                print("Wrong input!")
            share_option = str(input("DEL(-), IMPORT(i) or PLOT(p) chosen share or EXIT(x) to main menu: "))

    else:
        print("Wrong input try again: ")
    option = str(input("ADD (+), DEL(-), IMPORT(i), SEARCH(?), PLOT(p), SAVE(s), LOAD(l), QUIT(x): "))
