from django import forms
from .models import Submissions, DocumentSubmissionAgency, DocumentSubmissionAgencyType

class SubmissionsForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(SubmissionsForm, self).__init__(*args, **kwargs)
        # Restrict file types to PDF and Word documents for the commentDocument field
        self.fields['commentDocument'].widget.attrs.update({'accept': '.pdf,.doc,.docx'})
        # Restrict file types to PDF and Word documents for the replyDocument field
        self.fields['replyDocument'].widget.attrs.update({'accept': '.pdf,.doc,.docx'})

class DocumentSubmissionAgencyForm(forms.ModelForm):
    class Meta:
        model = DocumentSubmissionAgency
        fields = '__all__'

class DocumentSubmissionAgencyTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentSubmissionAgencyType
        fields = '__all__'
