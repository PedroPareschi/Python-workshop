import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='teste',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

name = input("Enter your name: ")
insert_query = """insert into employee(name) values('%s')""" \
               % name

try:
    cursor.execute(insert_query)
    connection.commit()
    print("Name is successfully insert")
except Exception as e:
    connection.rollback()
    print("Exception Occurred: ", e)

connection.close()
