import pandas as pd
from datetime import datetime

def transform_data(df: pd.DataFrame):
    # Logic pembersihan pindah kesini
    if 'created_date' in df.columns:
        df['created_date'] = df['created_date'].astype('datetime64[ns]')
    if 'updated_date' in df.columns:
        df['updated_date'] = df['updated_date'].astype('datetime64[ns]')
    
    df['landing_date'] = datetime.now()
    return df