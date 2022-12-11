import mysql.connector

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='03031995vlad'
)

cursor = conn.cursor()
queries = ['create database my_first_db',
		   'use my_first_db',
		   'create table students (id int, name varchar(255))',
		   'create table employees (id int auto_increment primary key, name varchar(255), salary int(6))',
		   'alter table students modify id int primary key',
		   'insert into students (id, name) values (01, \'John\')',
		   'insert into employees(name, salary) values (\'John\', 10000)']

for query in queries:
	cursor.execute(query)

conn.commit()
conn.close()