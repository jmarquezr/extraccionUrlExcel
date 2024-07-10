import requests
import pandas as pd
import os
from bs4 import BeautifulSoup

DATA_URL = 'https://es.wikipedia.org/wiki/Anexo:Destinos_tur%C3%ADsticos_mundiales'
OUTPUT_FILE = 'D:\\paractica1\\data.xlsx'

def extract_data():
    response = requests.get(DATA_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract table data
    table = soup.find_all('table')[0]  # Assuming the first table contains the relevant data
    df = pd.read_html(str(table))[0]

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(OUTPUT_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df.to_excel(OUTPUT_FILE, index=False)
    print(f'Data extracted and saved to {OUTPUT_FILE}')

if __name__ == "__main__":
    extract_data()
