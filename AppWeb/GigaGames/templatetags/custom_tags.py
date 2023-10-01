from django import template
from django.template.loader import get_template
from GigaGames.models import Categoria

register = template.Library()

def cargar_categorias():

    cat = Categoria.objects.all()

    print(cat)

    return {'categorias' : cat}

template_categorias = get_template('categorias_navbar.html')
register.inclusion_tag(template_categorias)(cargar_categorias)