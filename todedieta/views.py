from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

auth = firebase.auth()

def viewLogin(request):
    return render(request, "login.html")

def viewLogout(request):
    logout(request)
    return redirect("login")

def logando(request):
    email=request.POST.get("email")
    password = request.POST.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        novoUsuario = auth.get_account_info(user['idToken'])
        infoUser = novoUsuario["users"][0]
        uid = infoUser["localId"]
        username = infoUser["email"]
        # Se o usuário existir no banco de dados local
        usuarios = User.objects.all()
        usuarioLocal = []
        usuarioExiste = False
        for u in usuarios:
            if u.email == username:
                usuarioLocal = u
                usuarioExiste = True
        if not usuarioExiste:
            usuarioLocal = User.objects.create_user(username=username, email=email, password=uid)
            usuarioLocal.save()
        
        autLocal = authenticate(username=username, password=uid)
        login(request, autLocal)
        return redirect("pacientes")
    except:
        message = "Aconteceu algum erro"
        return render(request,"login.html",{"msg":message})