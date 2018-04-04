###############################################################################
# PROJECT: "PACA"
# author = "VICTOR"
# coding = utf-8
######################################
#####  IMPORTS & SERVER CONNECT  #####
######################################
try:
    import psycopg2
except:
    #import pip
    pip.main(['install','psycopg2'])
    import psycopg2

source_server = "pgserver.mah.se"
databas = "paca_database"
user = "ah8723"
passw = "m9q6w3ek"
connect = ""

while connect != "OK":
    try:
        conn = psycopg2.connect(dbname=databas, user=user, password=passw,
                                host=source_server)
        cursor = conn.cursor()
        connect = "OK"
    except:
        print("\n! Fel i anslutning till servern\nKolla inlogg"+
              " adress och uppkoppling!")
        user  = input("Användare: ")
        passw = input("Lösenord:  ")

######################################
#####  MAIN  #########################
######################################
def main():
    while True:
        main_menu()
        active_table()

def active_table():
    ''' Basic menu choice handler '''
    while True:
        choice = input("RUN: ")
        if choice   == "1":     return  table_option_handler("Person")
        elif choice == "2":     return  table_option_handler("Phone")
        elif choice == "3":     return  table_option_handler("Pass")
        elif choice == "4":     return  table_option_handler("shift_demand")
        elif choice == "5":     return  table_option_handler("availability")
        elif choice == "6":     return  table_option_handler("department")
        elif choice == "7":     return  table_option_handler("avd_anstid")
        elif choice == "0":     print("YOU WILL BE ASSIMILATED!..*host* umm"+
                                      " jag menar eh, ERROR! juste! ERROR.")
        else:                   inv_inp()

def main_menu():
    ''' Basic menu printer '''
    print("\n_____PACA PSQL INTERFACE_____\n")
    print("  1) Person")
    print("  2) Phone")
    print("  3) Pass")
    print("  4) shift_demand")
    print("  5) availability")
    print("  6) department")
    print("  7) avd_anstid")
    print("  0) END PROGRAM")
    print("-- Utkast 1 --")

def table_options(table):
    ''' Basic manu printer '''
    print ("1) Register"    , table)
    print ("2) Search"      , table)
    print ("3) Edit"        , table)
    print ("4) Delete from" , table)
    print ("5) PRINT ALL"   , table)
    if table == "person":
        print ("6) Statistics")
    print ("0) EXIT")

def table_option_handler(table):
    ''' Handles all shared options '''
    table_options(table)
    user_input = input("RUN: ")
    if user_input   == "1":     insert_vars(table)
    elif user_input == "2":     search_in(table)
    elif user_input == "3":     edit(table)
    elif user_input == "4":     delete_from(table)
    elif user_input == "5":     print_all(table)
    elif user_input == "6":     statistics(table)
    elif user_input == "0":     return
    else:                       inv_inp()

######################################
#####  CRUD  ######################### # Create, Read, Update, Delete
######################################
def insert_vars(table):
    ''' Första funktionen i INSERT, bygger INSERT-statement '''
    tidy_col_list = non_serial_cols(table)
    query_input = []
    query_confirm = []
    print("\n__Register new below__")

    # Itererar input för varje kolumn i tidy_col_list (som är fri från PK)
    try:
        
        for column in tidy_col_list:
            new_input = input ("{}:".format(column))
            query_input.append(new_input)
        """
        query_input = ['1', '2018-1-1', '8:00', '1', '', '', 'f']
        """
        
        # Skapa och skicka SQL syntax:
        if query_input[0] != "":
            insert_statement(table, query_input, tidy_col_list)
        else:
            blank_exit()
    except ValueError:
        print("Value error", ValueError)
        blank_exit()

def non_serial_cols(table):
    ''' Andra funktionen i INSERT: Returnerar NON-SERIAL kolumner
        Används av INSERT, returnerar lista på kolumner i table'''
    # Hämtar alla columnnamn
    cursor_execute("Select * FROM {}".format(table))
    colname_list = [desc[0] for desc in cursor.description]

    # Dynamic serial remove on %id
    tidy_col_list =[]
    for column in colname_list:
            if column.endswith(('id')) == False:
                    tidy_col_list.append(column)
    # POST ID-REMOVE CHECK
    print("\nNon-serial columns to fill:")
    for col in tidy_col_list:
        print (col+ ", ", end="")
    row_spacer()
    return tidy_col_list

def insert_statement(table, query_input, tidy_col_list):
    ''' Tredje funktionen i INSERT:
        Composes & sends SQL insert+commit to server '''
    # BYGGER INSERT STATEMENT
    new_values = ""
    a_col = len(query_input)
    print(query_input)
    
    for col in query_input:
            if a_col >=2:
                if col == "":
                    new_values = new_values+("NULL, ").format(col)
                    a_col=a_col-1
                else:
                    new_values = new_values+("'{}', ").format(col)
                    a_col=a_col-1
            else:
                new_values=new_values+("'{}'").format(col)
    col_names = ""
    a_col = len(tidy_col_list)
    for col in tidy_col_list:
            if a_col >=2:
                col_names=col_names+("{}, ").format(col)
                a_col=a_col-1
            else:
                col_names=col_names+("{}").format(col)

#(table, query_input, tidy_col_list, new_values, col_names):
    # PLATSER I BUSSEN?
    if table == "booking":
        if int(query_input[2]) <= int(0):
            conn.rollback()
            print("\n--NULL VALUE NOT ACCEPTED--\n")
            return
        if seats_available(table, query_input) == False:
            print("Det finns inte tillräckligt med lediga platser "
                  +"på den bussen!")
            conn.rollback()
            print("\n--ROLLBACK--\n")
        elif seats_available(table, query_input) == TypeError:
            conn.rollback()
            print("\n--ROLLBACK--\n", TypeError)
        else:
            execute_insert(table, col_names, new_values)

    # REPETERA DEPARTURE?
    elif table == "departure":
        """try:"""

        weeks = int(input("Repeat for how many weeks: "))
        if weeks >= 2:
            ins_x_weeks(table, col_names, new_values, weeks, query_input)
        else:
            execute_insert(table, col_names, new_values)
        """
        except:
            print("ERROR vid REPEAT for WEEKS i insert_statement(table, query_input, tidy_col_list):")
            execute_insert(table, col_names, new_values)
            pass
        """

    else:
        execute_insert(table, col_names, new_values)

def ins_x_weeks(table, col_names, new_values, weeks, query_input):
    ''' Används för att skapa flera inserts över flera veckor'''
    import datetime
    print("NEW VALUES: ", new_values)
    print("query_input: ", query_input)

    
    """today = datetime.date.today()
    print("today      ", today)
    print("today type ", type(today))"""
    row_spacer()



    #str.replace("is", "was")

    weeks = str(weeks)
    date = (query_input[1])
    print("date      ", date)
    print("MÅL: Lista som ser ut som (2018")
    print("date type ", type(date))


    """
    for x in date:
        x.replace("-",",")
    print("date      ", date)
    print("date type ", type(date))"""


    date_format = ""
    for lista in date:
        for char in lista:
            if char == "-":
                date_format += ","
            else:
                date_format += char

    print("date_format TEST: ", date_format)
    print("date_format TEST type: ", type(date_format))
    print("date_format TEST str: ", str(date_format))
    print("date_format TEST str: ", type(str(date_format)))

    print (date_format.strftime('TODAY %Y,%m,%d'))

    print(datetime.date(date))
    print ("We are the {:%d, %m %Y}".format(today))

    for week in weeks:
        loop = int(0)
        while loop <= int(weeks):
            date = (date_format + datetime.timedelta(days=7))
            new_values[1] = date
            execute_insert(table, col_names, new_values)
            loop += int(1)

            #     to_integer(datetime.date(2012, 6, 13))


def seats_available(table, query_input):
    ''' Returnerar FALSE om lediga platser saknas '''
    # INFO on departure
    departure_bookings_statement = ("SELECT regnr_f, sum FROM departure_bookings where depid = {}".format(query_input[1]))
    try:
        cursor.execute(departure_bookings_statement)
        departure_bookings = cursor.fetchone()
        # Available seats on bus from departure
        available_statement = ("SELECT bus.seats FROM bus JOIN departure_bookings"
                           + " as db ON bus.regnr = db.regnr_f WHERE bus.regnr "
                           + " = '{}' and depid = '{}'".format(departure_bookings[0], query_input[1]))
        cursor.execute(available_statement)
        available = cursor.fetchone()
        print("fetchone available") ##########
        for avail in available:
            print("Antal säten i buss {}: {}".format(departure_bookings[0], avail))
    except TypeError:       
        return TypeError
    try:
        departure = int(departure_bookings[1])
        print("Bokningar på departure {}: {}".format(query_input[1], departure))

        lediga_platser = avail - departure
        print("Lediga platser: {}".format(lediga_platser))
        if int(lediga_platser - int(query_input[2])) <= int(-1):
            #print("Bussen är full!")
            return False
        else:
            #print("Det finns inget ledigt i den avgången!")
            return True
    except psycopg2.ProgrammingError as detail:
        print("psycopg2.ProgrammingError:", detail)
    

def execute_insert(table, col_names, new_values):
    ''' Confirmation and execution of insert '''
    # Insert statement skapas
    col_head = column_headers(table)
    insert_statement = ("INSERT INTO {} ({}) VALUES ({});".format(table, col_names, new_values))



    # Bekräftelse
    print ("\nSTATEMENT:\n"+insert_statement)
    col_head = column_headers(table)
    confirm_commit("insert", insert_statement)

    """
    ## Detta är en fetch-confirm som hämtar senaste raden i tabell
    ## Funkar inte riktigt
    colname_list = [desc[0] for desc in cursor.description]
    # EXECUTE & PRINT CONFIRM FROM DB
    fetched = cursor_execute(("SELECT * FROM {}".format(table)))

    # Här blir något fel med bekräftelseprintern
    new_row = fetched[(len(fetched)-1)]
    column_header_printer(col_head)
    for item in new_row:
        column_spacer(item)    """

### SEARCH ####
def search_in(table):
    ''' First search function
    Search handler, calls the separate functions needed for a search '''
    # VG_select * for week X
    exekvera = ("Select * FROM " + table)
    printer_zeug(table, cursor_execute(exekvera))
    print("\n\nARGS: 'ANY' to order by in all columns")
    col = input("Search column: ").lower()
    try:
        if col != "":
            if col == "any":
                order_by(table, ("SELECT * FROM  {}".format(table)))
            else:
                where = input("WHERE "+ col + " = ")
                if where != "":
                    where_statement = where_criteria(table, col, where)
                    order_by(table, where_statement)
        else:
            blank_exit()
    except:
        print("Felaktiga värden\n--Blank/exit--")


def where_criteria(table, col, where):
    ''' SQL syntax för -select from WHERE-
        col = Aktuell kolumn i table
        where = Ett värde i col'''
    if col != "":
        row_spacer()
        where_statement = ("SELECT * FROM  {} WHERE {} = {}".format(table, col, where))
        where_data = cursor_execute(where_statement)
        if where_data == []:
            print("Selection empty")
            return False
        else:
            printer_zeug(table, where_data)
            return where_statement
    else:
        blank_exit()

def order_by(table, where_statement):
    ''' Bygger och exekverar ORDER BY statement '''
    order_input = input("Order by: ")
    if order_input != "":
        order_syntax = (" ORDER BY " + order_input)
        order_by_statement = where_statement + order_syntax

        printer_zeug(table, cursor_execute(order_by_statement))
        return order_by_statement
    else:
        blank_exit()

def statistics(table):
    print("Hr kommer statistik! Wiiee")
    """
        booking_statistics_VG
            VG_åkt mer än x gånger
            VG_Lista sträckor
            VG_antal gnger per sträcka
            VG_lista historik
    """


#### EDIT ####
def edit(table):
    ''' Hanterar hela ändringsprocessen '''
    col_head = column_headers(table)
    print("\nEdit {} ".format(table), end="")
    where = input("WHERE "+ col_head[0] + " = ")
    try:
        change_criteria= where_criteria(table, col_head[0], where)
        edit_statement(table, change_criteria, col_head, where)
    except psycopg2.ProgrammingError:
        print("ProgrammingError")
        blank_exit()


def edit_statement(table, change_criteria, col_head, where):
    if change_criteria != False:
        edit_col = input("\n Column to edit: ")
        if edit_col in col_head:
            new_value = input("\nNew value for {}: ".format(edit_col))
            if new_value != "":
                print("") # SPACER
                edit_statement = ("UPDATE {0} SET {1}={2} WHERE {3}={4};".format(table, edit_col, new_value, col_head[0], where))
                print(edit_statement)
                confirm_commit("insert", edit_statement)
            else:
                blank_exit()
        elif edit_col not in col_head:
            inv_inp()
        else:
            blank_exit()

#### DELETE ####
def delete_from(table):
    ''' Bygger DELETE-statement '''
    col_head = column_headers(table)
    print("\nObs! Delete is case-sensitive!")
    where = input("Where {} = ".format(col_head[0])).lower() #PK
    if table == "departure":
        edit_statement = ("UPDATE {0} SET {3}={4} WHERE {1}={2};".format(table, col_head[0], where, col_head[7], True))
        print(edit_statement)
        confirm_commit("update", edit_statement)
    else:
        if where != "":
            delete_statement = ("DELETE FROM {} WHERE {} = '{}';".format(table, col_head[0], where))
            print ("\nSTATEMENT:\n"+delete_statement)
            # Bekräfta data
            where_statement = (table, col_head[0], where)
            where_statement = ("SELECT * FROM {} WHERE {}='{}';".format(table, col_head[0], where))
            print("\nTO DELETE: \n"+where_statement)
            records = cursor_execute(where_statement)
            print(*col_head)

            for record in records:
                for item in record:
                    column_spacer(item)
                row_spacer()

                            
            available_statement = ("SELECT {0} FROM {1} WHERE {0} = {2}".format(col_head[0], table, where))
            cursor.execute(available_statement)
            available = cursor.fetchone()
            available = int(*available)            
            if available == int(where):
                confirm_commit("delete", delete_statement)
            elif available == None:
                print(where, "not existing in", table)
            else:
                print("Tokigt")
        else:
            blank_exit()

######################################
#####  ASSISTIVE  ####################
######################################
def confirm_commit(action, statement):
    ''' Bekräftelse av commit + boolean return'''
    confirm = input("\nBekräfta {} y/n: ".format(action)).lower()
    if confirm == "y":
        try:
            cursor.execute(statement)
            conn.commit()
            print("\n--COMMIT--\n")
            return True
        except psycopg2.DataError:
            conn.rollback()
            print("\n--ROLLBACK--\n", psycopg2.DataError)
            return False
        except psycopg2.IntegrityError:
            conn.rollback()
            print("\n--ROLLBACK--\n", psycopg2.IntegrityError)
            return False
    else:
        blank_exit()
        return False

def print_all(table):
    ''' Prints entire content of table '''
    exekvera = ("Select * FROM " + table)
    cursor.execute(exekvera)
    data = cursor.fetchall()

    #data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]

    col_width = max(len(str(item)) for row in data for item in row) + 2  # padding
    for row in data:
        print ("".join(item.ljust(col_width) for item in row))


    """
    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print "".join(word.ljust(col_width) for word in row)
    """
    

def printer_zeug(table, record):
    ''' Printar nästlade listor! '''
    column_header_printer(column_headers(table))
    for row in record:
        for item in row:
            column_spacer(item)
        row_spacer()

def column_headers(table):
    ''' Returns ALL colnames from current table '''
    cursor_execute("Select * FROM " + table)
    colname_list = [desc[0] for desc in cursor.description]
    return colname_list

def column_header_printer(col_head):
    ''' Ökar antalet serveranrop (genom anrop:column_headers)
        men snyggar till och förenklar funktioner    '''
    for name in col_head:
        column_spacer(name)
    row_spacer()

def column_spacer(obj):
    ''' Gör så att vi kan ändra spacing på alla prints från samma ställe '''
    print("%11s" % (obj), end="")

    """data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]

    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print "".join(word.ljust(col_width) for word in row)"""

def inv_inp():
    print("\n_Invalid input!_\n")

def cursor_execute(psql_string):
    ''' Short-hand code for PSQL-communication
        Exempel: cursor_execute("SELECT "+ col +" FROM "+ sel) '''
    cursor.execute(psql_string)
    return cursor.fetchall()

def blank_exit():
    print("-- Blank = Exit --")

def row_spacer():
    print("")

######################################
#####  RUN  ##########################
######################################
main()
