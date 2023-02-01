from database_utils import DatabaseConnector
import tabula
import pandas as pd

class DataExtractor:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.rds_database = self.db.init_db_engine()
        
    def read_rds_table(self, table_name):
        return pd.read_sql_table(table_name, self.rds_database)
    
    def retrieve_pdf_data(self, pdf_link):
        df_pdf = tabula.read_pdf(pdf_link, pages="all")
        dataframe = pd.DataFrame(df_pdf)
        return dataframe

if __name__ == "__main__":
    extractor = DataExtractor()
    print(extractor.read_rds_table("orders_table"))