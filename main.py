from csv_reader import print_last_thirty_days, get_last_thirty_days
from hash_table import Hashtable as ht
from Share import Share, is_name
from harry_plotter import plot_share

# table is list with dictionaries as entries
# the keys are: 'isDeleted', 'saved_string' and 'share'
name_table = ht(23)
abbr_table = ht(23)

# structured as follows
#   MAIN MENU
#       |-> SEARCH MENU
#               |-> SHARE MENU
print("|MAIN MENU --------------------------------------------------------------------------|")
option = str(input("ADD (+), SAVE(s), LOAD(l), QUIT(x), or SEARCH(?) for more options: "))
while option != "x":
    if option == "+":   # ADD new share
        newShare = Share()  # empty share created
        newShare.userCreateShare()  # filled by user
        name_table.new_entry(newShare.getName())    # enter name of share in name table
        abbr_table.new_entry(newShare.getAbbr())    # enter abbreviation in abbreviation table

        index_name = name_table.search_entry(newShare.getName())

        # errors while searching back to loop beginning
        if index_name is False:
            print("something went wrong. Please try again: ")
            continue

        index_abbr = abbr_table.search_entry(newShare.getAbbr())
        if index_abbr is False:
            print("something went wrong. Please try again: ")
            continue

        # share reference added to the corresponding tables
        name_table.add_info(index_name, "share", newShare)
        abbr_table.add_info(index_abbr, "share", newShare)

    elif option == "?":     # SEARCH for existing share
        while True:
            print("\n|SEARCH MENU  -----------------------------------------------------------------------|")
            to_search = str(input("Type '#NAME' or 'ABBREVIATION' of share to show it or CANCEL(x): "))
            # if a hashtag is put in front of the name the program knows it shall search in name_table
            # no matter if name or abbreviation both will get updated
            # idea: no name/abbreviation should be 'x' -> maybe 2 or more symbols for name/abbreviation
            if to_search == "x":
                break
            # check for case: name/case: abbreviation then update both
            if is_name(to_search):
                index_name = name_table.search_entry(to_search[1:])
                if index_name is False:
                    print("something went wrong. Please try again: ")
                    continue

                name = to_search
                abbr = name_table.get_entry(index_name)["share"].getAbbr()
                index_abbr = abbr_table.search_entry(abbr)

            else:
                index_abbr = abbr_table.search_entry(to_search)
                if index_abbr is False:
                    print("something went wrong. Please try again: ")
                    continue

                abbr = to_search
                name = abbr_table.get_entry(index_abbr)["share"].getName()
                index_name = name_table.search_entry(name)

            name_table.get_entry(index_name)["share"].getInfo()
            # check if data has been imported then print the first data line if it's imported
            if not abbr_table.get_entry(index_abbr)["share"].csv_lst:
                print("Latest Share: ")
                print("No additional data imported")
            else:
                print("Latest Share: ")
                print(abbr_table.get_entry(index_abbr)["share"].csv_lst[1])

            print("\n|CHANGE THIS SHARE?  ----------------------------------------------------------------|")
            share_option = str(input("DEL(-), IMPORT(i) or PLOT(p) chosen share or EXIT(x) this menu: "))
            while share_option != "x":
                if share_option == "-":     # DELETE current share
                    name_table.del_entry(name)
                    abbr_table.del_entry(abbr)
                    break
                elif share_option == "i":   # IMPORT csv file to current share
                    user_filepath = str(input("Enter path to csv file: "))
                    lst = get_last_thirty_days(user_filepath)
                    name_table.get_entry(index_name)["share"].csv_lst = lst

                elif share_option == "p":   # PLOT graph for current share
                    plot_lst = abbr_table.get_entry(index_abbr)["share"].csv_lst
                    plot_share(plot_lst)
                else:
                    print("Wrong input!")
                print("\n|CHANGE THIS SHARE?  ----------------------------------------------------------------|")
                share_option = str(input("DEL(-), IMPORT(i) or PLOT(p) chosen share or EXIT(x) to main menu: "))
    elif option == "s":  # save hashtable
        name_table.save_table('Hash_Directory\\hash_table_name.csv')
        abbr_table.save_table('Hash_Directory\\hash_table_abbr.csv')

    elif option == "l":  # load hashtable
        name_table.load_table('Hash_Directory\\hash_table_name.csv')
        abbr_table.load_table('Hash_Directory\\hash_table_abbr.csv')


    else:
        print("Wrong input try again: ")
    print("\n|MAIN MENU  -------------------------------------------------------------------------|")
    option = str(input("ADD (+), SAVE(s), LOAD(l), QUIT(x), or SEARCH(?) for more options: "))
