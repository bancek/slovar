from flask import Flask, render_template, request, url_for, redirect
from pyquery import PyQuery as pq

app = Flask(__name__)

def get_search_results(query):
    d = pq(url='http://slovarji.najdi.si/najdi/%s' % query)
    a = d('#contentDict')
    a('a').attr('onclick', '')
    a('.dict_search_more_pons').remove()
    a('.dict_source').remove()
    a('.dict_title_wrapp').remove()
    return a.html().replace('&#13;', '')

@app.route('/')
def index():
    if 'q' in request.args:
        return redirect(url_for('search', query=request.args['q']))

    return render_template('index.html')

@app.route('/najdi/<query>')
def search(query=None):
    results = ''

    if query:
        results = get_search_results(query)

    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
