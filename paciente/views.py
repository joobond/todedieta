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

def cadastrarPaciente(request):
    return render(request, "cadastrarPaciente.html")

def pacienteFormulario(request):
    email = request.POST.get('email')
    idade = request.POST.get('idade')
    nivel = request.POST.get('nivel')
    nome = request.POST.get('nome')
    peso = request.POST.get('peso')
    telefone = request.POST.get('telefone')
    
    data = {"email": email, "idade":idade, "nivel":nivel, "nome":nome, "peso":peso, "telefone":telefone}
    try:
        db.child("pacientes").push(data)
        message = "Paciente "+nome+" cadastrado com sucesso!"
    except:
        message = "Aconteceu um erro ao cadastrar o paciente"
        return render(request,"cadastrarPaciente.html",{"msg":message})
    return render(request, "cadastrarPaciente.html", {"msg":message})

def dadosPaciente(request):
    pacientesod = db.child("pacientes").get()
    pacientes = []
    for paciente in pacientesod.each():
        pacientes.append(paciente.val())
    try:
        return render(request, "pacientes.html", {"pacientes":pacientes})
    except:
        message = "Aconteceu um erro ao retornar os paciente"
        return render(request,"pacientes.html",{"msg":message})
    

