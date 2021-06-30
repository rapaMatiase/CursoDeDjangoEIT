
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('listArticulos/', views.listArticulos, name='list_articulos'),
    path('detailArticulos/<int:id>', views.detailArticulos, name='detail_articulos'),
    path('form/', views.form, name='form'),
    path('formArticulo/', views.formArtiuclo, name='formArticulo'),
    
]

