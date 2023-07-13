import pandas as pd
from pandas import DataFrame
from datetime import datetime


class ModifyDataframe:

    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe

    @staticmethod
    def convert_dtype_to_string(dataframe: DataFrame):
        return dataframe.astype(str)

    def add_report_upload_date(self, date=datetime.now().strftime('%Y-%m-%d')):
        df = self.dataframe['report_upload_date'] = date
        return df
