import psycopg2

conn = psycopg2.connect(database='postgres',user='postgres',host='localhost',port='5433',password='11111111')
print('Done!)')
conn.autocommit = True

try:
    connection = psycopg2.connect(database='postgres',user='postgres',host='localhost',port='5433',password='11111111')
    #cursor = conn.cursor()
    #test conekta db
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version:{cursor.fetchone()}")

    #test request

    #with connection.cursor() as cursor:
        #cursor.execute("""CREATE TABLE testik(
        #id serial PRIMARY KEY,
        #first_name varchar(50) NOT NULL,
        #nick_name varchar(50) NOT NULL);""")
        #connection.commit()
    # test create
    #with connection.cursor() as cursor:
        #cursor.execute("""INSERT INTO users(first_name, nick_name) VALUES ('Igor','IgorOk')""")
        #print("[INFO] Data was inserted")

    # ETO KOPIROVANIE IZ TABLICY
    #with connection.cursor() as cursor:
        #cursor.execute("""INSERT INTO testik2(first_name, nick_name) SELECT first_name, nick_name FROM users""")
        #print("Rabotaet!!!")

    # SOZDANIE RED_TABLICI

    #with connection.cursor() as cursor:
        #cursor.execute("""CREATE TABLE dannye(
        #user_id text,
        #created_at text,
        #revenue text,
        #event_name text;""")

    # Dalee s pomoshu PgAdmin4 perenosim dannye iz csv faila v nashu tablicu
    # redaktiruem tablicu

    #with connection.cursor() as cursor:
        #cursor.execute("""ALTER TABLE dannye ALTER COLUMN user_id TYPE varchar(100),
         #ALTER COLUMN event_name TYPE varchar(100)
         #""")
        #print('Chekai')
    #cursor.execute("""ALTER TABLE dannye ALTER COLUMN created_at TYPE timestamp""")

    #Dobavil id v tablicu dla ee redaktirovania

    #with connection.cursor() as cursor:
        #cursor.execute("""ALTER TABLE podbor_vseh_dannyh ADD id serial PRIMARY KEY""")
        #print('Chekai')

    # Udalil oshibki v db     SELECT * FROM dannye WHERE revenue='revenue';

    # Eto korektirovki
    # with connection.cursor() as cursor:
        #cursor.execute("""ALTER TABLE dannye ALTER COLUMN revenue TYPE numeric USING revenue::numeric""")
        #print('Chekai')
    # CORECTIRUU pole id
    # cursor.execute("""ALTER TABLE dannye DROP id""")
    # cursor.execute("""ALTER TABLE dannye ADD id serial PRIMARY KEY""")
    # Soglasno dokumentacii PostgreSQL, dla redaktirovania tablicy nuzno pole ID serial PRIMARY KEY -- sozdaju
    #with connection.cursor() as cursor:
        #cursor.execute("""ALTER TABLE dannye ADD id serial PRIMARY KEY""")
        #print('Gotovo!!!')

    with connection.cursor() as cursor:
        cursor.execute(
            """COPY testik3 (user_id,created_at,revenue,event_name)
            FROM 'D:\Programs\MyDjango_Projects\Data_Analyst_test_task\Data_Base\File_01.csv'
            DELIMITER ','
            CSV HEADER;""")
        connection.close()


    print('Chekai')

except Exception as ex:
    print("[INFO] Error while working with PostgreeSQL", ex)
finally:
    if connection:
        connection.close()
        #cursor.close()
        print("[INFO] PostgreeSQL connection closed")



