import yaml
from sqlalchemy import create_engine, inspect 
import psycopg2

class DatabaseConnector:
    
    def read_db_creds(self):
        with open('db_creds.yaml') as f:
            data = yaml.safe_load(f)
        return data

    def init_db_engine(self):
        config = self.read_db_creds()
        engine = create_engine(f"postgresql://{config['RDS_USER']}:{config['RDS_PASSWORD']}@{config['RDS_HOST']}:{config['RDS_PORT']}/{config['RDS_DATABASE']}")
        engine.connect()
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        
        engine.connect()

        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self, df, table_name):
        local_engine = create_engine('postgresql://admin:adm1n@localhost:5432/Sales_Data')
        df.to_sql(table_name, local_engine, if_exists='replace')

if __name__ == '__main__':
    db = DatabaseConnector()
    print(db.list_db_tables())
