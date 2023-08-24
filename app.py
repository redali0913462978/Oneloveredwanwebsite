from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBE = [
  {'id': 1,
   'title':'Tunbolare',
   'type of':'RHS AND SHS',
   'size':'0.45 up to 6 mm'},
  {'id':2,
   'title':'Lamera',
   'type of':'HOT ROLED AND COLOD ROLED',
   'size':'0.45 up to 50 mm'},
  {
    'id':3,
   'title':'TONDINO OR ROUND BAR',
   'type of':'ABISINIA AND UKRAIN ROLED',
   'size':'8mm up to 60 mm'
  },
  {
    'id':4,
   'title':'FLAT ROUND BAR',
   'type of':'ABISINIA AND UKRAIN ROLED',
   'size':'10 x 2 mm up to 100 x 6 mm'
    }
]

@app.route("/")
def hello_world():
  return render_template('home.html',  SHARP=JOBE,Company_name='Sharp Construction Material Retail')


@app.route("/api/SHARP")
def list_SHARP():
  return jsonify(JOBE)


if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)