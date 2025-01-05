import sqlite3

class Database :
    def __init__(self , db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(''' create table if not exists market
                          (id integer primary key , name text , price integer , price2 integer , number integer) ''')
        self.con.commit()


    
    def insert_table(self , name , price , price2 , number):
        self.cur.execute('''insert into market values (Null , ? , ? , ? ,?
                         )''' , (name , price , price2 , number))
        self.con.commit()
        
        print(self.cur.rowcount , 'record inserted!')
        print('last ID is : ' , self.cur.lastrowid)
        
        
    def select_record(self):
        self.cur.execute('select * from market')
        record =  self.cur.fetchall()
        return record
    
    def delete_record (self , id):
        self.cur.execute('delete from market where id = ? ' , (id ,) )
        self.con.commit()
        
        
    def update_records (self , id , name , price , price2 , number ):
        self.cur.execute('''update market set name = ? , buy = ? , sale = ?
                         , number = ? where id = ? ''' , (name, price , price2 , number , id ))
                         
        self.con.commit()
        
        
    def search_records(self , name):
        self.cur.execute('select * from market where name = ? ' , (name,) )
        row = self.cur.fetchone()
        return row
    
    