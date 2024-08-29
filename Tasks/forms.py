from django import forms
from .models import Tasks, TaskActivities, Hinderances, HinderanceFollowUp

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
class TaskActivitiesForm(forms.ModelForm):
    class Meta:
        model = TaskActivities
        fields = [
            # 'task',
            'activityName',
            'activityDescription',
        ]

class HinderancesForm(forms.ModelForm):
    class Meta:
        model = Hinderances
        fields = '__all__'

class HinderanceFollowUpForm(forms.ModelForm):
    class Meta:
        model = HinderanceFollowUp
        fields = [
            'followUpDate',
            'followUpDescription',
            'document',
        ]
