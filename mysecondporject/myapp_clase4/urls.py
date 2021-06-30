
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('friends/', views.ListFriends, name="list_friends"),
    path('listtodo/<int:user_id>', views.ListListToDo, name='list_todo'),
    path('listdetail/<int:user_id>/<int:list_id>', views.ListDetail, name='list_detail'),
    path('ctacte/<int:user_id>', views.CtaCteView, name="ctacte"),
    path('delete/<int:user_id>/<int:list_id>/<int:item_id>', views.ListItemDelete, name='deleteItem')

]
