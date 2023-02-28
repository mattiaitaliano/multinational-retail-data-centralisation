from database_utils import DatabaseConnector
import tabula as t
import pandas as pd
import requests

class DataExtractor:
    
    def __init__(self):
        self.db = DatabaseConnector()
        self.rds_database = self.db.init_db_engine()
        self.api_key ={'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        
    def read_rds_table(self, table_name):
        return pd.read_sql_table(table_name, self.rds_database)
    
    def retrieve_pdf_data(self, pdf_link):
        pdf_dataframes = t.read_pdf(pdf_link, pages="all")
        return pd.concat(pdf_dataframes,ignore_index=True)
    
    def list_number_of_store(self):
        stores = requests.get('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores',headers=self.api_key)
        n_of_stores = stores.json()
        return n_of_stores["number_stores"]
    
    def retrieve_stores_data(self):
        n_of_stores = self.list_number_of_store()
        stores_list = []
        for store_number in range(0, n_of_stores):
            stores_list.append(requests.get('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'+str(store_number), headers=self.api_key).json())
        return pd.json_normalize(stores_list)

        

if __name__ == "__main__":
    extractor = DataExtractor()
    print(extractor.read_rds_table("orders_table"))