from django.contrib import admin
from django.urls import path
from . import views


app_name = 'persona_urls'

urlpatterns = [
     path(
        '', 
        views.Inicio.as_view(),
        name='inicio'
    ),
    path(
        'lista-all/',
        views.Lista_all.as_view(),
        name='empleados-all'
     ),
    path(
        'lista-area/<shorname>',
         views.Lista_area.as_view(),
         name='lista_area_empleado'
         ),
         
    path('lista-job/<job>', views.Lista_job.as_view()),
    path('buscar-empleado/', views.Lista_Buscar.as_view()),
    path('ver-habilidades/', views.Ver_habilidades_empleado.as_view()),
    path(
        'form-empleado/',
         views.formulario.as_view(),
         name='form'
         ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar'
    ),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado-detail'
    ),
    path(
        'ver-empleado-admin',
        views.AdministrarListView.as_view(),
        name='empleado-admin'
    ),
]
