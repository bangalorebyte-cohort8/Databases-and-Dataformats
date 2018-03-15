import psycopg2

conn = psycopg2.connect(database = "testdb1", user = "lakshmi")
print("Opened database successfully")

cur = conn.cursor()

#cur.execute('''CREATE TABLE products (
#    product_id integer NOT NULL,
#    product_name text NOT NULL,
#    product_desc text,
#    product_price numeric NOT NULL CHECK(product_price > 0)


#);''')

cur.execute('''INSERT INTO products (product_id, product_name, product_price ) VALUES(2,'s',20);''')

cur.execute('''SELECT * FROM products; ''')

rows = cur.fetchall()

for row in rows:
    print(row[0],row[1],row[2],row[3])

conn.commit()
conn.close()