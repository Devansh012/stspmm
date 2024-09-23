from django import forms
from .models import Tasks, TaskActivities, Hinderances, HinderanceFollowUp

# Helper function to apply 'form-control' class to all form fields
def apply_form_control(fields):
    for field in fields.values():
        if field.widget.attrs.get('class'):
            field.widget.attrs['class'] += ' form-control'
        else:
            field.widget.attrs['class'] = 'form-control'

# Tasks Form
class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)  # Remove the project from kwargs if passed
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)
        
        if project:  # If a project is provided
            self.fields['project'].initial = project  # Set the initial value for the project field
            self.fields['project'].widget.attrs['readonly'] = True  # Disable the project field
            self.fields['project'].widget.attrs['disabled'] = 'disabled'

# Task Activities Form
class TaskActivitiesForm(forms.ModelForm):
    class Meta:
        model = TaskActivities
        fields = '__all__'
        widgets = {
            'dateOfEntry': forms.HiddenInput(),  # Hide the dateOfEntry field if you want to prevent it from being edited
            'entryDoneBy': forms.HiddenInput(),  # Hide the entryDoneBy field from the form
            'completionDate': forms.DateInput(attrs={'type': 'date'}),  # Date picker for completionDate
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)

        if user:
            self.fields['entryDoneBy'].initial = user
            self.fields['entryDoneBy'].widget.attrs['readonly'] = True
            self.fields['entryDoneBy'].required = False  # Make sure the field is not required

# Hinderances Form
class HinderancesForm(forms.ModelForm):
    class Meta:
        model = Hinderances
        fields = '__all__'
        widgets = {
            'dateOfOccurrence': forms.DateInput(attrs={'type': 'date'}),  # Date picker for dateOfOccurrence
            'clearedDate': forms.DateInput(attrs={'type': 'date'}),  # Date picker for clearedDate
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)

# Hinderance Follow-Up Form
class HinderanceFollowUpForm(forms.ModelForm):
    class Meta:
        model = HinderanceFollowUp
        fields = [
            'followUpDate',
            'followUpDescription',
            'document',
        ]
        widgets = {
            'followUpDate': forms.DateInput(attrs={'type': 'date'}),  # Date picker for followUpDate
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)
