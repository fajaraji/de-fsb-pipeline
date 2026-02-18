import pandas as pd
from pandas_gbq import to_gbq
from src.schema_generator import generate_bq_schema
from src.connect_gbq import connect_to_gbq

def load_to_gbq(
    data : pd.DataFrame,
    dataset_name : str,
    destination_table_name : str,
    id_project : str
):
    table_schema_datamart = generate_bq_schema(data)
    client = connect_to_gbq()
    to_gbq(
        data,
        destination_table = f'{dataset_name}.{destination_table_name}',
        project_id = id_project,
        if_exists = 'append',
        table_schema = table_schema_datamart,
        credentials=client._credentials
    )
    print(f'{destination_table_name} has been loaded successfully!')