from django.urls import path
from. import views
urlpatterns = [
    path('update/', views.UpdateView, name='update'),
    path('datashow/<int:file_id>', views.DataShowView, name='data_show'),
    path('save/<int:file_id>', views.SaveData, name='data_save')
]
