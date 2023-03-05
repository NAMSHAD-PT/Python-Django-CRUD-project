from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='index'),
    path('insert',views.insertData,name='insert'),
    path('update/<id>',views.updateData,name='update'),
    path('delete/<id>',views.deleteData,name='delete'),
]