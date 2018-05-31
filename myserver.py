from flask import Flask, request
import logging
from data_mos_req import get_data
from constants import data_mos_url

logging.getLogger().setLevel(logging.INFO)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/names')
def names():
    data_mos = get_data(data_mos_url)
    result = '''
Данные с сайта {site_url}
<b>Сведения о наиболее популярных женских именах среди новорожденных</b>
<table>
    <tr>
        <th>#1</th>
        <th>Имя</th>
        <th>Количество человек</th>
        <th>Год</th>
        <th>Месяц</th>
    </tr>'''.format(site_url=data_mos_url)

    for row in data_mos:
        number = row['Number']
        name = row['Cells']['Name']
        cnt = row['Cells']['NumberOfPersons']
        year = row['Cells']['Year']
        month = row['Cells']['Month']
        result += '''
    <tr>
        <td>{Number}</td>
        <td>{Name}</td>
        <td>{NumberOfPersons}</td>
        <td>{Year}</td>
        <td>{Month}</td>
    </tr>
'''.format(Number=number, Name=name, NumberOfPersons=cnt, Year=year, Month=month)

    result +='< / table >'
    #logging.info(result)
    return result


if __name__ == '__main__':
    app.run(port=5000, debug=True)