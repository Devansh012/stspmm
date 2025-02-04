from django.urls import path
from . import views

urlpatterns = [
    path('folderList/', views.folderList, name="folderList"),
    path('folderCreateView/', views.folderCreateView, name="folderCreateView"),
    # path('folderCreateView/<int:parent_id>/', views.folderCreateView, name="folderCreateView"),
    path('folderUpdateView/<int:id>/', views.folderUpdateView, name="folderUpdateView"),
    path('folderDeleteView/<int:id>/', views.folderDeleteView, name="folderDeleteView"),
    path('folder/toggle-protection/', views.toggle_protection, name='toggle_protection'),
    path('file-explorer/', views.file_explorer, name='file_explorer'),



    path('documentList/<int:id>/', views.documentList, name='documentList'),
    path('documentsDownloadsView/<int:id>/', views.documentsDownloadsView, name='documentsDownloadsView'),
    path('documentCreateView/<int:id>/', views.documentCreateView, name='documentCreateView'),
    path('documentUpdateView/<int:id>/', views.documentUpdateView, name='documentUpdateView'),
    path('documentDeleteView/<int:id>/', views.documentDeleteView, name='documentDeleteView'),
]

