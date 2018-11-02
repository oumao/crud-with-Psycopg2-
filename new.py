import os
import psycopg2

# creating connection to the postgres database using psycopg2 library
con = psycopg2.connect(host='localhost', user='postgres',
                       password='oumaruc2016', port=5400, dbname='futgen')
curs = con.cursor()

# create table users


def createTable(con=None):
    try:
        if con == None:
            return False
        curs.execute(
            "create table users(id serial primary key not null, username character varying(200) not null, password integer not null)")
        con.commit()
        con.close()
    except Exception as err:
        raise err

# function to add users in the table users


def addUser(id, username, password):
    try:
        curs.execute("insert into users(id, username, password) values(?, ?, ?)", (
            id, username, password))
        con.commit()
        con.rollback()
    except Exception as err:
        raise err


if __name__ == '__main__':
    addUser(3, 'John', 678909)
