from django import forms
from .models import DCI, DCIGroup, DCIItem

class DCIForm(forms.ModelForm):
    class Meta:
        model = DCI
        fields = '__all__'


class DCIGroupForm(forms.ModelForm):
    class Meta:
        model = DCIGroup
        fields = '__all__'

class DCIItemForm(forms.ModelForm):
    class Meta:
        model = DCIItem
        fields = '__all__'

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()
