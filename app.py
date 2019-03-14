# loe sisse flaski moodul
from flask import Flask 

# flask tahab, et sa nii ytleks
app = Flask(__name__)   

# siin all ytled, mis teha selle urli jaoks
@app.route("/")  
def hello():
  return "Tere tali!"

# pane flask kaima debug rezhiimis pordil 5000
app.run(debug=True, port=5000)
