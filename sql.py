import sqlite3


class DBConnector():
    def __init__(self) -> None:
        self.conn = sqlite3.connect('inventory.db',timeout=10,check_same_thread=False)
        self.cursor = self.conn.cursor()

   
    
    def init(self):
        self.execute('PRAGMA foreign_keys=ON;')
        self.execute('CREATE TABLE IF NOT EXISTS component(componentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,component_name TEXT NOT NULL, UNIQUE(component_name));')
        self.execute('CREATE TABLE IF NOT EXISTS componentdata(serial TEXT PRIMARY KEY NOT NULL,description TEXT NOT NULL,componentID INTEGER NOT NULL,FOREIGN KEY(componentID) REFERENCES component(componentID));')
        self.execute('INSERT INTO component(component_name) VALUES("RAM"),("HARD DRIVE"),("POWER SUPPLY UNIT"),("MOTHERBOARD"),("PROCCESOR");')

            
    

        
        
    def execute(self,query):
        result = None
        try:
            result=self.cursor.execute(query)
           
            self.conn.commit()
        except sqlite3.Error as err:
            print(err)
        if result:
            return result
            
            
            
