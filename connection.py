import pathlib
from google.oauth2 import service_account
from google.cloud import bigquery


def get_bq_client():
    credentials = service_account.Credentials.from_service_account_file(
        filename=f"{pathlib.Path(__file__).parent.resolve()}\double-exchange-300905-e1e0a75aaa35.json",
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    bq_client = bigquery.Client(credentials=credentials, project=credentials.project_id)