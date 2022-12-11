import mysql.connector

test_db = mysql.connector.connect(
	host='localhost',
	user='root',
	password='03031995vlad',
	database='testdata'
)

cursor = test_db.cursor()
sql = 'insert into customers (name, address) values (%s, %s)'
values = [
	('Peter', 'Lowstreet 4'),
	('Amy', 'Apple st 652'),
	('Hannah', 'Mountain 21'),
	('Michael', 'Valley 345'),
	('Sandy', 'Ocean blvd 2'),
	('Betty', 'Green Grass 1'),
	('Richard', 'Sky st 331'),
	('Susan', 'One way 98'),
	('Vicky', 'Yellow Garden 2'),
	('Ben', 'Park Lane 38'),
	('William', 'Central st 954'),
	('Chuck', 'Main Road 989'),
	('Viola', 'Sideway 1633')
]

cursor.executemany(sql, values)
test_db.commit()
test_db.close()