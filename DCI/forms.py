from django import forms
from .models import DCI, DCIGroup, DCIItem

class DCIForm(forms.ModelForm):
    class Meta:
        model = DCI
        fields = '__all__'


class DCIGroupForm(forms.ModelForm):
    class Meta:
        model = DCIGroup
        fields = ['name', 'groupCode']  # Explicitly exclude 'dci' from the form
    
    def __init__(self, *args, **kwargs):
        parent_dci = kwargs.pop('parent_dci', None)
        super(DCIGroupForm, self).__init__(*args, **kwargs)
        
        if parent_dci:
            self.fields['dci'] = forms.ModelChoiceField(queryset=DCI.objects.filter(id=parent_dci.id), initial=parent_dci, disabled=True)

class DCIItemForm(forms.ModelForm):
    class Meta:
        model = DCIItem
        fields = ['sNo', 'itemCode', 'name', 'documentNo', 'description', 'likelySubmissionDate', 'weightage', 'associatedCost', 'dciGroup']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.dci_group = kwargs.pop('dci_group', None)
        super().__init__(*args, **kwargs)

        # Disable the dciGroup field and set its value
        self.fields['dciGroup'].disabled = True
        if self.dci_group:
            self.fields['dciGroup'].initial = self.dci_group

    def save(self, commit=True):
        dci_item = super().save(commit=False)
        if self.user:
            dci_item.createdBy = self.user
        if self.dci_group:
            dci_item.dciGroup = self.dci_group
        if commit:
            dci_item.save()
        return dci_item




class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()
