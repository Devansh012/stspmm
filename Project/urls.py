from django.urls import path
from .import views

urlpatterns = [
    path('projectList/', views.projectList, name='projectList'),
    path('projectCreateView/', views.projectCreateView, name='projectCreateView'),
    path('projectUpdateView/<id>', views.projectUpdateView, name='projectUpdateView'),
    path('projectDeleteView/<id>', views.projectDeleteView, name='projectDeleteView'),

    path('sectorList', views.sectorList, name="sectorList"),
    path('create',views.sectorCreateView, name="sectorCreateView"),
    path('update/<id>', views.sectorUpdateView, name="sectorUpdateView"),
    path('delete/<id>',views.sectorDeleteView,name ="sectorDeleteView"),

    path('scopeItemList/', views.scopeItemList, name='scopeItemList'),
    path('scopeItemCreateView/', views.scopeItemCreateView, name='scopeItemCreateView'),
    path('scopeItemUpdateView/<id>', views.scopeItemUpdateView, name='scopeItemUpdateView'),
    path('scopeItemDeleteView/<id>', views.scopeItemDeleteView, name='scopeItemDeleteView'),

    path('clientList/', views.clientList, name="clientList"),
    path('clientCreateView',views.clientCreateView, name="clientCreateView"),
    path('clientUpdateView/<id>', views.clientUpdateView, name="clientUpdateView"),
    path('clientDeleteView/<id>',views.clientDeleteView,name ="clientDeleteView"),

    path('staffList/', views.staffList, name='staffList'),
    path('staffCreateView/', views.staffCreateView, name='staffCreateView'),
    path('staffUpdateView/<id>', views.staffUpdateView, name='staffUpdateView'),
    path('staffDeleteView/<id>', views.staffDeleteView, name='staffDeleteView'),

    path('cpList/', views.cpList, name="cpList"),
    path('cpCreateView/', views.cpCreateView, name="cpCreateView"),  
    path('cpUpdateView/<int:id>/', views.cpUpdateView, name="cpUpdateView"),  
    path('cpDeleteView/<int:id>/', views.cpDeleteView, name="cpDeleteView"),  

    path('plList/<int:id>', views.plList, name='plList'),
    path('create/', views.plCreateView, name='plCreateView'),
    path('update/<id>', views.plUpdateView, name='plUpdateView'),
    path('delete/<id>', views.plDeleteView, name='plDeleteView'),

    path('ppList/<int:id>/', views.ppList, name="ppList"),
    path('ppCreateView/<int:id>/',views.ppCreateView, name="ppCreateView"),
    path('ppUpdateView/<id>', views.ppUpdateView, name="ppUpdateView"),
    path('ppDeleteView/<id>',views.ppDeleteView,name ="ppDeleteView"),

    
]

