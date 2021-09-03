import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='teste',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

update_query = "update employee set name='Lucas' where _id = 1"

try:
    cursor.execute(update_query)
    connection.commit()
    print("Record update")
except Exception as e:
    connection.rollback()
    print("Exception Occurred: ", e)

connection.close()