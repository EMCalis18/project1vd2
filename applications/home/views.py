from django.shortcuts import render
#import models
from .models import Pruebabase
from django.views.generic import  (
    ListView ,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,

) 
from .forms import PruebaForm
# Create your views here.

from django.views.generic import TemplateView, ListView 
#templatesview para traer vistas genericas
#listview para traer vistas de listas

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listanumeros'
    queryset = ['0', '10', 'hola', '20'] #hace referencia a una lista


class Listadb(CreateView):
    template_name = "home/formprueba.html"
    model = Pruebabase
    form_class = PruebaForm
    success_url = '/'
