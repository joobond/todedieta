from django.shortcuts import render
from django.contrib.auth.models import User
import pyrebase

config = {
    'apiKey': "AIzaSyDg-AD8p3MTB3GhmLqupSO6TKrNqXun8TI",
    'authDomain': "to-de-dieta.firebaseapp.com",
    'databaseURL': "https://to-de-dieta.firebaseio.com",
    'projectId': "to-de-dieta",
    'storageBucket': "to-de-dieta.appspot.com",
    'messagingSenderId': "1053641145914",
    'appId': "1:1053641145914:web:dd47dc648cd5bc11"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

def singIn(request):
    return render(request, "login.html")

def postsign(request):
    email=request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)

    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user)
    return render(request, "welcome.html",{"e":email})