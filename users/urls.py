from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index,name='index'),
    path('home/',views.home,name='home'),
    path('adduser/',views.adduser,name='add'),
    path('edituser/<id>',views.edituser,name="edit"),
    path('editionuser/',views.editionuser,name="editionuser"),
    path('deleteuser/<id>',views.deleteuser,name='delete'),
]