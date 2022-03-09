# Script for connecting and querying a mysql database

import mysql.connector
from mysql.connector import connect, Error

query = "SELECT c.ID as 'Customer ID', c.name as 'Organization', a.Street, co.FirstName, co.LastName FROM DMS.customer c inner join contact"
query += " as co on co.customerid = c.ID and co.Active = 1 and co.Primary = 1"
query += " inner join address as a on a.CustomerID = c.ID and a.active = 1 where c.active = 1 ;"
counter = 0
try:
    with connect(
        host = "",
        user = "",
        password = "",
        database = "",
        port=3306
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            for row in cursor:
                if(counter == 10):
                    break
                print(row)
                counter+=1
except Error as e:
    print("Error: \n")
    print(e)