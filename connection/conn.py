import psycopg2

class Connection:
    def __init__(self, server='127.0.0.1', user='postgres',
                        pasword='root', database='reto6', port=5432):
        self.db= psycopg2.connect( user=user, password=pasword, host=server, port=port, database=database)
        self.cursor = self.db.cursor()
    
    def execute_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def close_connection(self):
        self.db.close()
        print("Se ha desconcectado de la base de datos")
    
    def commit(self):
        self.db.commit()
        return True