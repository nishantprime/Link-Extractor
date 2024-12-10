from flask import Flask, render_template, request
import requests
import random
from bs4 import BeautifulSoup
from helper import get_page_links

app = Flask(__name__)

@app.route('/', methods = ['GET','POST']):
  def home():
    if request.method == 'GET':
      return render_template('index.html')
    else:
      url = request.form['URL']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}



