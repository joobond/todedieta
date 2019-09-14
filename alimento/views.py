from django.shortcuts import render
from pyrebase import pyrebase

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
db = firebase.database()

def cadastrarAlimento(request):
    return render(request, "cadastrarAlimento.html")

def alimentoFormulario(request):
    descricao = request.POST.get('descricao')
    porcao = request.POST.get('porcao')
    unidade = request.POST.get('unidade')
    
    data = {"descricao": descricao, "porcao":porcao, "unidade":unidade}
    try:
        db.child("alimentos").push(data)
        message = "Alimento "+descricao+" cadastrado com sucesso!"
    except:
        message = "Aconteceu um erro ao cadastrar o alimento"
        return render(request,"cadastrarAlimento.html",{"msg":message})
    return render(request, "cadastrarAlimento.html", {"msg":message})

def dadosAlimento(request):
    alimentosod = db.child("alimentos").get()
    alimentos = []
    for alimento in alimentosod.each():
        alimentos.append(alimento.val())
    try:
        return render(request, "alimentos.html", {"alimentos":alimentos})
    except:
        message = "Aconteceu um erro ao retornar os alimentos"
        return render(request,"alimentos.html",{"msg":message})
    

