import pandas as pd

class DataCleaning:
    
    def clean_user_data(self, data, tablename):
        
        if tablename is "orders_table":
            data = data[['date_uuid', 'first_name', 'last_name', 'user_uuid', 'card_number', 'store_code', 'product_code', 'product_quantity']]
            data = data[(data["first_name"].notnull()) | (data["last_name"].notnull()) ]
        elif tablename is "legacy_users":
            data = data[[ 'first_name', 'last_name', 'date_of_birth', 'company', 'email_address', 'address', 'country', 'country_code', 'phone_number', 'join_date', 'user_uuid']]
        elif tablename is "legacy_store_details":
             data = data[['address', 'longitude', 'locality', 'store_code', 'staff_numbers', 'opening_date', 'store_type', 'latitude', 'country_code', 'continent']]
             data.loc[data["continent"] == "eeAmerica", "continent"] = "America"
             data.loc[data["continent"] == "eeEurope", "continent"] = "Europe"
             data = data[(data['continent'] == 'Europe') | (data['continent'] == 'America') | (data['continent'].isna())]
             data = data.fillna("N/A")
    
        return data


    def clean_card_data(self, data):
        new_data = data
        # remove empty lines
        new_data = new_data.dropna()
        # remove NULL's values rows
        new_data = new_data.dropna(inplace=True)

        return new_data
