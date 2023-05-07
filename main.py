import pyrebase
import func

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

func.update("users","0715843108","name","Rohini")
#func.retreive("users","0715843108")
#db.child("users").child("0715843108").update({"name": "Rohini"})

#retreive
#users = db.child("User Table").child("0786779000").get()
#print(users.val())

#delete
#db.child("User Table").child("0786779000").child("Age").remove()
