import pandas as pd

class DataCleaning:
    
    def clean_user_data(self, data):
        new_data = data
        # remove empty lines
        new_data = new_data.dropna()
        # remove NULL's values rows
        new_data = new_data.dropna(inplace=True)

        return new_data

    def clean_card_data(self, data):
        new_data = data
        # remove empty lines
        new_data = new_data.dropna()
        # remove NULL's values rows
        new_data = new_data.dropna(inplace=True)

        return new_data
