from django.urls import path
from .import views

urlpatterns = [
    path('submissionsList', views.submissionsList, name="submissionsList"),
    path('submissionsCreateView/',views.submissionsCreateView, name="submissionsCreateView"),
    path('submissionsUpdateView/<id>', views.submissionsUpdateView, name="submissionsUpdateView"),
    path('submissionsDeleteView/<id>',views.submissionsDeleteView,name ="submissionsDeleteView"),

    path('dsaList/<int:id>/', views.dsaList, name='dsaList'),
    path('dsaCreateView/<int:id>/', views.dsaCreateView, name='dsaCreateView'),
    path('dsaUpdateView/<int:id>/', views.dsaUpdateView, name='dsaUpdateView'),
    path('dsaDeleteView/<int:id>/', views.dsaDeleteView, name='dsaDeleteView'),


    path('dsatList/', views.dsatList, name="dsatList"),
    path('dsatCreateView',views.dsatCreateView, name="dsatCreateView"),
    path('dsatUpdateView/<id>', views.dsatUpdateView, name="dsatUpdateView"),
    path('dsatDeleteView/<id>',views.dsatDeleteView,name ="dsatDeleteView"),

]