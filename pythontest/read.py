import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='college_management',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

sql_query = "select * from student"
try:
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for record in results:
        _id = record['id']
        print("Id: ", _id)
        birthdate = record['birthdate']
        print("Birthdate: ", birthdate)
        cpf = record['cpf']
        print("CPF: ", cpf)
        email = record['email']
        print("email: ", email)
        name = record['name']
        print("Name: ", name)
        print("\n\n\n")
except Exception as e:
    print(e)
connection.close()
