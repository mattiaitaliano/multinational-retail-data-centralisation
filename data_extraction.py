from database_utils import DatabaseConnector
import pandas as pd

class DataExtractor:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.rds_database = self.db.init_db_engine()
        
    def read_rds_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        dataframe = pd.read_sql(query, self.rds_database)
        return dataframe

if __name__ == "__main__":
    extractor = DataExtractor()
    print(extractor.read_rds_table('orders_table'))