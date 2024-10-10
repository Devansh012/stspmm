from django import forms
from .models import Folder, Document

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parentFolder', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Set rows to 3

        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Add Bootstrap class to fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Conditionally disable parentFolder if necessary
        if self.instance and self.instance.pk:
            self.fields['parentFolder'].disabled = True

    def save(self, commit=True):
        folder = super().save(commit=False)
        if self.user:
            folder.createdBy = self.user
        if commit:
            folder.save()
        return folder

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Add Bootstrap class to fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        document = super().save(commit=False)
        if self.user:
            document.createdBy = self.user
        if commit:
            document.save()
        return document
