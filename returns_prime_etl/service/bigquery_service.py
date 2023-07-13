from pandas import DataFrame
import connection
from google.cloud import bigquery


def save_df_to_table(df: DataFrame, table_name: str):
    bq_client = connection.get_bq_client()
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
        allow_quoted_newlines=True
    )
    job = bq_client.load_table_from_dataframe(
        df, destination=table_name, job_config=job_config
    )
    job.result()