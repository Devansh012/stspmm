# forms.py
from django import forms
from .models import Submissions, DocumentSubmissionAgency, DocumentSubmissionAgencyType

class SubmissionsForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = '__all__'

class DocumentSubmissionAgencyForm(forms.ModelForm):
    class Meta:
        model = DocumentSubmissionAgency
        fields = '__all__'

class DocumentSubmissionAgencyTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentSubmissionAgencyType
        fields = '__all__'
