from django.urls import path
from .import views

urlpatterns = [
    path('tasksList/', views.tasksList, name="tasksList"),
    path('tasksCreateView/', views.tasksCreateView, name="tasksCreateView"),
    path('tasksUpdateView/<int:id>/', views.tasksUpdateView, name="tasksUpdateView"),
    path('tasksDeleteView/<int:id>/', views.tasksDeleteView, name="tasksDeleteView"),

    path('taskActivitiesList/<int:id>', views.taskActivitiesList, name='taskActivitiesList'),
    path('taskActivitiesCreateView/<int:id>', views.taskActivitiesCreateView, name='taskActivitiesCreateView'),
    path('taskActivitiesUpdateView/<int:id>', views.taskActivitiesUpdateView, name='taskActivitiesUpdateView'),
    path('taskActivitiesDeleteView/<int:id>', views.taskActivitiesDeleteView, name='taskActivitiesDeleteView'),

    path('hinderancesList/', views.hinderancesList, name='hinderancesList'),
    path('hinderancesCreateView/', views.hinderancesCreateView, name='hinderancesCreateView'),
    path('hinderancesUpdateView/<int:id>/', views.hinderancesUpdateView, name='hinderancesUpdateView'),
    path('hinderancesDeleteView/<int:id>/', views.hinderancesDeleteView, name='hinderancesDeleteView'),

    path('hinderanceFollowUpList/<int:id>', views.hinderanceFollowUpList, name="hinderanceFollowUpList"),
    path('documentDownloadView/<int:id>/',views.documentDownloadView,name = "documentDownloadView"),
    path('hinderanceFollowUpCreateView/<int:id>',views.hinderanceFollowUpCreateView, name="hinderanceFollowUpCreateView"),
    path('hinderanceFollowUpUpdateView/<int:id>', views.hinderanceFollowUpUpdateView, name="hinderanceFollowUpUpdateView"),
    path('hinderanceFollowUpDeleteView/<id>',views.hinderanceFollowUpDeleteView,name ="hinderanceFollowUpDeleteView"),






]