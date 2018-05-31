import requests
import logging
from constants import data_mos_url

logging.getLogger().setLevel(logging.INFO)


def get_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        logging.info('Error: %s' % result.status_code)


if __name__ == '__main__':
    req = get_data(data_mos_url)
    row = req[0]
    logging.info(row)
    name = row['Cells']['Name']
    logging.info(name)
