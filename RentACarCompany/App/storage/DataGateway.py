import psycopg2
import psycopg2.extras


class DataGateway:
    conn = psycopg2.connect(dbname='RentACarCompany',
                            user='admin',
                            password='admin',
                            host='localhost')

    @staticmethod
    def getCursor():
        return DataGateway.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
