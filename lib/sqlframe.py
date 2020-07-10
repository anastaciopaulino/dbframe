import sqlite3

class SQL(): 
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(str(self.dbname) + '.db')
        self.cursor = self.conn.cursor()
    
    def __str__(self):
        return "Conectado em: %s" %(self.dbname)
    
    def create(self, query):
        self.cursor.execute(str(query))
    
    def insert(self, query, parameters):
        if type(parameters) == tuple:
            self.cursor.execute(str(query), parameters)
        else:
            self.cursor.executemany(str(query), parameters)
    
    def alter_table(self, query, parameters):
        self.cursor.execute(str(query), parameters)

    def commit(self):
        self.conn.commit()
        return "Alterações gravadas"
    
    def rollback(self):
        self.conn.rollback()
        return "Alterações abortadas"

    def select(self, query):
        self.cursor.execute(str(query))
        results = self.cursor.fetchall()

        return results

    def search(self, query, parameters):
        self.cursor.execute(query, parameters)
        results = self.cursor.fetchone()

        return results
    
    def update(self, query, parameters):
        self.cursor.execute(query, parameters)

        return "Registros alterados: {}" .format(self.cursor.rowcount)

    def delete(self, query, parameters):
        self.cursor.execute(query, parameters)
        return "Registros apagados: {}" .format(self.cursor.rowcount)

    def close(self):
        self.cursor.close()
        self.conn.close()
