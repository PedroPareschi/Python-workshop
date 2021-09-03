import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='teste',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
sql_query = "SELECT VERSION()"

try:
    cursor.execute(sql_query)
    data = cursor.fetchone()
    print("Database Version: %s" %data)
except Exception as e:
    print("Exception: ", e)

connection.close()