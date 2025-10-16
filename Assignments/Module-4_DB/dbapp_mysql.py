import pymysql

try:
    db=pymysql.connect(host="localhost",user="root",password="",database="09jul_db")
    print("Database connected!")
except Exception as e:
    print(e)

cr=db.cursor()
    
#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name text,city text)"

try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','surat'),('hitesh','baroda'),('nirav','ahmedabad'),('harsh','rajkot')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""
    
#Update Data
"""update_data="update studinfo set name='pritesh',city='jamnagar' where id=3"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""
    
#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    #data=cr.fetchall()
    #data=cr.fetchmany(2)
    data=cr.fetchone()
    print(data)
except Exception as e:
    print(e)