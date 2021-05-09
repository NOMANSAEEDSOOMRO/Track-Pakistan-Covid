from flask import Flask , render_template
from flask import jsonify
import requests
from bs4 import BeautifulSoup as soup

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Track_Covid_Pak_API")
def API():
    url = "https://dunyanews.tv/coronavirus/graph/"
    content = requests.get(url)
    page = content.content

    s = soup(page, 'html.parser')
    div = s.find('div', id="coronaTable")
    div1 = div.find('div', {"class": "table-responsive d-none d-sm-block"})
    h, [_, *d] = [i.text for i in div1.tr.find_all('th')], [[i.text for i in b.find_all(['th', 'td'])] for b in div1.find_all('tr')]

    result = [dict(zip(h, i)) for i in d]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)