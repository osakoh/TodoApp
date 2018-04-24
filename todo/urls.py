from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('done/<id>', views.done, name='done'),
    path('undone/<id>', views.undone, name='undone'),
    path('delete/<id>', views.delete, name='delete'),

]