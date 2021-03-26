from django.urls import path

from demoapp.views import (
    getlist,
    edit_data,
    delete_data,
    add_data,
    detail_data
)


app_name= 'demoapp'

urlpatterns =[
    path('view/', getlist, name='view'),
    path('detail/<int:id>/', detail_data, name='detail'),
    path('edit/<int:id>/', edit_data, name='edit'),
    path('delete/<int:id>/', delete_data, name='delete'),
    path('add/', add_data, name='add'),
]