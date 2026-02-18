from google.oauth2 import service_account
from google.cloud import bigquery
import yaml

def connect_to_gbq():
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    key_path = config['service_account_key']
    project_id = config['id_project']
    
    credentials = service_account.Credentials.from_service_account_file(key_path)
    
    client = bigquery.Client(credentials=credentials, project=project_id)
    
    return client