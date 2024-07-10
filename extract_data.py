import requests
import pandas as pd
import os
from bs4 import BeautifulSoup

#DATA_URL = 'https://es.wikipedia.org/wiki/Anexo:Destinos_tur%C3%ADsticos_mundiales'


# Abrir el archivo de configuración
with open('urls.txt', 'r') as file:
    # Leer todas las líneas
    urls = file.readlines()
    
    # Quitar los caracteres de nueva línea al final de cada línea
    urls = [url.strip() for url in urls]


#OUTPUT_FILE = 'D:\\paractica1\\data.xlsx'
OUTPUT_FILE = 'D:\\paractica1\\data'


def extract_data():

    contador=1
    for DATA_URL in urls:
        response = requests.get(DATA_URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract table data
        table = soup.find_all('table')[0]  # Assuming the first table contains the relevant data
        df = pd.read_html(str(table))[0]
        
        new_path = os.path.join(OUTPUT_FILE, contador,'.xlsx')

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(new_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        df.to_excel(OUTPUT_FILE, index=False)
        print(f'Data extracted and saved to {OUTPUT_FILE}')


if __name__ == "__main__":
    extract_data()
