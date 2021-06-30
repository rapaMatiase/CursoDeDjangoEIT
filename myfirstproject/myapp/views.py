from django.shortcuts import render, HttpResponse

# Create your views here.

def myFirstView(request):
    return HttpResponse("Hola, soy tu primera vista 🧑‍🦯")

def mySecondView(request):
    return HttpResponse("Hola, esta es tu segunda vista!!")

def myThirdView(request):
    return HttpResponse("Esta es la tercera!!")

datos = {
    "titulo" : "Mi primera novela",
    "descripcion" : "Hace mucho tiempo atras, habia una vez"
}

def view90(request):
    contenido = """
        <h1 style='color:red;'> {} </h1>
        <p> {} </p>
    """.format(datos['titulo'], datos['descripcion'])
    return HttpResponse(contenido)

def viewHouse(request):
    contenido = """
    <h2> House </h2>
    <p> House M. D. (House en España y Gregory House: Diagnóstico Médico, durante las primeras temporadas en Hispanoamérica) es una serie de televisión estadounidense estrenada en 2004 por la cadena FOX y finalizada en 2012. Fue creada por David Shore, quien además es productor ejecutivo junto a otros como Paul Attanasio, Katie Jacobs o Bryan Singer. El personaje central es el Dr. Gregory House (Hugh Laurie), un genio médico, irónico, satírico y poco convencional e inconformista, que encabeza un equipo de diagnóstico en el ficticio Hospital Universitario Princeton-Plainsboro de Nueva Jersey. El argumento fue idea de Paul Attanasio, basándose en una columna médica escrita por la Dra. Lisa Sanders en el periódico The New York Times, mientras que la creación de los personajes corrió a cargo de Shore después de su visita a un hospital universitario. Las localizaciones están situadas en Century City, un distrito de Los Ángeles, California. </p>
    """
    return HttpResponse(contenido)
