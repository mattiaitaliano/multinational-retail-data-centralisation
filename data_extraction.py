from database_utils import DatabaseConnector
import tabula as t
import pandas as pd

class DataExtractor:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.rds_database = self.db.init_db_engine()
        
    def read_rds_table(self, table_name):
        return pd.read_sql_table(table_name, self.rds_database)
    
    def retrieve_pdf_data(self, pdf_link):
        pdf_dataframes = t.read_pdf(pdf_link, pages="all")
        return pd.concat(pdf_dataframes,ignore_index=True)

if __name__ == "__main__":
    extractor = DataExtractor()
    print(extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"))