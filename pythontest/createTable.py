import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='teste',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
delete_existing_table = "drop table if exists employee"
create_table_query = """create table employee(
_id int auto_increment primary key,
name varchar(20) not null
)"""
try:
    cursor.execute(delete_existing_table)
    print("Deleting existing table")
    cursor.execute(create_table_query)
    print("Employee Table was created")
except Exception as e:
    print("Exception Occurred: ", e)
connection.close()
