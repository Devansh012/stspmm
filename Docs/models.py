from django.db import models
from django.contrib.auth.models import User

class Folder(models.Model):
    name = models.CharField(max_length=30)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_folders')
    createdDate = models.DateField(auto_now_add=True,blank=True, null=True)
    parentFolder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subfolders')
    notes = models.TextField(blank=True, null=True)
    protected = models.BooleanField(default=False, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Document(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, blank=True, null=True)
    createdDate = models.DateField(auto_now_add=True, blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_documents')
    file = models.FileField(upload_to='documents/', blank=True, null=True)  # New file field

    def __str__(self):
        return self.name if self.name else f"Document #{self.id}"
    
 