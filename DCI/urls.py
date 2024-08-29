from django.urls import path
from . import views

urlpatterns = [
    path('dciList', views.dciList, name='dciList'),
    path('dciCreateView',views.dciCreateView, name="dciCreateView"),
    path('dciUpdateView/<id>', views.dciUpdateView, name="dciUpdateView"),
    path('dciDeleteView/<id>',views.dciDeleteView,name ="dciDeleteView"),
   
    path('dciOfDciGroup/<int:id>/', views.dciOfDciGroup, name='dciOfDciGroup'),
    path('dciGroupCreateView/<int:id>/', views.dciGroupCreateView, name="dciGroupCreateView"),  # Updated URL pattern
    path('dciGroupUpdateView/<id>', views.dciGroupUpdateView, name="dciGroupUpdateView"),
    path('dciGroupDeleteView/<int:id>/', views.dciGroupDeleteView, name="dciGroupDeleteView"),

    path('dciItemList<int:id>/', views.dciItemList, name='dciItemList'),
    path('dciItemCreateView/<int:id>',views.dciItemCreateView, name="dciItemCreateView"),
    path('dciItemUpdateView/<int:id>', views.dciItemUpdateView, name="dciItemUpdateView"),
    path('dciItemDeleteView/<int:id>/', views.dciItemDeleteView, name="dciItemDeleteView"),
    
]