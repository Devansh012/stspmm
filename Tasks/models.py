from django.db import models
from django.contrib.auth.models import User
from Project.models import Project, Staff 
from DCI.models import DCIItem,DCIGroup
class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    dciItem = models.ManyToManyField('DCI.DCIItem')
    taskName = models.CharField(max_length=30, null=True, blank=True,verbose_name='Task Name')
    taskDescription = models.TextField(blank=True, null=True)
    assignedTo = models.ForeignKey(Staff, on_delete=models.CASCADE, max_length=30, blank=True, null=True)
    assignmentDate = models.DateField(auto_now_add=True,blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    targetDateOfCompletion = models.DateField(null=True, blank=True)
    actualDateOfCompletion = models.DateField(null=True, blank=True)

    def __str__(self):
        return str (self.project)

 
class TaskActivities(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    dateOfEntry = models.DateField(auto_now_add=True, blank=True, null=True)
    completed =  models.BooleanField(default=False, blank=True, null=True)
    completionDate = models.DateField( blank=True, null=True)
    entryDoneBy = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True, related_name='entryDone')
    activityName = models.CharField(max_length=30, blank=True, null=True)
    activityDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.task)



class Hinderances(models.Model):
    # project = models.ForeignKey('app.Project', on_delete=models.CASCADE, blank=True, null=True)
    dciItem = models.ForeignKey(DCIItem, on_delete=models.CASCADE, blank=True, null=True)
    dateOfOccurrence = models.DateField(blank=True, null=True, verbose_name='Date of Occurance')
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
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return str(self.hinderance)


