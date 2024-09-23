from django import forms
from .models import Submissions, DocumentSubmissionAgency, DocumentSubmissionAgencyType

# Helper function to apply 'form-control' class to all form fields
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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply form-control class to all fields
        apply_form_control(self.fields)
        # Restrict file types to PDF and Word documents for the commentDocument field
        self.fields['commentDocument'].widget.attrs.update({'accept': '.pdf,.doc,.docx'})
        # Restrict file types to PDF and Word documents for the replyDocument field
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
