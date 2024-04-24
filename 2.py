import psycopg2 

conn = psycopg2.connect(dbname='python_data', host='localhost', port='5432', user='postgres', password='sam77')
curr = conn.cursor()

curr.execute('CREATE TABLE product(id serial primary key, name varchar(20) , price bigint , color varchar(15))')
curr.execute("""
    INSERT INTO users (id, name, price ,color) VALUES 
""" (1, "Samsung A72" , "black",  452.125478))
conn.commit()
conn.close()

