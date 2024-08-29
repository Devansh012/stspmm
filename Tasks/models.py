from django.db import models
from django.contrib.auth.models import User
from Project.models import Project, Staff 
from DCI.models import DCIItem
class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    # dciItem = models.OneToOneField('DCI.DCIItem', on_delete=models.CASCADE, blank=True, null=True)
    taskName = models.CharField(max_length=30, null=True, blank=True)
    taskDescription = models.TextField(blank=True, null=True)
    assignedTo = models.ForeignKey(Staff, on_delete=models.CASCADE, max_length=30, blank=True, null=True)
    assignmentDate = models.DateField(blank=True, null=True)
    targetDateOfCompletion = models.DateField(null=True, blank=True)

    def __str__(self):
        return str (self.project)

 
class TaskActivities(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    dateOfEntry = models.DateField(auto_now_add=True, blank=True, null=True)
    activityName = models.CharField(max_length=30, blank=True, null=True)
    activityDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.task)



class Hinderances(models.Model):
    # project = models.ForeignKey('app.Project', on_delete=models.CASCADE, blank=True, null=True)
    dciItem = models.ForeignKey(DCIItem, on_delete=models.CASCADE, blank=True, null=True)
    dateOfOccurrence = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    associatedStaff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)
    cleared = models.BooleanField(default=False, blank=True, null=True)
    clearedDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.dciItem)


class HinderanceFollowUp(models.Model):
    hinderance = models.ForeignKey(Hinderances, on_delete=models.CASCADE, blank=True,null=True)
    followUpDate = models.DateField(blank=True, null=True)
    followUpDescription = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return str(self.hinderance)


