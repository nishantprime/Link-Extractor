from flask import Flask, render_template, request
from helper import get_page_links

app = Flask(__name__)

@app.route('/', methods = ['GET','POST']):
  def home():
    if request.method == 'GET':
      return render_template('index.html')
    else:
      url = request.form['URL']
      links = get_page_links(url)
      return render_template('index.html', links=links)



