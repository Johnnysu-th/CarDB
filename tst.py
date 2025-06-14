#docstring- SteveRod






import sqlite3




DATABASE = "car.db"





 
#functionss
def print_all_name():
    '''print all the name nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "Select * from car;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name           top_speed       country    maker    id")
    for car in results:
        #print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}{car[4]:<4}{car[5]:<4}{car[6]:<4}")
        print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}")
        #loop finished here
    db.close()

def print_all_name_by_topspeed():
    '''print all the name by topspeed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "Select * from carORDER BY top_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name           top_speed       country    maker    id")
    for car in results:
        #print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}{car[4]:<4}{car[5]:<4}{car[6]:<4}")
        print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}")
        #loop finished here
    db.close()

def print_all_name_by_country():
    '''print all the name storted by country'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "Select * from car ORDER BY country DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name           top_speed       country    maker    id")
    for car in results:
        #print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}{car[4]:<4}{car[5]:<4}{car[6]:<4}")
        print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}")
        #loop finished here
    db.close()

def print_all_name_by_maker():
    '''print all the name storted by maker'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "Select * from carORDER BY maker DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name           top_speed       country    maker    id")
    for car in results:
        #print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}{car[4]:<4}{car[5]:<4}{car[6]:<4}")
        print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}")
        #loop finished here
    db.close()

def print_all_name_by_id():
    '''print all the name storted by id'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "Select * from carORDER BY id DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name           top_speed       country    maker    id")
    for car in results:
        #print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}{car[4]:<4}{car[5]:<4}{car[6]:<4}")
        print(f"{car[1]:<30}{car[2]:<8}{car[3]:<4}")
        #loop finished here
    db.close()


#main code
while True:
    user_input = input("""
What would you like to do.
1.Print all name
2.Print all name sorted by topspeed
3.Print all name sorted by country
4.Print all name sorted by maker
5.Print all name sorted by id
6.Exit
""")
    if user_input == "1":
        print_all_name()
    elif user_input == "2":
        print_all_name_by_topspeed()
    elif user_input == "3":
        print_all_name_by_country()
    elif user_input == "4":
        print_all_name_by_maker()
    elif user_input == "5":
        print_all_name_by_id()
    elif user_input == "6":
        break
    
    else:
        print("That was not a option\n")


