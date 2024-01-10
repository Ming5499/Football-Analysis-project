import pandas as pd
from bs4 import BeautifulSoup
import requests


def extract_match_data(year):
    url = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    
    return df_football


def transform_match_data(ti, years):
    df_football = ti.xcom_pull(task_ids='extract_match_data', key='return_value')
    match = [extract_match_data(year) for year in years]
    df_match = pd.concat(match, ignore_index=True)
    return df_match


def load_match_data(ti, file_name):
    data = ti.xcom_pull(task_ids='transform_match_data', key='return_value')
    data.to_csv(file_name, index=False)
    print(f"Data has been saved to {file_name}")