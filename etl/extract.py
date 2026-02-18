import requests
import pandas as pd

def extract_data(data_name : str, base_url : str):
    url = f"{base_url}{data_name}"
    response = requests.get(url)
    data = response.json()
    data_extracted = pd.DataFrame(data)

    return(data_extracted)