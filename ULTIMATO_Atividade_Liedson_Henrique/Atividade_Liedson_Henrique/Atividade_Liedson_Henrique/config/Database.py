import psycopg2

class Database:
    def __init__(self, config: dict) -> None:
        self.connect(config)

    def connect(self, config: dict):
        self.conn = None

        try:
            print('Conectando com Postgre...')
            self.conn = psycopg2.connect(**config)

            cur = self.conn.cursor()

            print('Postgre database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)

            cur.close()
        except (Exception, psycopg2.connect.DatabaseError) as error:
            print(error)