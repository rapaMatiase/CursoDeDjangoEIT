from django.urls import path
from . import views

#path('url a escribir en el browser/', vista, name de url)
urlpatterns = [
    path('myview/', views.myFirstView, name='myfirstview'),
    path('mysecondview/', views.mySecondView, name='mysecondview'),
    path('mythirdview/', views.myThirdView, name='mythirdview'),
    path('viewVieja/', views.view90, name='noventera'),
    path('house/', views.viewHouse, name="house")
]
