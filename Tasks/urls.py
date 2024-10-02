from django.urls import path
from .import views

urlpatterns = [
    path('tasksList/<int:id>/', views.tasksList, name="tasksList"),
    path('tasksCreateView/<int:id>/', views.tasksCreateView, name="tasksCreateView"),
    path('tasksUpdateView/<int:id>/', views.tasksUpdateView, name="tasksUpdateView"),
    path('tasksDeleteView/<int:id>/', views.tasksDeleteView, name="tasksDeleteView"),
    path('tasks/<int:task_id>/dci-items/', views.task_dci_item_view, name='taskDCIItemView'),
    path('tasks/<int:task_id>/activities/', views.load_task_activities, name='load_task_activities'),


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