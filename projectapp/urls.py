from django.urls import path 
from projectapp import views

urlpatterns = [
    path('',views.Indexpage,name='Indexpage'),
    path('Table',views.Table,name='Table'),
    path('Edit_data_page/<int:pk>/',views.Edit_data_page,name='Edit_data_page'),

    path('Savedata',views.Savedata,name='Savedata'),

    path('Edit_data/<int:pk>/',views.Edit_data,name='Edit_data'),
    path('Delete_data/<int:pk>/',views.Delete_data,name='Delete_data'),

]