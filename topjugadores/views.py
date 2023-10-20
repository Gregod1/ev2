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
    return render(request,'templatesProductos/index2',data)

def koby(request):
    data={
        "nombre":"koby bryant",
        'edad':"41",
        'altura':"1,98",
        'descripcion':"Jugador estadounidense",
        'imagen':'imagenes/koby.png'
    }
    return render(request,'templatesProductos/index2',data)

def alexisbigote(request):
    data={
        "nombre":"Lionel Messi",
        'edad':"36",
        'altura':"1,70",
        'descripcion':"Jugador argentino",
        'imagen':'imagenes/messi.png'
    }
    return render(request,'templatesProductos/index2',data)

# Create your views here.
