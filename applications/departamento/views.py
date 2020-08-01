from django.shortcuts import render
from django.views.generic.edit import FormView #para usar dos modelos

from applications.persona.models import Empleado
from .models import Departamento
from django.views.generic import  (
    ListView ,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    DetailView
    

) 

from .forms import NewDepartamentoForms
# Create your views here.



class List_DepartamentoListView(ListView):
    
    template_name = "departamento/lista-departamento.html"
    model = Departamento
    context_object_name = "departamentos"

    """def get_queryset(self):
        departamento = self.request.GET.get('depa', '') 
        lista = Empleado.objects.filter(
            shor_name__icontains=departamento #icontains para  buscar 
            
        )
        return lista"""
    






class NewDepartamentoView(FormView):#usa 2 models
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForms
    success_url =  '/'

    def form_valid(self, form):

        depa = Departamento(
            name = form.cleaned_data['departamentos'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name= nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentoView,self).form_valid(form)
