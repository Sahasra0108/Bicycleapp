import pyrebase

config = {
  "apiKey": "AIzaSyDVe_UbuxI4Hw2LO-mfJWQfSKfNFmVYExE",
  "authDomain": "fir-phoneauth1-1208a.firebaseapp.com",
  "databaseURL":
  "https://fir-phoneauth1-1208a-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "fir-phoneauth1-1208a",
  "storageBucket": "fir-phoneauth1-1208a.appspot.com",
  "messagingSenderId": "57907367912",
  "appId": "1:57907367912:web:8812c804b2108d11701e5d",
  "measurementId": "G-8VFK1RBCET"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


#funtion for update
def update(table, id, field, new_value):
  db.child(table).child(id).update({field: new_value})


#funtion for retrive data
def retreive(table, id):
  users = db.child(table).child(id).get()
  print(users.val())


#funtion for delete data
def delete(table, id, field):
  db.child(table).child(id).child(field).remove()