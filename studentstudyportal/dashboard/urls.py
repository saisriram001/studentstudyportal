from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('notes/',views.note,name="notes") ,
    path('delete/<int:pk>', views.delete_note , name = 'del') , 
    path('detail/<int:pk>', views.show_details , name = 'show') , 
    path('homework/',views.homework,name='homework') ,
    path('delt/<int:pk>',views.delete_hw,name='delt'),
    path('youtube/',views.youtube,name='you'),
    path('todo/',views.todo,name='todo'),
    path('del/<int:pk>',views.tdelete,name='de'),
    path('book/',views.book,name='book'),
    path('dictionary/',views.dictionary,name='dict'),
    path('wikipedia/',views.wiki,name='wiki'),
    path('conversion/',views.conversion,name='conv'),
    path('out/',views.lout,name='out')

]