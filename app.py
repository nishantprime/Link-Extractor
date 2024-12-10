from flask import Flask, render_template, request
from helper import get_page_links

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            url = request.form['URL']
            links = get_page_links(url)
            if links == 0:
                return render_template('index.html', error = 'Site not accessable')
            if not links:
                return render_template('index.html', error = 'No Links Found')
            return render_template('index.html', links=links)
        except Exception as e:
            return render_template('index.html', error = str(e))
if __name__ == '__main__':
    app.run(debug=True)
