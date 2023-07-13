import gspread
import pandas as pd
import time


class GdriveData:

    def __init__(self, service_account_path: str):
        self.service_account_path = service_account_path

    def generate_gdrive_client(self):
        return gspread.service_account(filename=f"{self.service_account_path}")

    def fetch_columns_from_api(self, date, client, col_num :int):
        return client.open(f"report_{date}").sheet1.col_values(col_num)[2:]

    def create_df(self, client, date, columns:list):
        df = pd.DataFrame()
        for i in range(len(columns)):
            print(columns[i])
            x = self.fetch_columns_from_api(date, client, i + 1)
            df[f'{columns[i]}'] = pd.Series(x)
            time.sleep(2)
        return df
