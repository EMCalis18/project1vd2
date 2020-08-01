from django.shortcuts import render
#import models
from .models import Empleado
from django.urls import reverse_lazy

# Create your views here.


from django.views.generic import  (
    ListView ,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    DetailView
    

) 
#FORMS
from .forms import EmpleadoForm   
#templatesview para traer vistas genericas
#listview para traer vistas de listas


class Inicio(TemplateView):#homee--
    template_name = "inicio.html"



class Lista_all(ListView):
    
    template_name = "persona/lista_all.html"
    context_object_name = 'lista'
    paginate_by = 4
    ordering = 'first_name'
    
    def get_queryset(self):
        nombre = self.request.GET.get('kword', '') 
        lista = Empleado.objects.filter(
            first_name__icontains=nombre #icontains para  buscar 
            
        )
        return lista


class Lista_area(ListView):
    """ nombre de los departamentos """
    template_name = "persona/lista_area_all.html"
    context_object_name = 'emplados'
    

    def get_queryset(self):
        area = self.kwargs['shorname']
        Lista_area = Empleado.objects.filter(
            departamento__shor_name = area #departamentp__ porque es de la bd departamento
        )
        return Lista_area
       

class Lista_job(ListView):
    """ lista de los trabajos que hay"""
    template_name = "persona/lista_job.html"
    

    def get_queryset(self):
        if (self.kwargs['job']=='CONTADOR'):
            trabajo = '0'
        elif (self.kwargs['job']=='ADMINISTRADOR'):
            trabajo = '1'

       
        Lista = Empleado.objects.filter(
            job = trabajo
        )
        return Lista



class Lista_Buscar(ListView):
    """ buscar empleado"""
    template_name = "persona/Buscar_empleado.html"
    context_object_name = 'empleado'

    def get_queryset(self):
        nombre = self.request.GET.get('kwargs', '') 
        lista= Empleado.objects.filter(
            first_name = nombre 
        )
        return lista


class Ver_habilidades_empleado(ListView):   
    template_name = "persona/ver_habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        
        habilidades =Empleado.objects.get('valor')
        #Empleado.objects.get(id=self.kwargs['id'])
        

        
        return habilidades.habilidad.all()






        
    

class formulario(CreateView):
    model = Empleado
    template_name = "persona/form-empleado.html"
    form_class = EmpleadoForm 
    #success_url = 'form-empleado' esta forma no conviene
    success_url = reverse_lazy('persona_urls:empleado-admin')

    def form_valid(self, form):#si lo enviado es valido
        empleado = form.save(commit=False)#se guarda en esa variable
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()#para guardar en la db lo nuevo
        return super(formulario,self).form_valid(form)
        #super porque modifica la clase formulario 




class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidad',
        'avatar',
        
    ]
    success_url = reverse_lazy('persona_urls:empleado-admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):#si lo enviado es valido
       
        return super(EmpleadoUpdateView,self).form_valid(form)
        #super porque modifica la clase  
        # 


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_urls:empleado-admin') 


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        return context
    
     

    


class AdministrarListView(ListView):
    template_name = "persona/administrar.html"
    context_object_name = 'lista_administrar'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    

    
