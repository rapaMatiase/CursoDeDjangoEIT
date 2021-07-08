
from django.urls import path, include
from .views import Index, Delete, Update
urlpatterns = [
    path('', Index, name='index'),
    path('delete/<int:item_id>', Delete, name='delete'),
    path('update/<int:item_id>', Update, name='update')
]
