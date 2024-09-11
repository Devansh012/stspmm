# forms.py
from django import forms
from .models import Sector,ScopeGroup, ScopeItem, Client, Staff, ContactPerson, ProjectLead, ProjectProposal, Project,  DCI

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = '__all__'
        
class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['sectorName']

class ScopeGroupForm(forms.ModelForm):
    class Meta:
        model = ScopeGroup
        fields = ['name','description']

class ScopeItemForm(forms.ModelForm):
    class Meta:
        model = ScopeItem
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.parent_scopeGroup = kwargs.pop('parent_scopeGroup', None)
        super(ScopeItemForm, self).__init__(*args, **kwargs)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'mobile']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['fathersName', 'dateOfBirth', 'addressPresent', 'addressHome', 'email', 'mobile1', 'mobile2']

        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectLeadForm(forms.ModelForm):
    class Meta:
        model = ProjectLead
        fields = ['projectName', 'cost', 'agency','scopeItem', 'description', 'source', 'sourceDescription']

class ProjectProposalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        parent_projectLead = kwargs.pop('parent_projectLead', None)
        super(ProjectProposalForm, self).__init__(*args, **kwargs)

        if parent_projectLead:
            self.fields['projectLead'].initial = parent_projectLead
            self.fields['projectLead'].widget.attrs['readonly'] = True
            self.fields['projectLead'].widget.attrs['disabled'] = 'disabled'

        # Filter out DCIs that are already attached to project proposals
        used_dcis = ProjectProposal.objects.values_list('docControlIndex', flat=True)
        self.fields['docControlIndex'].queryset = DCI.objects.exclude(id__in=used_dcis)

    class Meta:
        model = ProjectProposal
        fields = '__all__'

        widgets = {    
            'workOrderDate': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'acceptedDate': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'submissionDate': forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
        }


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        parent_projectProposal = kwargs.pop('parent_projectProposal', None)
        super(ProjectForm, self).__init__(*args, **kwargs)
        if parent_projectProposal:
            self.fields['projectProposal'].initial = parent_projectProposal
            self.fields['projectProposal'].widget.attrs['readonly'] = True
            self.fields['projectProposal'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'dateOfCommencement': forms.DateInput(attrs={'type': 'date'}),
            'lastDateOfDelivery': forms.DateInput(attrs={'type': 'date'}),
            'workOrderDate': forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
        }

