import psycopg2

from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # connection.autocommit = True
    
    # the cursor for performing database operations
    with connection.cursor() as cursor:
        # sql_query = "SELECT version();"
        # cursor.execute(sql_query)
        # print(f"Server version: {cursor.fetchone()}")

        # create_table_query = "CREATE TABLE users (" \
        #                      "id serial PRIMARY KEY, " \
        #                      "first_name varchar(30) NOT NULL," \
        #                      "last_name varchar(30) NOT NULL);"
        # cursor.execute(create_table_query)
        # connection.commit()
        # print("Table created successfully")

    
        # insert_data_query = "INSERT INTO users (first_name, last_name)" \
        #                     "VALUES ('Anna', 'Petrenko');"
        # cursor.execute(insert_data_query)
        # connection.commit()
        # print("Insert data was successfully")

   
        # insert_data_query = "INSERT INTO users (first_name, last_name)" \
        #                     "VALUES ('Dana', 'Bebeshko');"
        # cursor.execute(insert_data_query)
        # connection.commit()
        # print("Insert data was successfully")
        
        select_data_query = "SELECT * FROM users;"
        cursor.execute(select_data_query)
        print(cursor.fetchall())

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print(f"[INFO] PostgreSQL connection closed")