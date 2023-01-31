import yaml
from sqlalchemy import create_engine 
import psycopg2

class DatabaseConnector:
    
    def read_db_creds(self):
        with open('db_creds.yaml') as f:
            data = yaml.safe_load(f)
        return data

    def init_db_engine(self):
        config = self.read_db_creds()
        engine = create_engine(f"postgresql://{config['RDS_USER']}:{config['RDS_PASSWORD']}@{config['RDS_HOST']}:{config['RDS_PORT']}/{config['RDS_DATABASE']}")
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        with engine.connect() as conn:
            result = conn.execute('''
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
            ''')
            return [row[0] for row in result]

    def upload_to_db(self, dataframe, table_name):
        pass

if __name__ == '__main__':
    db = DatabaseConnector()
    print(db.list_db_tables())
