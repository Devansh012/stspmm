from django import forms
from .models import Submissions, DocumentSubmissionAgency, DocumentSubmissionAgencyType

def apply_form_control(fields):
    for field in fields.values():
        if field.widget.attrs.get('class'):
            field.widget.attrs['class'] += ' form-control'
        else:
            field.widget.attrs['class'] = 'form-control'

# Submissions Form
class SubmissionsForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = '__all__'
        widgets = {
            'checkingDate': forms.DateInput(attrs={'type': 'date'}),
            'printingDate': forms.DateInput(attrs={'type': 'date'}),
            'submissionDate': forms.DateInput(attrs={'type': 'date'}),
            'approvalDate': forms.DateInput(attrs={'type': 'date'}),
            'dciItems': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Use SelectMultiple widget for dciItems
            'whyRevision': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Set rows to 3
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Set rows to 3
            'commentIfAny': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Set rows to 3
            'commentReply': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Set rows to 3

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)
        # Restrict file types for document uploads
        self.fields['commentDocument'].widget.attrs.update({'accept': '.pdf,.doc,.docx'})
        self.fields['replyDocument'].widget.attrs.update({'accept': '.pdf,.doc,.docx'})

        
# DocumentSubmissionAgency Form
class DocumentSubmissionAgencyForm(forms.ModelForm):
    class Meta:
        model = DocumentSubmissionAgency
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)

# DocumentSubmissionAgencyType Form
class DocumentSubmissionAgencyTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentSubmissionAgencyType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)
