from django.shortcuts import render
import random
from django.http import HttpResponse

list = []
resultados = []

def index(request):
    dicio={"chave":[]}
    return render(request,'index.html')

def adicionar(request):
    dicio = {"chave": []}
    grupos = []


    if request.method == "POST":
        nome = request.POST['nome']
        combobox = request.POST['qtdgrupos']
        if combobox == "0":
            list.append(nome)
        else:
            tam = len(list) / int(combobox)

            for i in range(int(combobox)):
                um = []
                for j in range(int(tam)):
                    while True:
                        nome = random.choice(list)
                        if not (nome in um):
                            flag = 0
                            for grupo in grupos :
                                if nome in grupo :
                                    flag = 1
                            if flag == 0 :
                                um.append(nome)
                                break
                        else:
                            pass
                grupos.append(um)
                print(grupos)
        dicio["chave"]=grupos
        print(dicio)

    return render(request, 'index.html',dicio)


