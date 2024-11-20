from django.db import models
# from Project.models import Project
from django.contrib.auth.models import User

class DCI(models.Model):
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True , blank=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    # dciGroups = models.ForeignKey('DCIGroup', on_delete=models.CASCADE, blank=True, null=True)
    cost = models.FloatField(blank=True,null=True)
    def __str__(self):
        return self.name
  
class DCIGroup(models.Model):
    name = models.CharField(max_length=30)
    groupCode = models.CharField(max_length=15, blank=True, null=True)
    # dciItems = models.ForeignKey('DCIItem', on_delete=models.CASCADE, blank=True, null=True)
    dci = models.ForeignKey(DCI , on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class DCIItem(models.Model):
    sNo = models.IntegerField(null= True,blank=True)
    itemCode = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50)
    documentNo = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    likelySubmissionDate = models.DateField(blank=True, null=True)
    weightage = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    associatedCost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    dciGroup = models.ForeignKey('DCIGroup', on_delete=models.CASCADE, blank=True, null=True)
    dci = models.ForeignKey('DCI', on_delete=models.CASCADE, blank=True,null=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    createdDate = models.DateField(auto_now_add=True,blank=True, null=True)
    completed = models.BooleanField(default=False,blank=True,null=True)
    dateOfCompletion = models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        if self.name:
            return self.name
        return f"DCI Item #{self.id}"
