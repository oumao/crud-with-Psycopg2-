import os
import psycopg2

con = psycopg2.connect(host='localhost', user='postgres',
                       password='oumaruc2016', port=5400, dbname='futchat')
curs = con.cursor()

def createUser(con=None):
    try:
        if con == None:
            return False
        sql = """create table users if doesnot exist(id serial not null,
                                                     username text not null, 
                                                     password varchar not null)"""
        curs.execute(sql)
        con.commit()
        con.close()
    except Exception as err:
        return ('Couldnot create user',err)  

def addUser(name, passw):
    try:
        if con == None:
            return False
        curs.execute("""INSERT INTO users values({0},{1})""".format(name, passw))
        con.commit()
        con.close()
    except Exception as e:
        raise e
        
if __name__ == '__main__':
    # createUser(con)
     addUser('Ouma', 'tom123')
   