import pandas as pd

def generate_bq_schema(data : pd.DataFrame):
    dtype_mapping = {
    'object': 'STRING',
    'string': 'STRING',
    'Int64': 'INT64',
    'int64': 'INT64',
    'float64': 'FLOAT64',
    'boolean': 'BOOL',
    'bool': 'BOOL',
    'date': 'DATE',
    'datetime64[ns]': 'TIMESTAMP'
    }

    schema = []
    for col, dtype in data.dtypes.items():
        dtype_str = str(dtype)
        bq_type = dtype_mapping.get(dtype_str, 'STRING')
        schema.append({'name': col, 'type': bq_type})
    return(schema)
