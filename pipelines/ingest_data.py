import argparse
import yaml
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_gbq

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = load_config()
    id_project = config['id_project']
    api_url = config['api_base_url']

    parser = argparse.ArgumentParser()
    parser.add_argument("--data_name", type = str, help = "Data Extracted")
    parser.add_argument("--dataset_name", type = str, help = "Destination Dataset Name")
    parser.add_argument("--dest_table_name", type = str, help = "Destination Table Name")
    args = parser.parse_args()

    # Extract Data
    raw_df = extract_data(args.data_name, api_url)
    print("1. Extract Done")

    # Transform Data
    clean_df = transform_data(raw_df)
    print("2. Transform Done")

    # Load Data
    load_to_gbq(
        data = clean_df,
        dataset_name = args.dataset_name,
        destination_table_name = args.dest_table_name,
        id_project = id_project
        )