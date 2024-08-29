from django import forms
from .models import Folder, Document

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parentFolder', 'notes', 'protected', 'password']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

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

    def save(self, commit=True):
        document = super().save(commit=False)
        if self.user:
            document.createdBy = self.user
        if commit:
            document.save()
        return document
