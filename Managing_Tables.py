## A Program to display a table with rows and columns
## with apporiate width

import pickle
from time import sleep
import colorama as cr
cr.init()

loc_dict = "table_dict.pickle"


# no inspection PyMethod First ArgAssignment
class c():
    def init():
        cr.init()
        
    def red(string):
        string = " "+cr.Style.BRIGHT+cr.Fore.RED + string + cr.Fore.RESET+cr.Style.NORMAL+" "
        return string

    def yellow(string):
        string = " "+cr.Style.BRIGHT+cr.Fore.YELLOW + string + cr.Fore.RESET +cr.Style.NORMAL+" "
        return string

    def blue(string):
        string = " "+cr.Style.BRIGHT+cr.Fore.BLUE + string + cr.Fore.RESET+cr.Style.NORMAL+" "
        return string

    def cyan(string):
        string = " "+cr.Style.BRIGHT+cr.Fore.CYAN + string + cr.Fore.RESET+cr.Style.NORMAL+" "
        return string

    def green(string):
        string = " "+cr.Style.BRIGHT+cr.Fore.GREEN + string + cr.Fore.RESET+cr.Style.NORMAL+" "
        return string


def load_dict():
    global table_dict
    try:
        pickle_in = open(loc_dict, "rb")
        table_dict = pickle.load(pickle_in)
    except:
        table_dict = {}


def save_dict():
    global table_dict

    pickle_out = open(loc_dict, "wb")
    pickle.dump(table_dict, pickle_out)
    pickle_out.close()

    sleep(2)

    pickle_in = open(loc_dict, "rb")
    table_dict = pickle.load(pickle_in)


def change_loc():
    global loc_dict

    print(">Current location of tables:", loc_dict)
    print(">Please enter new location of tables")
    print(r">Eg : C:\User\Destop\Tables_file")
    print(">The last level is the file name WITHOUT extension")
    print(">This is case sensitive")
    print()
    pre_text = (">File location: ")

    loc_dict_new = input_color(pre_text)
    if loc_dict.upper() == "DONE":
        return None

    if ".pickle" not in loc_dict:
        loc_dict_new +=".pickle"

    try:
        with open(loc_dict_new, "wb") as F:
            pass
    except FileNotFoundError:
        print(">File unable to be created")
        print(">Invalid path, please try again")
        print(">Enter DONE to exit process")
        change_loc()

    else:

        loc_dict = loc_dict_new


def pnt(text, ignore=""):

    ## just a function to print and end on
    ## the same line
    print(text, end="")


# noinspection PyTypeChecker
class display_table():

    def column_lengths(table):

        ## Table is just the entire table as a tuple where
        ## each row is a sub tuple

        column_chr = []
        ## This list will contain the maximum chars in each column

        for i in range(len(table[0])):
            max_char = 0
            for row in table:
                if len(row[i])>max_char:
                    max_char = len(row[i])

            column_chr.append(max_char + 3) ## the +3 for space

        return tuple(column_chr)

    def top_line(column_chr, sep_ver, sep_hori, corner, func=pnt, file=""):
        ## Just the seperator b/w 2 rows

        for each in column_chr:

            func(corner +(sep_hori*each), file)
        func(corner+"\n", file)

    def top_num(column_chr, func=pnt, file=""):
        func(" ", file)
        for i, each in enumerate(column_chr, start=1):
            func(str(i)+" "*each, file)
        func("\n", file)


    def display(table, sep_ver = "|", sep_hori = "-", corner = "+", func = pnt, file=""):

        column_chr = display_table.column_lengths(table)

        ## sum of the widths of the coloumns
        ## + the lines in b\w columns
        ## + 1 last dash at the end as to create 9 columns you need 10 lines

        display_table.top_num(column_chr, func, file=file)
        row_no = 0
        for row in table:

            if table.index(row) == 0:
                pnt(cr.Style.BRIGHT, file)

            display_table.top_line(column_chr, sep_ver, sep_hori, corner, func = func, file=file)

            if table.index(row) == 1:
                pnt(cr.Style.NORMAL, file)
            
            column = 0
            for element in row:

                func(sep_ver + str(element), file)
                func(" " * (column_chr[column] - len(str(element))), file)
                column += 1

            func(sep_ver, file)
            if row_no:func(str(row_no)+"\n", file)
            else:func("\n", file)
            row_no += 1




        display_table.top_line(column_chr, sep_ver, sep_hori, corner, func = func, file=file)


# noinspection PyTypeChecker
class table_func():

    # Returns a Tuple containing either the sum in a single element tuple
    # or if its not able to calculate it then it just return the (False, row_no)
    def sum(table, column):

        ## The sum function returns a value of (False, and the row) if there is an error
        ## The above return is a tuple
        ## In the converstion of the value to a float
        ## If Everything is executed properly then
        ## The function returns a value sum as a tuple

        sum = 0
        for row in table:

            try :
               x = float(row[column])
            except Exception as e:
                if row[column] in ("","nil","none"):
                    continue

                ## Error in the convertion of the element in the row
                return (False, row.index(table))
                ## Returning a tuple
            sum += x
        return (sum, )


    def avg(table, column):

        sum = table_func.sum(table, column)
        if not sum[0] == False:
            pass


    def count(table, column, search=False):

        count = 0
        for row in table:
            if row[column] in ("","nil","none"):
                continue
            count += 1

        return count

    def col_name(add = False, table = ()):

        ## If add == True then a column has to be
        ## appended to an existing table

        if not add:
            print(">Create Table >Enter the column names.")
            col_name = ''
            cols = ()
            count = 1

            while col_name != "DONE":

                text1 = ">Col_"+str(count)
                pre_text = (text1+">")
                col_name = input_color(pre_text).upper()
                if col_name == "DONE":
                    break
                else:
                    count+=1
                    cols+=(col_name ,)

            table += (cols ,)
            return table


    def add_to_col(table, col_no, user_in):
        ## table -----> current working table
        ## col_no ----> col onto which data to be added
        ## user_in ---> data to be addded

        flag = False
        ## to check if there is a row with a blank in its column

        for row in table:
            if "" == row[col_no]:
                flag = table.index(row)
                break

        if not flag:
            ## An empty column does not exit and has tp be created

            no_of_cols = len(table[0])
            new_row = ["" for i in range(no_of_cols)]
            new_row[col_no] = user_in
            new_row = (tuple(new_row),)
            table+= new_row

        else:

            cur_row = list(table[flag])
            cur_row[col_no] = user_in
            table = list(table)
            table[flag] = tuple(cur_row)
            table = tuple(table)

        return table


    def add_to_row(table, row_no,col_no, user_in):

        row = list(table[row_no])
        row[col_no] = user_in
        row = tuple(row)
        table = list(table)
        table[row_no] = row
        table = tuple(table)
        return table



    def create_row(table, row_no):
        if row_no+1 > len(table):
            ## row +1 to get no. of the row not index
            diff = row_no+1 - len(table)
            for i in range(diff):
                add_row = tuple(["" for j in range(len(table[0]))])
                table += (add_row, )

        return table



    def check_cmd(table, user_cmd, user_in):

        if "COL" in user_cmd:
            col_no = int(user_cmd[user_cmd.index("COL")+3])-1
            ## -1 for the indexing value
            if col_no+1 > len(table[0]):
                print(">...>...>Column no. out of range")
                return table

            if "ROW" in user_cmd:
                ## user wants to enter data on the specific tab
                ## col1#row2 (Suchith)
                row_no = int(user_cmd[user_cmd.index("ROW")+3])+(-1+1)
                ## -1 for the indexing 
                ## +1 as the names wala row is not considered a row

                table = table_func.create_row(table, row_no)

                table = list(table)
                row = list(table[row_no])
                row[col_no] = user_in
                table[row_no]= tuple(row)
                table = tuple(table)
                

            elif "#" in user_cmd:
                ## user wants to keep entering data onto this column
                while True:
                    pre_text = ("...>In table >Col_"+str(col_no+1)+">")
                    user_in = input_color(pre_text).upper()
                    if user_in == "DONE":
                        break
                    table = table_func.add_to_col(table, col_no, user_in)

            else:
                ## user wants to add on data to the column
                table = table_func.add_to_col(table, col_no, user_in)

        elif "ROW" in user_cmd:
            while True:

                row_no = int(user_cmd[user_cmd.index("ROW")+3])-1+1
                ## -1 for the indexing value
                ## +1 as the names wala row is not considered a row
                table = table_func.create_row(table, row_no)

                if "#" in user_cmd:
                    ## User wants to keep adding row wise
                    table = table_func.create_row(table, row_no)

                    for col_ in table[row_no]:
                        if col_ == "":
                            col_ = table[row_no].index(col_)
                            break
                    else:
                        user_cmd = list(user_cmd)
                        temp = user_cmd.index("W")
                        temp+=1 ## Gives you index of  number
                        row_no+=1 ## Next row as row is full
                        user_cmd[temp] = str(row_no)
                        user_cmd = "".join(user_cmd)
                        continue

                        # table_func.check_cmd(table, user_cmd, user_in)


                    pre_text = "...>In table >Row_"+str(row_no)+" #Col_"+str(col_+1)+">"
                    user_in = input_color(pre_text).upper()
                    if user_in == "DONE":
                        if col_ == 0:
                            for i in table[row_no]:
                                if i != "":
                                    break
                            else:
                                table = list(table)
                                del table[-1]
                                table = tuple(table)
                        break

                table = table_func.add_to_row(table, row_no, col_, user_in)
                continue
                # table = table_func.check_cmd(table, user_cmd, user_in)                    
            
            else:
                row = (table[row_no])
                for i in row:
                    if i == "":
                        col_ = row.index(i)

                table = table_func.add_to_row(table, row_no, col_, user_in)



        return table


    def save_table(table):
        pre_text = "Save Table >"

        global table_dict

        print(">Save Table >Enter a name for the table")
        name = input_color(pre_text).upper()
        table_dict[name] = table

        save_dict()

        print(c.blue("\rSave Table >Table Successfully saved"))


    def export():
        table_name = ""

        while table_name not in table_dict:
            pnt(">Export Table >Table Name >")
            table_name = input().upper()

        opt = ""
        opt_list = ["WORD", "EXCEL", "NOTEPAD"]

        while opt not in opt_list:
            pnt(">Export Table >Type >")
            opt = input().upper()

        if opt == "NOTEPAD":
            pnt(">Export Table >Name of file(case sensitve) >")
            name_of_file = input()
            if ".txt" not in name_of_file:
                name_of_file+=".txt"

        with open(name_of_file, "w") as file:

            display_table.display(table_dict[table_name], func = table_func.writing,
                file = file)

    def writing(string, file):

        file.write(string)


    def create():

        table = table_func.col_name()

        print(">Create Table >Table Created with the column names")
        print()
        print(">Create Table >Refer to guide")
        print()
        while True:

            pre_text = ">Create Table >In table >"
            user_cmd = input_color(pre_text).upper()


            if user_cmd == "DONE":
                print(">Create Table >Table Created with entered data")
                print(">Create Table >Do you want to save table (Y/N)")
                while True:
                    pre_text = (">Create Table >")
                    x = input_color(pre_text).upper()
                    if x == "Y":
                        table_func.save_table(table)
                        break

                    elif x == "N":
                        break

                    else:
                        print(">Create Table >Please enter valid option")
                        print()

                break


            elif user_cmd == "save table".upper():
                table_func.save_table(table)

            elif user_cmd == "display table".upper():
                display_table.display(table)
                print()
                continue

            elif "(" in user_cmd:

                if user_cmd[-1] != ")":
                    user_cmd+= ")"

                loc = user_cmd.index("(")
                loc2 = -(user_cmd[::-1].index(")")+1)

                user_in = user_cmd[loc+1:loc2]
                user_cmd = user_cmd[:loc]

            elif "#" in user_cmd and (("ROW" not in user_cmd) or ("COL" not in user_cmd)):
                user_in = ""

            else:
                print(">Create Table >Invalid syntax, () must exist")
                continue

            table = table_func.check_cmd(table, user_cmd, user_in)


            
        return table


    def edit(table_name):
        table  = table_dict[table_name]
        display_table.display(table)
        print()
        pre_text = ">Edit Table >In table >"
        while True:
            user_cmd = input_color(pre_text).upper()

            if user_cmd == "DONE":
                print(">Edit Table >Table Created with entered data")
                print(">Edit Table >Do you want to save table (Y/N)")
                while True:
                    pre_text = (">Edit Table >")
                    x = input_color(pre_text).upper()
                    if x == "Y":
                        table_func.save_table(table)
                        break

                    elif x == "N":
                        break

                    else:
                        print(">Edit Table >Please enter valid option")
                        print()

                break


            elif user_cmd == "save table".upper():
                table_func.save_table(table)

            elif user_cmd == "display table".upper():
                display_table.display(table)
                print()
                continue

            elif "(" in user_cmd:

                if user_cmd[-1] != ")":
                    user_cmd+= ")"

                loc = user_cmd.index("(")
                loc2 = -(user_cmd[::-1].index(")")+1)

                user_in = user_cmd[loc+1:loc2]
                user_cmd = user_cmd[:loc]

            elif "#" in user_cmd and (("ROW" not in user_cmd) or ("COL" not in user_cmd)):
                user_in = ""

            else:
                print(">Edit Table >Invalid syntax, () or # must exist")
                continue

            table = table_func.check_cmd(table, user_cmd, user_in)



def intro(ins):
    string = ('''\r>Running Hexnal program of tables
        \r>Please enter'''+c.cyan('GUIDE')+ '''for the instructions for the program
        ''')

    string2 = ("""
        \r>This program can be used for storing and analyzing data in
        \rtable format.
        \r>The commands ARE NOT case sensitve

        \r>Program works on command provided to the system
        \r>The following is the list of commands:\n\n""" +

        '   1.'+ c.cyan('EXIT')+'                [exits the program]\n'
        '   2.'+c.cyan('CREATE TABLE')+'        [creates a new table]\n'
        '   3.'+c.cyan('SHOW TABLES')+'         [shows all the tables saved in program]\n'
        '   4.'+c.cyan('{Table Name}')+'        [displays a specific table from saved tables]\n'
        '   5.'+c.cyan('EDIT TABLE')+'          [edits a currently existing table]\n'
        '   6.'+c.cyan('DELETE TABLE')+'        [delete table from saved tables]\n'
        '   7.'+c.cyan('{Command} GUIDE')+'     [instructions on any of the above 6 commands]\n'
        '       [Replace {Command} with any of the above commands]\n'
        '       [eg: CREATE TABLE GUIDE]')

    if ins == 2:
        print(string2)
    elif ins == 1:
        print(string)


def input_color(pre_text):

        pnt(cr.Fore.GREEN+cr.Style.BRIGHT)
        pnt(pre_text)
        x = input()
        pnt(cr.Fore.RESET+cr.Style.NORMAL)
        return x


def main():
    load_dict()
    intro(1)
    pre_text = ">"

    while True:

        user_cmd = input_color(pre_text).upper()
        
        if user_cmd == "exit".upper():
            exit()

        elif user_cmd == "GUIDE":
            intro(2)

        elif user_cmd == "Create Table".upper():
            table_func.create()

        elif user_cmd == "export table".upper():
            table_func.export()

        elif user_cmd == "show tables".upper():
            for i, key in enumerate(table_dict, start = 1):
                pnt(">Show Tables >")
                print(str(i)+"."+ c.blue(key))
            print()

        elif user_cmd in table_dict:
            display_table.display(table_dict[user_cmd])
            print()

        elif user_cmd == "edit table".upper():
            print(">Edit Table >Enter Table name")
            pre_text = (">Edit Table >")
            table_name = input_color(pre_text).upper()

            if table_name in table_dict:

                table_func.edit(table_name)

            else:
                print(c.red("\r>Edit Table >Table not found"))
                print()
            pre_text = (">")


        elif user_cmd == "delete table".upper():
            print(">Delete Table >Enter Table Name")
            pnt(">Delete Table >")
            table_name = input_color(pre_text).upper()

            if table_name in table_dict:

                print(">Delete Table >The Table Contains the following Columns")
                print(table_dict[table_name][0])
                print()
                print(">Delete Table >Confirm Deletion (Y/N)")

                while True:
                    pnt(">Delete Table >")
                    x = input_color(pre_text).upper()

                    if x == "Y":
                        del table_dict[table_name]
                        break

                    elif x == "N":
                        break

                    else:
                        print(">Delete Table >Invalid input")
                        print()
                        continue
        else:
            print(c.red("\r>Invalid Command, Please refer to GUIDE"))

           


if __name__ == '__main__':
    main()

