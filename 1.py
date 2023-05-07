import pyrebase
from flask import Flask, request, render_template

config = {
  "apiKey": "AIzaSyDPKPPhR4AhwltgUjgXKUxQiYNSv-_tTIk",
  "authDomain": "bicycleapp-2e6f1.firebaseapp.com",
  "databaseURL": "https://bicycleapp-2e6f1-default-rtdb.firebaseio.com",
  "projectId": "bicycleapp-2e6f1",
  "storageBucket": "bicycleapp-2e6f1.appspot.com",
  "messagingSenderId": "489283898986",
  "appId": "1:489283898986:web:72852454488db723e54413",
  "measurementId": "G-30W5D4VXFP"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def basic():
  if request.method == 'POST':
    if 'submit' in request.form and request.form['submit'] == 'update':
      tel_num = request.form['telnum']
      field = request.form['field']
      new_value = request.form['newvalue']
      db.child("User Table").child(tel_num).update({field: new_value})
    elif 'submit' in request.form and request.form['submit'] == 'delete':
      tel_num = request.form['telnum']
      db.child("User Table").child(tel_num).remove()
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
