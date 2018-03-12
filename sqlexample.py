#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

query = 'CREATE TABLE test(testid integer, testname text);'

cursor.execute(query)

query = "INSERT INTO test VALUES(1,'abcd');"
cursor.execute(query)

query = "INSERT INTO test VALUES(2,'efgh');"
cursor.execute(query)

query = 'SELECT * FROM test;'
cursor.execute(query)

print(cursor.fetchall())

connection.commit()
connection.close()

