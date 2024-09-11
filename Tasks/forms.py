from django import forms
from .models import Tasks, TaskActivities, Hinderances, HinderanceFollowUp

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)  # Remove the project from kwargs if passed
        super(TasksForm, self).__init__(*args, **kwargs)
        
        if project:  # If a project is provided
            self.fields['project'].initial = project  # Set the initial value for the project field
            self.fields['project'].widget.attrs['readonly'] = True  # Disable the project field
            self.fields['project'].widget.attrs['disabled'] = 'disabled'

class TaskActivitiesForm(forms.ModelForm):
    class Meta:
        model = TaskActivities
        fields = '__all__'
        widgets = {
            'dateOfEntry': forms.HiddenInput(),  # Hide the dateOfEntry field if you want to prevent it from being edited
            'entryDoneBy': forms.HiddenInput(),  # Hide the entryDoneBy field from the form
            'completionDate': forms.DateInput(attrs={'type': 'date'}),

        }
        

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['entryDoneBy'].initial = user
            self.fields['entryDoneBy'].widget.attrs['readonly'] = True
            self.fields['entryDoneBy'].required = False  # Make sure the field is not required

    # def __init__(self, *args, **kwargs):
    #     # Pop the 'task' from kwargs if it's provided
    #     task = kwargs.pop('task', None)
    #     super(TaskActivitiesForm, self).__init__(*args, **kwargs)

    #     if task:
    #         # Dynamically add the task field to the form
    #         self.fields['task'] = forms.ModelChoiceField(
    #             queryset=Tasks.objects.filter(id=task.id),
    #             initial=task,
    #             # widget=forms.HiddenInput()  # Make it hidden
    #         )
    #     else:
    #         # Ensure task field does not show up if not provided
    #         self.fields.pop('task', None)


class HinderancesForm(forms.ModelForm):
    class Meta:
        model = Hinderances
        fields = '__all__'

        widgets = {
            'dateOfOccurrence': forms.DateInput(attrs={'type': 'date'}),
            'clearedDate': forms.DateInput(attrs={'type': 'date'}),
        }

class HinderanceFollowUpForm(forms.ModelForm):
    class Meta:
        model = HinderanceFollowUp
        fields = [
            'followUpDate',
            'followUpDescription',
            'document',
        ]

        widgets = {
            'followUpDate': forms.DateInput(attrs={'type': 'date'}),
        }
