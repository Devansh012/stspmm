# forms.py
from django import forms
from .models import Sector, ScopeItem, Client, Staff, ContactPerson, ProjectLead, ProjectProposal, Project

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = ['name', 'position', 'email', 'mobile1', 'mobile2', 'landline']
        
class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['sectorName']

class ScopeItemForm(forms.ModelForm):
    class Meta:
        model = ScopeItem
        fields = ['name']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'mobile']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['fathersName', 'dateOfBirth', 'addressPresent', 'addressHome', 'email', 'mobile1', 'mobile2']


class ProjectLeadForm(forms.ModelForm):
    class Meta:
        model = ProjectLead
        fields = ['projectName', 'cost', 'agency', 'description', 'source', 'sourceDescription']

class ProjectProposalForm(forms.ModelForm):
    class Meta:
        model = ProjectProposal
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
