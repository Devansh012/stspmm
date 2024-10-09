from django import forms
from .models import Sector, ScopeGroup, ScopeItem, Client, Staff, ContactPerson, ProjectLead, ProjectProposal, Project, DCI

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['sectorName']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ScopeGroupForm(forms.ModelForm):
    class Meta:
        model = ScopeGroup
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ScopeItemForm(forms.ModelForm):
    class Meta:
        model = ScopeItem
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.parent_scopeGroup = kwargs.pop('parent_scopeGroup', None)
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'mobile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['fathersName', 'dateOfBirth', 'addressPresent', 'addressHome', 'email', 'mobile1', 'mobile2']

        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ProjectLeadForm(forms.ModelForm):
    class Meta:
        model = ProjectLead
        fields = ['projectName', 'cost', 'agency', 'scopeItem', 'description', 'approved', 'source', 'sourceDescription']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ProjectProposalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extract parent_projectLead if provided
        self.parent_projectLead = kwargs.pop('parent_projectLead', None)
        super().__init__(*args, **kwargs)

        # # Set the projectLead field's initial value and disable it if provided
        # if self.parent_projectLead:
        #     self.fields['projectLead'].initial = self.parent_projectLead
        #     self.fields['projectLead'].widget.attrs.update({'readonly': True, 'disabled': 'disabled'})

        # Get the currently associated DCI if updating
        if self.instance and self.instance.pk:
            current_dci = self.instance.docControlIndex
        else:
            current_dci = None

        # Filter out DCIs that are already attached to other project proposals
        used_dcis = ProjectProposal.objects.exclude(id=self.instance.pk).values_list('docControlIndex', flat=True)
        self.fields['docControlIndex'].queryset = DCI.objects.exclude(id__in=used_dcis)

        # If updating, ensure the current DCI is included in the queryset
        if current_dci and current_dci not in self.fields['docControlIndex'].queryset:
            self.fields['docControlIndex'].queryset |= DCI.objects.filter(id=current_dci)

        # Apply Bootstrap styling to all fields
        self.apply_bootstrap()

        # Make certain fields required if the proposal is accepted
        if self.instance and self.instance.accepted:
            self.fields['acceptedDate'].required = True
            self.fields['workOrderNo'].required = True
            self.fields['workOrderDate'].required = True
            self.fields['workOrderCost'].required = True

    class Meta:
        model = ProjectProposal
        fields = '__all__'
        widgets = {
            'workOrderDate': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'acceptedDate': forms.DateInput(attrs={'type': 'date'}),   # HTML5 date picker
            'submissionDate': forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
        }

    # Apply Bootstrap classes to all fields
    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    # Add validation logic to ensure only one proposal per project lead
    def clean(self):
        cleaned_data = super().clean()

        # Get the project lead from the form (or instance if updating)
        project_lead = self.cleaned_data.get('projectLead') or self.parent_projectLead

        # If a project proposal already exists for this project lead and it's not the current instance (for updates)
        if ProjectProposal.objects.filter(projectLead=project_lead).exists() and not self.instance.pk:
            raise forms.ValidationError(f"A project proposal for {project_lead} already exists.")

        return cleaned_data




class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        parent_projectProposal = kwargs.pop('parent_projectProposal', None)
        super().__init__(*args, **kwargs)
        if parent_projectProposal:
            self.fields['projectProposal'].initial = parent_projectProposal
            self.fields['projectProposal'].widget.attrs.update({'readonly': True, 'disabled': 'disabled'})

        self.apply_bootstrap()

    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'dateOfCommencement': forms.DateInput(attrs={'type': 'date'}),
            'lastDateOfDelivery': forms.DateInput(attrs={'type': 'date'}),
            'workOrderDate': forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
        }

    def apply_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
