from django.shortcuts import render

def index2(request):
    return render(request,'templatesProductos/index2.html')

def messi(request):
    data={
        "nombre":"Lionel Messi",
        'edad':"36",
        'altura':"1,70",
        'descripcion':"Jugador argentino",
        'imagen':'imagenes/messi.png'
    }
    return render(request,'templatesProductos/index2.html',data)

def koby(request):
    data={
        "nombre":"koby bryant",
        'edad':"41",
        'altura':"1,98",
        'descripcion':"Jugador estadounidense",
        'imagen':'imagenes/koby.png'
    }
    return render(request,'templatesProductos/index2.html',data)

def alexisbigote(request):
    data={
        "nombre":"Alexis Sanchez",
        'edad':"34",
        'altura':"1,69",
        'descripcion':"Jugador Chileno",
        'imagen':'imagenes/alexisbigote.png'
    }
    return render(request,'templatesProductos/index2.html',data)

def cr7(request):
    data={
        "nombre":"Cristiano Ronaldo",
        'edad':"38",
        'altura':"1,87",
        'descripcion':"Jugador portugues",
        'imagen':'imagenes/cr7.png'
    }
    return render(request,'templatesProductos/index2.html',data)

# Create your views here.
