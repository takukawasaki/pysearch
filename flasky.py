

import searchengine as s
import nn
from flask import Flask
from flask import render_template, request
import os


mynet = nn.searchnet("nn.db")

tempate = os.path.join(os.getcwd(),'templates')
app = Flask(__name__,template_folder=tempate)

def makeindex(key):
  e = s.searcher('searchindex.db')
  result = e.query(key)
  List = []
  size = len(result)
  for i in range(size):
    for j in result[i]:
      List.append(e.geturlname(j))
  return List


@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'POST':
    keyword = request.form['keyword']
    res_list = makeindex(keyword)
    if keyword:
      return render_template(
        'search.html',
        query = res_list,
        keyword = keyword)
    else:
      return 'not exists'
  return render_template('search.html')

  
if __name__=='__main__':
  app.run()
