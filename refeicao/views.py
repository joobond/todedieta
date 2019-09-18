from django.shortcuts import render
from pyrebase import pyrebase
from django.http import JsonResponse

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

def cadastrarRefeicao(request):
    return render(request, "cadastrarRefeicao.html")

def refeicaoFormulario(request):
    descricao = request.POST.get('descricao')
    
    data = {"descricao": descricao}
    try:
        db.child("refeicoes").push(data)
        message = "Refeicao "+descricao+" cadastrado com sucesso!"
    except:
        message = "Aconteceu um erro ao cadastrar o refeição"
        return render(request,"cadastrarRefeicao.html",{"msg":message})
    return render(request, "cadastrarRefeicao.html", {"msg":message})

def dadosRefeicao(request):
    refeicaood = db.child("refeicoes").get()
    refeicoes = []
    for refeicao in refeicaood.each():
        refeicoes.append(refeicao.val())
    try:
        return render(request, "refeicao.html", {"refeicoes":refeicoes})
    except:
        message = "Aconteceu um erro ao retornar os refeicoes"
        return render(request,"refeicao.html",{"msg":message})

def autocomplete(request):
    if request.is_ajax():
        descAlimento = str(request.GET.get('descAlimento'))
        alimentosod = db.child("alimentos").get()
        alimentos = []
        for alimento in alimentosod.each():
            if alimento.val()['descricao'] == descAlimento:
                alimentos.append(alimento.val())
        try:
            return JsonResponde(alimentos)
        except:
            msg = "Deu erro ao retornar a lista de alimentos"
            return render (request, "cadastrarRefeicao.html", msg)
    

