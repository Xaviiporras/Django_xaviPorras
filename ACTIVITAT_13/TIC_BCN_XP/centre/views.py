from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def teachers(request):
    profes = [
        {"nom": "Roger", "cognom1": "Sobrino", "cognom2": "", "edat": 39, "rol": "teacher", "cursos": "DAM2B, DAW2A"},
        {"nom": "Josep Oriol", "cognom1": "Roca", "cognom2": "", "edat": 25, "rol": "teacher", "cursos": "DAW2B, DAW2A, DAW1A"},
        {"nom": "Juanma", "cognom1": "Biel", "cognom2": "", "edat": 24, "rol": "teacher", "cursos": "DAW2B, DAW2A"},
    ]
    return render(request, 'teachers.html', {'profes': profes})

def students(request):
    alumnes = [
        {"nom": "Hugo", "cognom1": "Sanssegundo", "cognom2": "Costantini", "correu": "2023_hugo.sanssegundo@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08, Big Data"},
        {"nom": "Adrián", "cognom1": "Navarro", "cognom2": "Pérez", "correu": "2023_adrian.navarro@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Xavi", "cognom1": "Porras", "cognom2": "del Pino", "correu": "2023_xavier.porras@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Javier", "cognom1": "Giménez", "cognom2": "Sánchez", "correu": "2023_javier.gimenez@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Milena", "cognom1": "Vardumyan", "cognom2": "Aleksanyan", "correu": "2023_milena.vardumyan@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M013, Big Data"},
        {"nom": "Daniel", "cognom1": "Vallespin", "cognom2": "Mellado", "correu": "2023_daniel.vallespin@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Félix Bequet", "cognom1": "Balbin", "cognom2": "Silva", "correu": "2023_felix.balbin@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Víctor Andrés", "cognom1": "Fernández", "cognom2": "Álvarez", "correu": "2023_victor.fernandez@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Lila", "cognom1": "Díez", "cognom2": "Zhou", "correu": "2023_lila.diez@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08, ML"},
        {"nom": "Arman", "cognom1": "Mohammed", "cognom2": "Akther", "correu": "2023_arman.mohammed@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"nom": "Albert", "cognom1": "Penadés", "cognom2": "Casajús", "correu": "2023_albert.penades@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08, ML"},
        {"nom": "Natalia", "cognom1": "Casanellas", "cognom2": "Blanquer", "correu": "2023_natalia.casanellas@ticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07"},
    ]
    return render(request, 'students.html', {'alumnes': alumnes})

def index(request):
    return render(request, 'index.html')

# Create your views here.
