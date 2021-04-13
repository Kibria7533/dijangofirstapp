from django.urls import  path
from .views import st,list_view,update_view,delete

urlpatterns={
    path('',st,name="student"),
    path('listview/', list_view,name="list_student"),
    path('update/<id>',update_view,name="update_student"),
    path('delete/<id>', delete ,name="delete_student"),
}