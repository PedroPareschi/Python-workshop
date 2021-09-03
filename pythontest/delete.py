import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='teste',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

delete_query = "delete from employee where _id = 1"

try:
    cursor.execute(delete_query)
    connection.commit()
    print("Record delete")
except Exception as e:
    connection.rollback()
    print("Exception Occurred: ", e)

connection.close()